
from rest_framework import serializers, pagination, request
from django.db.models import Q

import shortuuid
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
from collabo_events.models import EventSeller, Seller, Country, Event, EventCategory, ButtonText, CategoryImage, Slot, \
    Price_Category, City, SlotPC, Artist, ArtistImage, ArtistSong, State, Type, VImage, Venue1, HomeFeatureArtist, \
    HomeFeatureVenue, HomeFeatureEvent, HomeBanner, ArtistGenre, PaymentMethod, CustomText, Choice
import sys,traceback

from events_api.models import Customer

sys.path.append("..")



class ButtonTextSerializer(serializers.ModelSerializer):
    class Meta:
        model = ButtonText
        fields = '__all__'
class CountrySerializer(serializers.ModelSerializer):


    class Meta:
        model = Country
        fields = '__all__'


class StateSerializer(serializers.ModelSerializer):
    country=CountrySerializer()

    class Meta:
        model = State
        fields = '__all__'


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentMethod
        fields = '__all__'


class CitySerializer(serializers.ModelSerializer):
    state=StateSerializer()
    #payment_method=PaymentSerializer(many=True)
    class Meta:
        model = City
        fields = '__all__'



class EventCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = EventCategory
        fields = '__all__'
        ordering = ['weight']


class CategoryImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryImage
        fields = '__all__'

class PriceCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Price_Category
        fields = '__all__'


class SlotPCSerializer(serializers.ModelSerializer):
    price_cat=PriceCategorySerializer()
    class Meta:
        model = SlotPC
        fields = '__all__'

class SlotPCSerializerNew(serializers.ModelSerializer):
    price_cat=PriceCategorySerializer()
    class Meta:
        model = SlotPC
        fields = '__all__'


class SlotSerializer(serializers.ModelSerializer):
    #slotpc_set=SlotPCSerializer(many=True)
    slotpc_set=serializers.SerializerMethodField()

    start_time=serializers.SerializerMethodField()
    end_time=serializers.SerializerMethodField()




    def get_start_time(self, obj):
        return obj.start_time
    def get_end_time(self, obj):
        return (obj.end_time)

    def get_slotpc_set(self,obj):
        print("inside*****")
        print(obj.id)
        slug = self.context.get('slug')
        print(slug)


        qs= ((SlotPC.objects.filter(event__slug=slug,slot=obj)))
        serializer = SlotPCSerializerNew(instance=qs,many=True)


        return serializer.data


    # print(qs)
        # list=[]
        # for item in qs:
        #     slotpc={
        #
        #         "seating_id": str(item.seating_id),
        #         "event":str(item.event),
        #         "slot":str(item.slot),
        #         "pricing_category":str(item.price_cat),
        #         "max_size":item.totalSlot or None,
        #         "remaining_seats":item.remaining_seats,
        #
        #
        #     }
        #     list.append(slotpc)
        # print(list)
        # return (list)

    class Meta:
        model = Slot
        fields = ('start_time','end_time','max_size','slotpc_set','id')






class Price_CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Price_Category
        fields = '__all__'

class CitySerializer(serializers.ModelSerializer):
    payment_method=PaymentSerializer(many=True)
    #state=StateSerializer()

    class Meta:
        model=City
        fields=('name','short_name','slug','payment_method')


class ArtistSongSerializer(serializers.ModelSerializer):

    class Meta:
        model=ArtistSong
        fields='__all__'

class ArtistImageSerializer(serializers.ModelSerializer):

    class Meta:
        model=ArtistImage
        fields='__all__'


class ArtistSerializer(serializers.ModelSerializer):
    artistImage=ArtistImageSerializer(many=True)
    artistSong=ArtistSongSerializer(many=True)
    city=CitySerializer()
    is_user_follow = serializers.SerializerMethodField('_user')



    def _user(self, obj):
        print("Current user")
        current_artist = obj.title
        request = self.context.get('request')



        #print(request.user)

        #request = getattr(self.context, 'request', None)
        print(request.user)
        status=False
        try:

            if(not request.user.is_anonymous ):
                print("LIST")
                follow_list=[]
                query=request.user.customer.follow_artist.get_queryset()
                for i in query:
                    follow_list.append(i.title)

                if(current_artist in follow_list):
                    status=True
                else:
                    status=False
            print(status)
            return (status)
        except Exception as e:
            return (status)





    #is_follow=serializers.SerializerMethodField()


    class Meta:
        model=Artist
        fields='__all__'

    def get_is_follow(selfself,obj):
        status=True
        return (status)






class ArtistSimpleSerializer(serializers.ModelSerializer):
    #artistImage=ArtistImageSerializer(many=True)
    #artistSong=ArtistSongSerializer(many=True)
    #city=CitySerializer()

    class Meta:
        model=Artist
        fields=('title','thumbnail','fb_followers','inst_followers','rate','slug','id')




class TypeSerializer(serializers.ModelSerializer):

    class Meta:
        model=Type
        fields='__all__'
class VImageSerializer(serializers.ModelSerializer):

    class Meta:
        model=VImage
        fields='__all__'
        #fields=("image_name","upload")




class Venue1Serializer(serializers.ModelSerializer):
    location=serializers.SerializerMethodField(source='location')
    type=TypeSerializer(many=False)
    upload=VImageSerializer(many=True)
    city=CitySerializer()

    class Meta:
        model=Venue1
        fields=('title','label','capacity','rate','rate_type','about','type','upload','location','slug','city')
    def get_location(self,obj):
        cont={'place': obj.location.place,
              'latitude':obj.location.latitude,
              'longitude':obj.location.longitude}
        return cont



class Venue1SimpleSerializer(serializers.ModelSerializer):
    location=serializers.SerializerMethodField(source='location')
    #type=TypeSerializer(many=False)
    upload=VImageSerializer(many=True)

    #city=CitySerializer()

    class Meta:
        model=Venue1
        fields=('title','label','capacity','rate','rate_type','upload','location','slug')
    def get_location(self,obj):
        cont={'place': obj.location.place,
              'latitude':obj.location.latitude,
              'longitude':obj.location.longitude}
        return cont


class ChoiceSerializer(serializers.ModelSerializer):


    class Meta:
        model=Choice
        fields=('choice_text',)


class CustomTextSerializer(serializers.ModelSerializer):
    choice=ChoiceSerializer(many=True)


    class Meta:
        model=CustomText
        fields=('select_text','choice')


class EventSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)


    category = EventCategorySerializer(many=False,)
    #medias=serializers.SerializerMethodField(source='upload')
    medias=serializers.SerializerMethodField(source='image_original')
    #photo_original1=serializers.FileField(source='photo_original')
    categoryImage=CategoryImageSerializer(many=True,)
    #gallary = categoryImage(source='get_absolute_url')
    gallery=categoryImage

    #slots=SlotSerializer(many=True,)
    slots=serializers.SerializerMethodField()
    #slotpc=serializers.SerializerMethodField()
    #pricing_category=Price_CategorySerializer(many=True)
    city=CitySerializer(many=False)
    ticket_type = serializers.SerializerMethodField()
    #button_text=ButtonTextSerializer(many=False,)
    #external_url=serializers.SerializerMethodField()
    booking= serializers.SerializerMethodField()
    artists=ArtistSerializer(many=True,)
    address_venue=Venue1Serializer(many=False)
    start_time=serializers.SerializerMethodField()
    end_time=serializers.SerializerMethodField()
    custom_field=CustomTextSerializer(many=True,)
    #custom_field=serializers.SerializerMethodField()

    def get_slots(self,obj):
        today = datetime.datetime.today()
        print(today)
        print("OBJ")
        print(obj.slots)

        qs = obj.slots.filter(Q(end_time__gte =today))
        print(qs)


        serializer = SlotSerializer(instance=qs,many=True,context={'slug': self.context.get('slug')})


        return serializer.data









    class Meta:
            model = Event
            #fields = '__all__'
            fields = ( 'id','title','short_title', 'slug','ticket_type', 'description','itinerary','cancellation_policy','start_time', 'end_time', 'city','booking','category','categoryImage','gallery','medias','slots','address_venue','artists','lowest_price','custom_field')




    def get_custom_field(self, obj):
        print("INSIDE SER")
        #print(obj)
        cust = obj.custom_field.all() # get 10 similar stores for this store
        print(cust)
        #quest=shuffle(quest)
        return CustomTextSerializer(cust, many=True).data




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



class EventSerializerWeb(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    category = EventCategorySerializer(many=False,)
    city=CitySerializer(many=False)
    ticket_type = serializers.SerializerMethodField()
    booking= serializers.SerializerMethodField()
    address_venue=Venue1Serializer(many=False)
    start_time=serializers.SerializerMethodField()
    end_time=serializers.SerializerMethodField()





    class Meta:
        model = Event
        #fields = '__all__'
        fields = ( 'id','title','short_title', 'slug','ticket_type','start_time', 'end_time', 'city','booking','category','address_venue','lowest_price')
        ordering = ['-category']


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
        #thumpnail = obj.photo_original.url
        original = obj.get_original()
        medium=obj.get_medium()
        thumb=obj.get_thumb()
        medias={

            "thumbnail": str(request.build_absolute_uri(thumb)),
            "medium":str(request.build_absolute_uri(medium)),
            "large": str(request.build_absolute_uri(original)),
        }
        return (medias)




import datetime



class EventSimpleSerializerWeb(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    category = EventCategorySerializer(many=False,)
    city=CitySerializer(many=False)
    #ticket_type = serializers.SerializerMethodField()
    booking= serializers.SerializerMethodField()
    #address_venue=Venue1Serializer(many=False)
    address_venue=Venue1SimpleSerializer(many=False,)
    medias=serializers.SerializerMethodField(source='image_original')
    start_time=serializers.SerializerMethodField()
    end_time=serializers.SerializerMethodField()







    class Meta:


        #model = Event.objects.filter(Q(end_time__gte=today))
        model=Event
        #fields = '__all__'
        fields = ( 'id','title','short_title','category','booking', 'slug','start_time','end_time', 'address_venue','lowest_price','city','medias')
        ordering = ['-category']



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


    # def get_medias(self,obj):
    #     request = self.context.get('request')
    #
    #     medias={
    #
    #         "thumbnail":obj.image_thumb.url,
    #
    #     }
    #     return (medias)

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









class BannerSerializer(serializers.ModelSerializer):
    #image = serializers.SerializerMethodField('get_image1')

    class Meta:
        model = HomeBanner
        fields = ("image", "title", "event")

    def get_image1(self, obj):
        request = self.context.get('request')
        print("request")
        request="http://localhost:8000/"
        print(obj.image)

        return request.build_absolute_uri(obj.image)



class FeaturesArtistSerializer(serializers.ModelSerializer):
    #artist = ArtistSerializer(many=True)
    artist = ArtistSimpleSerializer(many=True)

    class Meta:
        model = HomeFeatureArtist
        fields = ('name','slug','id','city','artist')




class FeaturesVenueSerializer(serializers.ModelSerializer):
    #venue = Venue1Serializer(many=True)
    venue = Venue1SimpleSerializer(many=True)

    class Meta:
        model = HomeFeatureVenue
        fields = ('name','slug','id','city','venue')

class FeaturesEventSerializer(serializers.ModelSerializer):
    #event = EventSimpleSerializerWeb(many=True)
    event=serializers.SerializerMethodField('get_events')








    def get_events(self,obj):
        today = datetime.datetime.today()
        print(today)
        print("OBJ")
        print(obj.event)

        qs = obj.event.filter(Q(end_time__gte =today)&Q(city__slug=self.context['city']))


        serializer = EventSimpleSerializerWeb(instance=qs,many=True,context={'request': self.context.get('request')})


        return serializer.data

    class Meta:
        model = HomeFeatureEvent
        #model=HomeFeatureEvent.objects.filter(Q(event__city__slug=slug)).filter(Q(event__end_time__gte =today)).distinct,
        fields = ('name','slug','id','city','event')
from django.db.models import Count

class EventCountSerializer(serializers.ModelSerializer):
    category=serializers.SerializerMethodField(source='EventCategory')
    class Meta:
        model = EventCategory
        fields = ("category",)



    def get_category(self,obj):
        print(obj.name)
        city = self.context["city"]
        today=self.context['today']

        qs=Event.objects.filter(category=obj.category_id,city__slug=city,end_time__gte =today).count()

        tuple={"count":qs,"name":obj.name,"id":obj.category_id}
        print(tuple)
        return tuple
        #if(not qs):

        #return {}


    def get_count_assigned(self, obj):
        return {"category":obj.category}
        #category=str({"category":str(obj.category)})

        #category={"category":obj.category,
        #         "count":obj.category.count()}
        #print(obj.category)


class EventTypeCountSerializer(serializers.ModelSerializer):
    type=serializers.SerializerMethodField(source='Type',)
    #all=serializers.SerializerMethodField(source="Type")
    flag=0


    class Meta:
        model = Type
        fields = ("type",)

    def get_all(self,obj):
        print("TITLE")
        print(obj.pk)
        print(self.context.get("city"))
        qs=Venue1.objects.filter(city__slug=self.context.get("city")).count()
        print("COUNT")
        print(qs)
        #dict={}




        if(self.flag==0):
            tuple={"type":{"count":qs,"name":"all"}}
            self.flag=1
            return tuple



        #dict=({"count":all,"name":"all",})
        return None




    def get_type(self,obj):
        print("TITLE")
        print(obj.pk)
        print(self.context.get("city"))

        #dict={}


        qs=Venue1.objects.filter(type=obj.pk,city__slug=self.context.get("city")).count()
        tuple={"count":qs,"name":obj.title,"id":obj.id}

        return tuple


    def get_count_assigned(self, obj):
        return {"category":obj.title}




class VenueTypeCountSerializer(serializers.ModelSerializer):
    type=serializers.SerializerMethodField(source='Type',)
    #all=serializers.SerializerMethodField(source="Type")
    flag=0


    class Meta:
        model = Type
        fields = ("type",)

    def get_all(self,obj):
        print("TITLE")
        print(obj.pk)
        print(self.context.get("city"))
        qs=Venue1.objects.filter(city__slug=self.context.get("city")).count()
        print("COUNT")
        print(qs)
        #dict={}




        if(self.flag==0):
            tuple={"type":{"count":qs,"name":"all"}}
            self.flag=1
            return tuple



        #dict=({"count":all,"name":"all",})
        return None




    def get_type(self,obj):
        print("TITLE")
        print(obj.pk)
        print(self.context.get("city"))

        #dict={}


        qs=Venue1.objects.filter(type=obj.pk,city__slug=self.context.get("city")).count()
        tuple={"count":qs,"name":obj.title,"id":obj.id}

        return tuple


    def get_count_assigned(self, obj):
        return {"category":obj.title}




class ArtistTypeCountSerializer(serializers.ModelSerializer):
    genre=serializers.SerializerMethodField(source='Type')
    class Meta:
        model = ArtistGenre
        fields = ("genre",)



    def get_genre(self,obj):
        print("TITLE")
        print(obj.pk)
        qs=Artist.objects.filter(genre=obj.pk).count()
        tuple={"count":qs,"name":obj.title,"id":obj.id}
        return tuple

    def get_count_assigned(self, obj):
        return {"category":obj.title}




class BannerFeatureSerializer(serializers.Serializer):
    status = serializers.SerializerMethodField('_is_my_find')
    #city=serializers.SerializerMethodField('_is_my_find')

    def _is_my_find(self, obj):

        status = self.context.get("status")
        print("***********")
        print(status)


        if status:

            print(status)
            return status
        return False


    banner = BannerSerializer(many=True)
    category=EventCountSerializer(many=True)
    featureartist = FeaturesArtistSerializer(many=True)
    featureevent = FeaturesEventSerializer(many=True)
    featurevenue = FeaturesVenueSerializer(many=True)




class ArtistEventSerializer(serializers.Serializer):
    status = serializers.SerializerMethodField('_is_my_find')

    def _is_my_find(self, obj):
        status = self.context.get("status")
        print(status)

        if status:
            print(status)
            return status
        return False

    upcomingEvents = EventSimpleSerializerWeb(many=True)
    pastEvents=EventSimpleSerializerWeb(many=True)
    artist = ArtistSerializer(many=True)




class VenueEventSerializer(serializers.Serializer):
    status = serializers.SerializerMethodField('_is_my_find')

    def _is_my_find(self, obj):
        status = self.context.get("status")
        print(status)

        if status:
            print(status)
            return status
        return False

    upcomingEvents = EventSimpleSerializerWeb(many=True)
    pastEvents=EventSimpleSerializerWeb(many=True)
    venue = Venue1Serializer(many=True)


class EventDetailSerializer(serializers.Serializer):
     event=EventSerializer(many=True,)



class EventsListWebSerializer(serializers.Serializer):
    status = serializers.SerializerMethodField('_is_my_find')

    def _is_my_find(self, obj):
        status = self.context.get("status")
        print(status)

        if status:
            print(status)
            return status
        return False


    banner = BannerSerializer(many=True)
    category=EventCountSerializer(many=True)
    #category=VenueTypeCountSerializer(many=True)
    eventlist = EventSerializerWeb(many=True)



class VenueListWebSerializer(serializers.Serializer):
    status = serializers.SerializerMethodField('_is_my_find')

    def _is_my_find(self, obj):
        status = self.context.get("status")
        print(status)

        if status:
            print(status)
            return status
        return False


    banner = BannerSerializer(many=True)
    category=VenueTypeCountSerializer(many=True)
    #category=VenueTypeCountSerializer(many=True)
    venuelist = Venue1Serializer(many=True)




class ArtistListWebSerializer(serializers.Serializer):
    status = serializers.SerializerMethodField('_is_my_find')

    def _is_my_find(self, obj):
        status = self.context.get("status")
        print(status)

        if status:
            print(status)
            return status
        return False


    banner = BannerSerializer(many=True)
    category=ArtistTypeCountSerializer(many=True)
    artistlist = ArtistSerializer(many=True)



class EventSellerSerializer(serializers.ModelSerializer):
    eventdetail=EventSerializer()



    class Meta:
        model = EventSeller
        fields='__all__'



class SellerSerializer(serializers.ModelSerializer):



    event=EventSellerSerializer(many=True)

    #event=serializers.SerializerMethodField('get_events')








    def get_event(self,obj):

        today = datetime.datetime.today()
        print(today)
        print("OBJ")
        print(obj.event)

        qs = obj.event.filter(Q(event__end_time__gte =today)&Q(event__city__slug=self.context['city']))


        serializer = EventSellerSerializer(instance=qs,many=True,context={'request': self.context.get('request')})


        return serializer.data



    class Meta:
        model = Seller
        fields='__all__'


class SellerSerializerDet(serializers.Serializer):
    status = serializers.SerializerMethodField('_is_my_find')

    def _is_my_find(self, obj):
        status = self.context.get("status")
        print(status)

        if status:
            print(status)
            return status
        return False


    seller = SellerSerializer(many=True)
