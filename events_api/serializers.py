import collections

from django.db.models import Q
from rest_framework import serializers, pagination, request
import shortuuid
import uuid

from django.conf import settings

from oauth2_provider.models import AccessToken

import requests
import json
from rest_framework.settings import api_settings


from rest_framework.validators import UniqueTogetherValidator

from django.core.exceptions import ValidationError
from datetime import datetime as DateTime, timedelta as TimeDelta
from datetime import datetime
import sys
from rest_framework.pagination import PageNumberPagination
from collabo_events.models import Event, EventCategory, ButtonText, CategoryImage, Slot, Price_Category, City, SlotPC, \
    PaymentMethod, Facility, Seller, EventSeller, Host
from .models import Orders,OrderItems
from collabo_events.serializers import EventSerializer,ArtistSerializer
import sys,traceback
sys.path.append("..")

import logging

class OrderItemsUserSerializer(serializers.ModelSerializer):
    #count = serializers.SerializerMethodField('is_named_bar')
    #item_id=serializers.IntegerField( write_only=True)





    class Meta:
        model = OrderItems


        fields = ('item_name','count')



class OrderItemsSerializer(serializers.ModelSerializer):
    #count = serializers.SerializerMethodField('is_named_bar')
    item_id=serializers.IntegerField( write_only=True)





    class Meta:
        model = OrderItems
        extra_kwargs = {'count':{'read_only': False}}

        fields = ('item_id','item_name','pc_cat','pc_slot','count','item_price','additional_charge')



class PaymentMethodSerializer(serializers.ModelSerializer):


    class Meta:
        model = PaymentMethod

        fields = ('name','slug')

class EventOrderSerializer(serializers.ModelSerializer):

    io_id = OrderItemsSerializer(many=True,)
    #payment_status =serializers.CharField(source='get_payment_display')
    payment_status = serializers.SerializerMethodField()
    #payment_method = serializers.CharField(source='Pa.name')
    payment_method = serializers.SlugRelatedField(
        many=False,
        queryset=PaymentMethod.objects.all(),
        slug_field='slug',
        required=False

    )

    #payment_method=serializers.CharField(source='payment.')
    #payment_method = serializers.RelatedField(source='payment_method', read_only=False)
    #payment_method = PaymentMethodSerializer(source="payment_method.name")
    #payment_method=serializers.Payme


#access_token=serializers.CharField(required=False,read_only=False)
    #saloon_name=SaloonSerializer()



    def get_payment_status(self, obj):
        print(obj.get_payment_status_display)
        return str(obj.get_payment_status_display())
    #order_status = serializers.CharField(source='get_order_status_display')


    #saloon_name=SaloonsSerializer(required=True)




    class Meta:
        model = Orders

        fields = ('event','slot','cust_name', 'cust_email', 'cust_phone','payment_method','ordercreatedtime','grandtotal','io_id','order_no','payment_status','order_status',"id",'ticket_code','seller','is_order_seller')
        print("test")
        #fields = '__all__'

        # validators = [
        #
        #     UniqueTogetherValidator(
        #         queryset=Orders.objects.all(),
        #         fields=('cust_name', 'cust_email', 'cust_phone',)
        #     )
        # ]


    def create(self, validated_data):

        print((self.context['request'].user))
        print("INSIDE CREATE")
        logging.debug("INSEIDE CREATE")
        print(validated_data)
        user=self.context['request'].user
        print(user)

        order_items = validated_data.pop('io_id')
        print(validated_data)
        #access_token=validated_data.pop('access_token')
        #print(access_token)
        #user = AccessToken.objects.get(token=access_token).user
        #user=self.instance
        print("USER")
        validated_data['user'] = user
        #print(validated_data['id'])

        #validated_data['ticket_code']=(uuid.uuid4().hex[:6].upper())
        validated_data['ticket_code']=(uuid.uuid4().hex[:6].upper())

        print(validated_data['ticket_code'])
        print("PAYMENT_METHOD *************")
        #print(validated_data['payment_method'])
        #print(validated_data)

        #print(order_items)

        flag=0


        total=0.00
        try:

            for order_item in order_items:

                itemid = order_item.pop('item_id')
                print("Itemid")
                print(itemid)

                logging.debug(itemid)
                #pc_slot=order_item.pop('pc_slot').seating_id

                try:
                    if(Price_Category.objects.values_list('title', flat=True).get(pk=itemid)!=order_item['item_name']):
                        logging.debug("Item id and name mismatch for  item")

                        raise serializers.ValidationError("Item id and name mismatch for  item"+str(order_item['item_name'])+" "+str(order_item['item_price']))

                    if (Price_Category.objects.values_list('price', flat=True).get(pk=itemid) != order_item['item_price']):

                        logging.debug("Item expected price and actual price mismatch for item")
                        raise serializers.ValidationError("Item expected price and actual price mismatch for item "+str(order_item['item_name'])+" "+str(order_item['item_price']))
                    #tax=item.objects.values_list('tax', flat=True).get(pk=itemid)

                    price=Price_Category.objects.values_list('price', flat=True).get(pk=itemid)
                    logging.debug(price)
                    additional_charges=Price_Category.objects.values_list('additional_charge', flat=True).get(pk=itemid)
                    #print(tax)
                    print(price)


                    # calculate total sum of item
                    logging.debug("total")
                    logging.debug(price)
                    logging.debug(additional_charges)
                    logging.debug(float(price)+float(additional_charges))
                    total+= (((price+additional_charges)*(order_item['count'])))
                    logging.debug(total)
                    grandtotal=validated_data['grandtotal']
                    print("GRANDTOTLA")
                    print(grandtotal)

                    #addcharges=int(validated_data['additioncharges'])
                    #print(addcharges)
                    grandTotal = (total)
                    grandTotal=(grandTotal*100)
                    grandtotal=(grandtotal*100)
                    #Calculating and updating  seats update pnly if order is generated

                    # spc=SlotPC.objects.filter(seating_id=pc_slot)
                    # print("BOOKED SEATS")
                    #
                    # booked_seats=spc[0].booked_seats
                    # remaining_seats=spc[0].remaining_seats
                    # print('Booked Seats:{0} Remaining Seats:{1}'.format(booked_seats,remaining_seats))
                    # print("After booking")
                    #
                    # booked_seats=booked_seats+int(order_item['count'])
                    # remaining_seats=remaining_seats-int(order_item['count'])
                    # print('Booked Seats:{0} Remaining Seats:{1}'.format(booked_seats,remaining_seats))
                    # max_size=Price_Category.objects.values_list('max_size', flat=True).get(pk=itemid)
                    #
                    # #varification
                    # print(max_size)
                    # print(booked_seats+remaining_seats)
                    #print(spc[0].seating_id)
                    #print(spc[0].remaining_seats)

                except Exception as error :


                    exc_type, exc_value, exc_traceback = sys.exc_info()

                    traceback_details = {
                        'filename': exc_traceback.tb_frame.f_code.co_filename,
                        'lineno': exc_traceback.tb_lineno,
                        'name': exc_traceback.tb_frame.f_code.co_name,
                        'type': exc_type.__name__,

                    }
                    raise serializers.ValidationError(error)
            print("grand total from frontend" + str(grandtotal))
            print("grand total from backend" + str(grandTotal))
            logging.debug(grandtotal)
            if (grandtotal != grandTotal):
                raise serializers.ValidationError("Mismatch grandtotal" )


            print("ORDER creating")
            print(validated_data)
            orders = Orders.objects.create(**validated_data)
            rcptId=shortuuid.uuid()
            orders.order_no='rcptId'+(rcptId)
            #grandtotal=orders.grandtotal
            #addcharges=orders.additioncharges
            orders.grandtotal=grandTotal
            orders.save()
            for order_item in order_items:
                OrderItems.objects.create(io_id=orders, ** order_item)
            print("SAVE 1")



        #validate Order amount

        except Exception as error:

            exc_type, exc_value, exc_traceback = sys.exc_info() # most recent (if any) by default



            traceback_details = {
                'filename': exc_traceback.tb_frame.f_code.co_filename,
                'lineno'  : exc_traceback.tb_lineno,
                'name'    : exc_traceback.tb_frame.f_code.co_name,
                'type'    : exc_type.__name__,
                'message' : exc_value # or see traceback._some_str()
            }

            raise serializers.ValidationError(str(error))
        print(orders)

        return orders




class EventOrderSerializerGeneric(serializers.ModelSerializer):

    io_id = OrderItemsSerializer(many=True,)
    #payment_status =serializers.CharField(source='get_payment_display')
    payment_status = serializers.SerializerMethodField()
    #payment_method = serializers.CharField(source='Pa.name')
    payment_method = serializers.SlugRelatedField(
        many=False,
        queryset=PaymentMethod.objects.all(),
        slug_field='slug',
        required=False

    )

    #payment_method=serializers.CharField(source='payment.')
    #payment_method = serializers.RelatedField(source='payment_method', read_only=False)
    #payment_method = PaymentMethodSerializer(source="payment_method.name")
    #payment_method=serializers.Payme


    #access_token=serializers.CharField(required=False,read_only=False)
    #saloon_name=SaloonSerializer()



    def get_payment_status(self, obj):
        print(obj.get_payment_status_display)
        return obj.get_payment_status_display()
    #order_status = serializers.CharField(source='get_order_status_display')


    #saloon_name=SaloonsSerializer(required=True)




    class Meta:
        model = Orders

        fields = ('event','slot','cust_name', 'cust_email', 'cust_phone','payment_method','ordercreatedtime','grandtotal','io_id','order_no','payment_status','order_status',"id",'ticket_code','seller','is_order_seller')
        print("test")
        #fields = '__all__'

        # validators = [
        #
        #     UniqueTogetherValidator(
        #         queryset=Orders.objects.all(),
        #         fields=('cust_name', 'cust_email', 'cust_phone',)
        #     )
        # ]


    def create(self, validated_data):

        print((self.context['request'].user))
        print("INSIDE CREATE")
        logging.debug("INSEIDE CREATE")
        print(validated_data)
        user=self.context['request'].user
        print(user)

        order_items = validated_data.pop('io_id')
        print(validated_data)
        #access_token=validated_data.pop('access_token')
        #print(access_token)
        #user = AccessToken.objects.get(token=access_token).user
        #user=self.instance
        print("USER")
        validated_data['user'] = user
        #print(validated_data['id'])

        #validated_data['ticket_code']=(uuid.uuid4().hex[:6].upper())
        validated_data['ticket_code']=(uuid.uuid4().hex[:6].upper())

        print(validated_data['ticket_code'])
        print("PAYMENT_METHOD *************")
        #print(validated_data['payment_method'])
        #print(validated_data)

        #print(order_items)

        flag=0


        total=0.00
        try:

            for order_item in order_items:

                itemid = order_item.pop('item_id')
                print("Itemid")
                print(itemid)

                logging.debug(itemid)
                #pc_slot=order_item.pop('pc_slot').seating_id

                try:
                    if(Price_Category.objects.values_list('title', flat=True).get(pk=itemid)!=order_item['item_name']):
                        logging.debug("Item id and name mismatch for  item")

                        raise serializers.ValidationError("Item id and name mismatch for  item"+str(order_item['item_name'])+" "+str(order_item['item_price']))

                    if (Price_Category.objects.values_list('price', flat=True).get(pk=itemid) != order_item['item_price']):

                        logging.debug("Item expected price and actual price mismatch for item")
                        raise serializers.ValidationError("Item expected price and actual price mismatch for item "+str(order_item['item_name'])+" "+str(order_item['item_price']))
                    #tax=item.objects.values_list('tax', flat=True).get(pk=itemid)

                    price=Price_Category.objects.values_list('price', flat=True).get(pk=itemid)
                    logging.debug(price)
                    additional_charges=Price_Category.objects.values_list('additional_charge', flat=True).get(pk=itemid)
                    #print(tax)
                    print(price)


                    # calculate total sum of item
                    logging.debug("total")
                    logging.debug(price)
                    logging.debug(additional_charges)
                    logging.debug(float(price)+float(additional_charges))
                    total+= (((price+additional_charges)*(order_item['count'])))
                    logging.debug(total)
                    grandtotal=validated_data['grandtotal']
                    print("GRANDTOTLA")
                    print(grandtotal)

                    #addcharges=int(validated_data['additioncharges'])
                    #print(addcharges)
                    grandTotal = (total)
                    grandTotal=(grandTotal*100)
                    grandtotal=(grandtotal*100)
                    #Calculating and updating  seats update pnly if order is generated

                    # spc=SlotPC.objects.filter(seating_id=pc_slot)
                    # print("BOOKED SEATS")
                    #
                    # booked_seats=spc[0].booked_seats
                    # remaining_seats=spc[0].remaining_seats
                    # print('Booked Seats:{0} Remaining Seats:{1}'.format(booked_seats,remaining_seats))
                    # print("After booking")
                    #
                    # booked_seats=booked_seats+int(order_item['count'])
                    # remaining_seats=remaining_seats-int(order_item['count'])
                    # print('Booked Seats:{0} Remaining Seats:{1}'.format(booked_seats,remaining_seats))
                    # max_size=Price_Category.objects.values_list('max_size', flat=True).get(pk=itemid)
                    #
                    # #varification
                    # print(max_size)
                    # print(booked_seats+remaining_seats)
                    #print(spc[0].seating_id)
                    #print(spc[0].remaining_seats)

                except Exception as error :


                    exc_type, exc_value, exc_traceback = sys.exc_info()

                    traceback_details = {
                        'filename': exc_traceback.tb_frame.f_code.co_filename,
                        'lineno': exc_traceback.tb_lineno,
                        'name': exc_traceback.tb_frame.f_code.co_name,
                        'type': exc_type.__name__,

                    }
                    raise serializers.ValidationError(error)
            print("grand total from frontend" + str(grandtotal))
            print("grand total from backend" + str(grandTotal))
            logging.debug(grandtotal)
            if (grandtotal != grandTotal):
                raise serializers.ValidationError("Mismatch grandtotal" )


            print("ORDER creating")
            print(validated_data)
            print("END Validating data")
            print(validated_data)
            orders = Orders.objects.create(**validated_data)
            rcptId=shortuuid.uuid()
            orders.order_no='rcptId'+(rcptId)
            #grandtotal=orders.grandtotal
            #addcharges=orders.additioncharges
            orders.grandtotal=grandTotal
            orders.save()
            print("ORDER")


            for order_item in order_items:
                OrderItems.objects.create(io_id=orders, ** order_item)
            print("SAVE 1")



        #validate Order amount

        except Exception as error:

            exc_type, exc_value, exc_traceback = sys.exc_info() # most recent (if any) by default



            traceback_details = {
                'filename': exc_traceback.tb_frame.f_code.co_filename,
                'lineno'  : exc_traceback.tb_lineno,
                'name'    : exc_traceback.tb_frame.f_code.co_name,
                'type'    : exc_type.__name__,
                'message' : exc_value # or see traceback._some_str()
            }

            raise serializers.ValidationError(str(error))

        return orders



class FacilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Facility
        fields = '__all__'




class OrderSerializer(serializers.ModelSerializer):

    io_id = OrderItemsSerializer(many=True,)
    event=serializers.SerializerMethodField()
    slot=serializers.SerializerMethodField()
    slotend=serializers.SerializerMethodField()
    address_venue=serializers.SerializerMethodField()
    start_time=serializers.SerializerMethodField()
    end_time=serializers.SerializerMethodField()
    thumbnail=serializers.SerializerMethodField()
    medium=serializers.SerializerMethodField()
    host_details=serializers.SerializerMethodField(required=False)
    things_to_know=serializers.SerializerMethodField()

    payment_status = serializers.SerializerMethodField()
    location=serializers.SerializerMethodField()
    payment_method = serializers.SlugRelatedField(
        many=False,
        queryset=PaymentMethod.objects.all(),
        slug_field='slug',
        required=False

    )
    def get_event(self, obj):
        print(obj.event.address_venue)
        return obj.event.title


    def get_slot(self, obj):
        return (obj.slot.start_time)
    def get_slotend(self, obj):
        return (obj.slot.end_time)

    def get_address_venue(self, obj):
        print(obj.event.address_venue)
        return str(obj.event.address_venue)

    def get_location(self, obj):
        print("location")
        print(str(obj.event.address_venue.location.latitude )+ "," + str(obj.event.address_venue.location.longitude))
        print("location end")
        #return str(obj.event.address_venue.location.latitude )+ "," + str(obj.event.address_venue.location.longitude)
        return ({"lat":str(obj.event.address_venue.location.latitude) ,"long" :str(obj.event.address_venue.location.longitude)})


    def get_payment_status(self, obj):
        print(obj.get_payment_status_display)
        return obj.get_payment_status_display()

    def get_start_time(self, obj):
        return obj.slot.start_time.time()
    def get_end_time(self, obj):
        return str(obj.slot.end_time.time())

    def get_host_details(self, obj):
        if(obj.event.organizer):
            return (obj.event.organizer.details)
        else:
            return ("")




        #return str("details")



    def get_things_to_know(self,obj):
        print("things to knoe")
        things_to_know=obj.event.address_venue.facilities.all()
        serializer = FacilitySerializer(instance=things_to_know,many=True,context={'request': self.context.get('request')})
        print("thing to know end")
        return serializer.data


    def get_thumbnail(self,obj):
        request = self.context.get('request')
        print("get_thumbnail")
        thumb=obj.event.image_thumb.url
        print(thumb)
        print("end thumb")
        return (str(request.build_absolute_uri(thumb)))

    def get_medium(self,obj):
        request = self.context.get('request')
        print("get_thumbnail")
        medium=obj.event.image_medium.url
        print(medium)
        print("end thumb")
        return (str(request.build_absolute_uri(medium)))




    class Meta:
        model = Orders
        fields = ('medium','thumbnail','location','event','address_venue','start_time','end_time','things_to_know','slot','slotend','host_details','cust_name', 'cust_email', 'cust_phone','payment_method','ordercreatedtime','grandtotal','io_id','order_no','payment_status','order_status',"id",'ticket_code','ticket_type','seller','is_order_seller')






class EventArtistSerializer(serializers.ModelSerializer):

    artists=ArtistSerializer(many=True,)




    class Meta:
        model = Event
        #fields = '__all__'
        fields=("artists",)

class EventSellerSerializer(serializers.ModelSerializer):

    #event=EventSellerSerializer(many=True,)

    class Meta:
        model = EventSeller
        fields = '__all__'
        #fields=("artists",)



class OrderSimpleSerializer(serializers.ModelSerializer):

    io_id = OrderItemsSerializer(many=True,)
    grandtotal=serializers.SerializerMethodField()

    #thumbnail=serializers.SerializerMethodField()
    #medium=serializers.SerializerMethodField()
    #host_details=serializers.SerializerMethodField(required=False)
    #things_to_know=serializers.SerializerMethodField()

    #payment_status = serializers.SerializerMethodField()
    #location=serializers.SerializerMethodField()

    def get_event(self, obj):
        print(obj.event.address_venue)
        return obj.event.title
    def get_grandtotal(self, obj):

        return (obj.grandtotal/100)


    def get_slot(self, obj):
        return (obj.slot.start_time)
    def get_slotend(self, obj):
        return (obj.slot.end_time)

    def get_address_venue(self, obj):
        print(obj.event.address_venue)
        return str(obj.event.address_venue)

    def get_location(self, obj):
        print("location")
        print(str(obj.event.address_venue.location.latitude )+ "," + str(obj.event.address_venue.location.longitude))
        print("location end")
        #return str(obj.event.address_venue.location.latitude )+ "," + str(obj.event.address_venue.location.longitude)
        return ({"lat":str(obj.event.address_venue.location.latitude) ,"long" :str(obj.event.address_venue.location.longitude)})


    def get_payment_status(self, obj):
        print(obj.get_payment_status_display)
        return obj.get_payment_status_display()

    def get_start_time(self, obj):
        return obj.slot.start_time.time()
    def get_end_time(self, obj):
        return str(obj.slot.end_time.time())

    def get_host_details(self, obj):
        if(obj.event.organizer):
            return (obj.event.organizer.details)
        else:
            return ("")




        #return str("details")



    def get_things_to_know(self,obj):
        print("things to knoe")
        things_to_know=obj.event.address_venue.facilities.all()
        serializer = FacilitySerializer(instance=things_to_know,many=True,context={'request': self.context.get('request')})
        print("thing to know end")
        return serializer.data


    def get_thumbnail(self,obj):
        request = self.context.get('request')
        print("get_thumbnail")
        thumb=obj.event.image_thumb.url
        print(thumb)
        print("end thumb")
        return (str(request.build_absolute_uri(thumb)))

    def get_medium(self,obj):
        request = self.context.get('request')
        print("get_thumbnail")
        medium=obj.event.image_medium.url
        print(medium)
        print("end thumb")
        return (str(request.build_absolute_uri(medium)))




    class Meta:
        model = Orders
        fields = ('io_id','grandtotal')
        #fields = '__all__'



class EventSimpleSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)


    #category = EventCategorySerializer(many=False,)
    #medias=serializers.SerializerMethodField(source='upload')
    #medias=serializers.SerializerMethodField(source='image_original')
    #photo_original1=serializers.FileField(source='photo_original')
    #categoryImage=CategoryImageSerializer(many=True,)
    #gallary = categoryImage(source='get_absolute_url')
    #gallery=categoryImage

    #slots=SlotSerializer(many=True,)
    #slotpc=serializers.SerializerMethodField()
    #pricing_category=Price_CategorySerializer(many=True)
    #city=CitySerializer(many=False)
    #ticket_type = serializers.SerializerMethodField()
    #button_text=ButtonTextSerializer(many=False,)
    #external_url=serializers.SerializerMethodField()
    #booking= serializers.SerializerMethodField()
    #artists=ArtistSerializer(many=True,)

    address_venue=serializers.SerializerMethodField()
    start_time=serializers.SerializerMethodField()
    end_time=serializers.SerializerMethodField()








    class Meta:
        model = Event
        #fields = '__all__'
        fields = ( 'id','title','short_title', 'start_time', 'end_time','address_venue',)



    def get_address_venue(self, obj):
        print(obj.address_venue)
        return str(obj.address_venue)

    def get_start_time(self, obj):
        return obj.start_time
    def get_end_time(self, obj):
        return (obj.end_time)

    def get_ticket_type(self,obj):
        return obj.get_ticket_type_display()

    def get_external_url(self,obj):
        return obj.external_url
    def get_booking(self,obj):
        booking={

            "type": str(obj.get_booking_type_display()),
            "button_text":str(obj.button_text),
            "external_url": str(obj.external_url),
        }
        return (booking)



    def get_medias(self,obj):
        request = self.context.get('request')
        print("Reached")
        thumb=obj.image_thumb
        medium=obj.image_medium
        original=obj.image_original
        thumb_url=None
        medium_url=None
        original_url=None

        if(thumb):
            thumb_url=obj.image_thumb.url
        if(medium):
            medium_url=obj.image_medium.url
        if(original):
            original_url=obj.image_original.url



        medias={

            "thumbnail":thumb_url,
            "medium":medium_url,
            "large":original_url,
        }
        return (medias)

class OrderUserSerializer(serializers.ModelSerializer):

    #order=OrderSimpleSerializer(many=True,)
    #orders=serializers.SerializerMethodField()
    io_id=OrderItemsUserSerializer(many=True)
    user=serializers.SerializerMethodField()

    class Meta:
        model = Orders
        #fields = '__all__'
        fields=('io_id','attended',"cust_name","cust_email","cust_phone","ticket_type","user",'is_order_seller','scan_time','ticket_code')
    def get_user(self,obj):
        print(obj.user)
        if(obj.user is not None):
            return obj.user.username
        else:
            return obj.user



class SlotSerializer(serializers.ModelSerializer):
    total_booking=serializers.SerializerMethodField()
    attendee_list=serializers.SerializerMethodField()
    class Meta:
        model = Slot
        #fields = '__all__'
        fields=("title","start_time","end_time","total_booking","attendee_list")

    def get_total_booking(self,obj):
        print("SLOT *****")
        print( self.context.get('event_id'))
        print(obj.id)
        #count=Orders.objects.filter(event__id=self.context.get('event_id') ).count()
        count = Orders.objects.filter(Q(event__id=self.context.get('event_id')) & Q(slot=obj.id) & (Q(payment_status='FE')|Q(payment_status='PC'))).count()
        print(count)
        return count

    def get_attendee_list(self,obj):
        print("get_attendee_list")
        print( self.context.get('event_id'))
        print(obj.id)
        #count=Orders.objects.filter(event__id=self.context.get('event_id') ).count()
        orders = Orders.objects.filter(Q(event__id=self.context.get('event_id')) & Q(slot=obj.id) & (Q(payment_status='FE')|Q(payment_status='PC')))
        print(orders)

        serializer = OrderUserSerializer(instance=orders,many=True)
        print("thing to know end")
        return serializer.data




class HostEventSerializer(serializers.ModelSerializer):

    #slots=SlotSerializer(many=True,context={'id':1})
    total_booking=serializers.SerializerMethodField()
    slots=serializers.SerializerMethodField()
    #summary=serializers.SerializerMethodField()

    def get_slots(self,obj):
        slots=obj.slots.all()
        serializer = SlotSerializer(instance=slots,many=True,context={'event_id': obj.id})
        print("thing to know end")
        return serializer.data





#event=EventSellerSerializer(many=True,)

    class Meta:
        model = Event
        fields = ('title','short_title','slug','image_original','slots','total_booking')

    def get_total_booking(self,obj):
        count=Orders.objects.filter(Q(event__id=obj.id ) & (Q(payment_status='FE')|Q(payment_status='PC'))).count()
        print(count)
        return count



    def get_summary(self,obj):
        print("things to knoe")
        print(obj.id)
        orders=Orders.objects.filter(event__id=obj.id)
        print(orders)


        list=[]
        cat=[]
        mainlist=[]
        total=0
        subtotal=0
        earnings=0
        summary={}
        totalticket=0
        result={}


        cnt=1
        for i in orders:
            #pc_cat=
            print(i)

            queryset=OrderItems.objects.filter(io_id=i)


            for i in queryset:
                cat.append(({i.item_name:i.count,"itemprice"+str(cnt):i.item_price}))
                cnt+=1
                list.append({i.item_name:i.count})
                totalticket=totalticket+i.count
                mainlist.append(cat)
                #cat.add({i.item_name:i.count,"item price":i.item_price})

                #if(i.item_name):
                print(i.pc_cat)

                print(i.item_name)
                print(i.count)
                print(i.item_price)
            #mainlist.append((list))
            print("LIST")

            print(list)
            print("CAT")
            print(cat)
            # sum the values with same keys
            counter = collections.Counter()
            for d in list:
                counter.update(d)

            result = dict(counter)
            print("RESULT")

            print(result)
        mainlist=[]
        for i in orders:
            queryset=OrderItems.objects.filter(io_id=i)
            for j in queryset:
                print(j.item_name)
                if j.item_name in result:
                    print(j.item_price)
                    mainlist.append({j.item_name:result[j.item_name],"itemprice":j.item_price*result[j.item_name]})
                    result.pop(j.item_name)

                    #subtotal+=(i.item_price*result[i.item_name])
                    #earnings=((subtotal*commission)/100)

        print("MAINLIST")
        print(mainlist)


        for i in mainlist:

            print(total)
            print("itemprice")
            print(i['itemprice'])
            total=total+(i['itemprice'])

            print("total")





        summary={"order":mainlist,"earnings":earnings,"subtotal":total,"total_ticketssold":totalticket}




        #print(mainlist)
        #serializer = EventSellerSerializer(instance=event,many=True,context={'request': self.context.get('request')})
        print("thing to know end")
        #return serializer.data
        return  summary



class EventHostSerializer(serializers.ModelSerializer):

    #order=OrderSimpleSerializer(many=True,)
    #orders=serializers.SerializerMethodField()
    event=HostEventSerializer(many=True)

    class Meta:
        model = Host
        #fields = '__all__'
        fields=("event",)




class EventSellerSerializer(serializers.ModelSerializer):

    #order=OrderSimpleSerializer(many=True,)
    order=serializers.SerializerMethodField()
    eventdetail=EventSimpleSerializer(many=False)

    class Meta:
        model = EventSeller
        #fields = '__all__'
        fields=("eventdetail","order")
    def get_order(self,obj):
        print("things to knoe")
        order=obj.order.all()
        print(order)


        list=[]
        cat=[]
        mainlist=[]
        total=0
        subtotal=0
        earnings=0
        summary={}
        totalticket=0
        result={}
        commission=obj.commission
        print("COMMISSION")
        print(commission)

        cnt=1
        for i in order:
            #pc_cat=
            print(i)

            queryset=OrderItems.objects.filter(io_id=i)


            for i in queryset:
                cat.append(({i.item_name:i.count,"itemprice"+str(cnt):i.item_price}))
                cnt+=1
                list.append({i.item_name:i.count})
                totalticket=totalticket+i.count
                mainlist.append(cat)
                #cat.add({i.item_name:i.count,"item price":i.item_price})

                #if(i.item_name):
                print(i.pc_cat)

                print(i.item_name)
                print(i.count)
                print(i.item_price)
            #mainlist.append((list))
            print("LIST")

            print(list)
            print("CAT")
            print(cat)
            # sum the values with same keys
            counter = collections.Counter()
            for d in list:
                counter.update(d)

            result = dict(counter)
            print("RESULT")

            print(result)
        mainlist=[]
        for i in order:
            queryset=OrderItems.objects.filter(io_id=i)
            for j in queryset:
                print(j.item_name)
                if j.item_name in result:
                    print(j.item_price)
                    mainlist.append({j.item_name:result[j.item_name],"itemprice":j.item_price*result[j.item_name]})
                    result.pop(j.item_name)

                    #subtotal+=(i.item_price*result[i.item_name])
                    #earnings=((subtotal*commission)/100)

        print("MAINLIST")
        print(mainlist)


        for i in mainlist:

            print(total)
            print("itemprice")
            print(i['itemprice'])
            total=total+(i['itemprice'])
            earnings=((total*commission)/100)
            print("total")





        summary={"order":mainlist,"earnings":earnings,"subtotal":total,"commission":commission,"total_ticketssold":totalticket}




        #print(mainlist)
        #serializer = EventSellerSerializer(instance=event,many=True,context={'request': self.context.get('request')})
        print("thing to know end")
        #return serializer.data
        return  summary



class SellerSerializer(serializers.ModelSerializer):

    event=EventSellerSerializer(many=True,)
    #event=serializers.SerializerMethodField()


    class Meta:
        model = Seller
        fields = ('event',)
        #fields=("artists",)
    def get_event(self,obj):
        print("things to knoe")
        event=obj.event.all()
        serializer = EventSellerSerializer(instance=event,many=True,context={'request': self.context.get('request')})
        print("thing to know end")
        return serializer.data


class BookPageSerializer(serializers.Serializer):
    status = serializers.SerializerMethodField('_is_my_find')

    def _is_my_find(self, obj):
        status = self.context.get("status")
        print(status)

        if status:
            print(status)
            return status
        return False

    bookinginfo = OrderSerializer(many=True)
    print("END ORDER")
    relatedartist=EventArtistSerializer(many=True)
