import random
import math, random

import pytz
from django.db.models import Q
from django.http import HttpResponse
from rest_framework import status, generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.exceptions import APIException
from rest_framework.generics import get_object_or_404
from drf_accountkit.views import LoginSuccess
from oauth2_provider.models import AccessToken
from rest_framework.response import Response
from django.conf import settings
#from django.shortcuts import redirect, get_object_or_404
from rest_framework import exceptions

import bottle
from threading import Thread
import json
import requests
import re

from collabo_events.api_views import LargeResultsSetPagination, testResultsSetPagination
from .sendSMS import SendMessage

from django.shortcuts import render
from qr_code.qrcode.utils import QRCodeOptions

import datetime as dtime
from datetime import datetime as DateTime, timedelta as TimeDelta
from datetime import datetime
from django.views.decorators.csrf import csrf_exempt
from .serializers import EventOrderSerializer, BookPageSerializer, EventOrderSerializerGeneric, SellerSerializer, \
    EventSellerSerializer, EventHostSerializer, HostEventSerializer
from collabo_events.models import Event, User, PaymentMethod, EventSeller
from events_api.models import Customer
from .viewsPayment.createorders import createRazorpayOrder,FetchRazorPayment,CapturePaymnet
from rest_framework.views import APIView
from .viewsPayment.RAZORAPISECRETS import RAZORPAY_API_SECRET,RAZORPAY_API_KEY
from .viewsPayment.payfort_utility import get_signature,payfort_operation
import razorpay
from django.core import serializers
from .mails import WelcomeMail

from rest_framework.permissions import IsAuthenticated,AllowAny
import sys
sys.path.append("..")
from .models import Orders,OrderItems,Slot,SlotPC,Price_Category,Seller,Host
from datetime import date
from django.shortcuts import render
from qr_code.qrcode.utils import ContactDetail, WifiConfig, Coordinates, QRCodeOptions
from django.conf import settings
from django.core import mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.core.exceptions import ValidationError
from rest_framework import viewsets
from collections import namedtuple
from django.contrib.auth import authenticate, login
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK
)
from rest_framework.response import Response


BookPage = namedtuple('BookPage',('bookinginfo','relatedartist','context'))


from django.core.mail import EmailMessage


"""Send an email message from the user's account.
"""
import logging
import os
filename = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'ram.log')
logging.basicConfig(
    filename=filename,
    level=logging.DEBUG,
    format='%(asctime)s.%(msecs)03d %(levelname)s %(module)s - %(funcName)s: %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
)


import base64
from email.mime.audio import MIMEAudio
from email.mime.base import MIMEBase
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import mimetypes
import os

from email.mime.multipart import MIMEMultipart

from email.mime.text import MIMEText
from email.mime.image import MIMEImage

from pathlib import Path
from email.mime.image import MIMEImage
from django.core.mail import EmailMultiAlternatives


#
# import logging
# from aws_logging_handlers.S3 import S3Handler
# from aws_logging_handlers.Kinesis import KinesisHandler
#
# bucket=settings.AWS_STORAGE_BUCKET_NAME # The bucket should already exist
#
# # The log will be rotated to a new object either when an object reaches 5 MB or when 120 seconds pass from the last rotation/initial logging
# s3_handler = S3Handler("test_log", bucket)
# kinesis_handler = KinesisHandler('log_test', 'us-east-1', workers=1)
# formatter = logging.Formatter('[%(asctime)s] %(filename)s:%(lineno)d} %(levelname)s - %(message)s')
# s3_handler.setFormatter(formatter)
# kinesis_handler.setFormatter(formatter)
# logger = logging.getLogger('root')
# logger.setLevel(logging.INFO)
# logger.addHandler(s3_handler)
# logger.addHandler(kinesis_handler)

# for i in range(0, 100000):
#     logger.info("test info message")
#     logger.warning("test warning message")
#     logger.error("test error message")
#
# logging.shutdown()


class MobileLogin(LoginSuccess):


    def post(self, request, *args, **kwargs):

        response = super(MobileLogin, self).post(request, *args, **kwargs)
        print(response.status_code)
        print("PHONE**************")
        print(response.data)
        print(status.is_success(response.status_code))
        print("MY TOKEN")

        if(status.is_success(response.status_code)):

            user = User.objects.get(id=response.data['user_id'])

            print("REached")
            user.is_customer=True
            user.save()
            print("--models")

            if (not user.customer.is_previously_logged_in):
                user.customer.is_previously_logged_in=True
                user.customer.country_prefix=response.data['identity_response']['phone']['country_prefix']
                user.customer.phone=response.data['identity_response']['phone']['number']
                #user.customer.
                date_1 = DateTime.today()
                end_date = date_1
                user.customer.exptime=end_date
                print(end_date)
                print(user.customer.exptime)

                user.save()

        return response

class MobileLogin(LoginSuccess):


    def post(self, request, *args, **kwargs):

        response = super(MobileLogin, self).post(request, *args, **kwargs)
        print(response.status_code)
        print("PHONE**************")
        print(response.data)
        print(status.is_success(response.status_code))
        print("MY TOKEN")

        if(status.is_success(response.status_code)):

            user = User.objects.get(id=response.data['user_id'])

            print("REached")
            user.is_customer=True
            user.save()
            print("--models")

            if (not user.customer.is_previously_logged_in):
                user.customer.is_previously_logged_in=True
                user.customer.country_prefix=response.data['identity_response']['phone']['country_prefix']
                user.customer.phone=response.data['identity_response']['phone']['number']
                #user.customer.
                date_1 = DateTime.today()
                end_date = date_1
                user.customer.exptime=end_date
                print(end_date)
                print(user.customer.exptime)

                user.save()

        return response





class MyTokenView(LoginSuccess):


    def post(self, request, *args, **kwargs):
        #request.POST._mutable = True
        #print(request.auth.application)

        #SAINA_APPLICATION_CLIENT_ID = getattr(settings, "SAINA_APPLICATION_CLIENT_ID", None)
        #print(SAINA_APPLICATION_CLIENT_ID)

        #request.POST['client_id']=SAINA_APPLICATION_CLIENT_ID
        response = super(MyTokenView, self).post(request, *args, **kwargs)
        print(response.status_code)
        print("PHONE**************")
        print(response.data)
        print(status.is_success(response.status_code))
        print("MY TOKEN")
        #response.data.update({"status":response.data['error_description']})
        # check for status
        #{'token': 'fb132f85660ca5257f001f696bedf6eb03f38ca0', 'user_id': 12}

        if(status.is_success(response.status_code)):

            user = User.objects.get(id=response.data['user_id'])
            print(user)

            #{'id': '2275504256022832', 'phone': {'number': '+919947267251', 'country_prefix': '91', 'national_number': '9947267251'}, 'application': {'id': '333260200721985'}}



            #user=response.data['user_id'].user
            print(user)





            print("REached")

            #print(user.customer.is_previously_logged_in)

            user.is_customer=True
            user.save()
            print("--models")

            if (not user.customer.is_previously_logged_in):



                user.customer.is_previously_logged_in=True
                user.customer.country_prefix=response.data['identity_response']['phone']['country_prefix']
                user.customer.phone=response.data['identity_response']['phone']['number']
                #user.customer.
                date_1 = DateTime.today()
                end_date = date_1
                user.customer.exptime=end_date
                print(end_date)
                print(user.customer.exptime)
                #user.customer.email_address=user.email
                #user.customer.user_plan='N'
                #user.customer.user_type='N'

                user.save()

        return response




class GenerateOrderGeneric(generics.CreateAPIView):
    """
    Create an order from server
    """
    serializer_class = EventOrderSerializerGeneric

    permission_classes = (AllowAny,)

    def create(self, request, *args, **kwargs):
        self.serializer_class = EventOrderSerializerGeneric
        print(request)
        print("**************")
        print(request.data['event'])
        #
        # user=(Event.objects.filter(event_id=request.data['event_id']).values('owner','name'))
        # print(user[0]['owner'])
        # print(user[0]['name'])
        # print(User.objects.filter(id=user[0]['owner']).values("email"))
        print("*************")
        print("REQUEST USER")
        print(request.user)
        print(request.data['slot'])




        if(request.user.is_anonymous ):
            request.user=None
            print("Testi")

        try:
            totalCount=0
            limitSlot=SlotPC.objects.values_list('limitSlot', flat=True).get(pk=request.data['io_id'][0]['pc_slot'])
            print(limitSlot)
            print("Testi")
            logging.debug("Blocked IN")

            for i in (request.data['io_id']):
                print(i)
                remaining_seats=SlotPC.objects.values_list('remaining_seats', flat=True).get(pk=i['pc_slot'])
                print(remaining_seats)
                itemCount=i['count']
                if(itemCount>remaining_seats):
                    cont={"status":False,
                          "message":"Limit exceeds remaining_seats"}
                    print(cont)
                    raise ValueError(cont)
                totalCount+=(i['count'])

            print(totalCount)
            if(limitSlot<totalCount):
                cont={"status":False,
                      "message":"Limit exceeds"}
                print(cont)
                raise ValueError(cont)





            #Limit check  for the seating availability in concurrent booking
            #
            #
            # max_size_slot=Slot.objects.values_list('max_size', flat=True).get(pk=request.data['slot'])
            # pcslot=SlotPC.objects.filter(slot=request.data['slot'])
            # total_max_size_pcslot=0
            # for i in (pcslot):
            #     print("limitCategory")
            #     print(i.limitCategory)
            #     print("limitSlot")
            #     print(i.limitSlot)
            #     limitSlot=i.limitSlot
            #
            #     total_max_size_pcslot+=(i.remaining_seats+i.booked_seats)
            # if(total_max_size_pcslot>max_size_slot):
            #     cont={"status":False,
            #           "message":"Limit exceeds"}
            #
            #     raise ValueError(cont)
            #
            #
            #
            # for i in (request.data['io_id']):
            #     total_max_size_pcslot+=(i['count'])
            #
            #
            # if(total_max_size_pcslot>limitSlot):
            #     cont={"status":False,
            #           "message":"Limit exceeds"}
            #     raise ValueError(cont)
            #
            # if(total_max_size_pcslot>max_size_slot):
            #     cont={"status":False,
            #           "message":"Limit exceeds"}
            #
            #     raise ValueError(cont)

            print("REACHED here")
            orders=super(GenerateOrderGeneric, self).create(request, *args, **kwargs)
            print("DONE here")
            print(orders.status_code)
            print(request.data['payment'])
            if((orders.status_code==201) and  (request.data['payment'] == 'razorpay') ):

                try:

                    razororder= createRazorpayOrder(orders.data)
                    print(razororder['id'])
                    logging.debug("ORDER SATAUS")
                    logging.debug(orders.status_code)

                    Orders.objects.filter(id=orders.data["id"]).update(pm_order_id=razororder['id'],order_status="OC")
                    orders.data["order_status"]="Order Completed"
                    logging.debug("Order Completed")

                    order = {'razororder': razororder, 'order_details':orders.data,'status':True}
                    logging.debug(orders)
                    #order={"pm_order_id":razororder['id'],'ticket':orders.data['ticket_code'],'payment_status':orders.data['payment_status'],'order_status':orders.data['order_status'],'order_no':orders.data['order_no'],
                    #       'seller':orders.data['seller'],'is_order_seller':orders.data['is_order_seller'] ,'id':orders.data['id'],'status':True}
                    logging.debug(orders)
                    #order={'order_details':orders.data,'status':True}
                    return Response(order, status=status.HTTP_201_CREATED)

                except Exception as ValidationError:
                    cont={"status":False,
                          "message":str(ValidationError)}

                    return Response(cont)

            elif(orders.status_code==201) and ((request.data['payment']=='payfort') or (request.data['payment']=='freeevent')):
                try:

                    #razororder= createRazorpayOrder(orders.data)
                    #print(razororder['id'])
                    logging.debug("ORDER SATAUS")
                    print("asd")
                    logging.debug(orders.status_code)
                    p = get_object_or_404(PaymentMethod, slug=request.data['payment'])
                    print(p.name)


                    Orders.objects.filter(id=orders.data["id"]).update(payment_method=p,order_status="OC")
                    orders.data["order_status"]="Order Completed"
                    logging.debug("Order Completed")

                    order = { 'order_details':orders.data,'status':True}
                    logging.debug(orders)
                    #order={"pm_order_id":razororder['id'],'ticket':orders.data['ticket_code'],'payment_status':orders.data['payment_status'],'order_status':orders.data['order_status'],'order_no':orders.data['order_no'],
                    #       'seller':orders.data['seller'],'is_order_seller':orders.data['is_order_seller'] ,'id':orders.data['id'],'status':True}
                    logging.debug(orders)
                    #order={'order_details':orders.data,'status':True}
                    return Response(order, status=status.HTTP_201_CREATED)

                except Exception as ValidationError:
                    cont={"status":False,
                          "message":str(ValidationError)}

                    return Response(cont)
            else:
                cont={"status":False,
                  "message":"No payment found for "+str(request.data['payment'])}

                return Response(cont)


        except Exception as ValidationError:
            print(ValidationError)
            cont={"status":False,
                  "message":str(ValidationError)}
            return Response(cont)



class GenerateOrderSeller(generics.CreateAPIView):
    """
    Create an order from server
    """
    serializer_class = EventOrderSerializer
    #permission_classes = (AllowAny,)
    permission_classes = (IsAuthenticated,)
    #permission_classes = (AllowAny,)
    authentication_classes = (TokenAuthentication,)

    def create(self, request, *args, **kwargs):
        self.serializer_class = EventOrderSerializer
        print(request)
        if(request.user):
            print(request.user)

        try:
            totalCount=0
            limitSlot=SlotPC.objects.values_list('limitSlot', flat=True).get(pk=request.data['io_id'][0]['pc_slot'])
            print(limitSlot)
            print("Testi")
            logging.debug("Blocked IN")

            for i in (request.data['io_id']):
                print(i)
                remaining_seats=SlotPC.objects.values_list('remaining_seats', flat=True).get(pk=i['pc_slot'])
                print(remaining_seats)
                itemCount=i['count']
                if(itemCount>remaining_seats):
                    cont={"status":False,
                          "message":"Limit exceeds remaining_seats"}
                    print(cont)
                    raise ValueError(cont)
                totalCount+=(i['count'])

            print(totalCount)
            if(limitSlot<totalCount):
                cont={"status":False,
                      "message":"Limit exceeds"}
                print(cont)
                raise ValueError(cont)

            orders=super(GenerateOrderSeller, self).create(request, *args, **kwargs)
            print("DONE here")
            print(orders.status_code)
            if(orders.status_code==201):

                try:

                    #razororder= createRazorpayOrder(orders.data)
                    #print(razororder['id'])
                    logging.debug("ORDER SATAUS")
                    logging.debug(orders.status_code)
                    p = get_object_or_404(PaymentMethod, slug="collectcash")
                    seller = get_object_or_404(Seller, user=request.user)

                    print(p.name)
                    print("***************")
                    print(seller)
                    Orders.objects.filter(id=orders.data["id"]).update(payment_method=p,order_status="OC",seller=seller)
                    #ord.seller=request.user
                    orders.data["order_status"]="Order Completed"
                    logging.debug("Order Completed")

                    order = { 'order_details':orders.data,'status':True}
                    logging.debug(orders)
                    #order={"pm_order_id":razororder['id'],'ticket':orders.data['ticket_code'],'payment_status':orders.data['payment_status'],'order_status':orders.data['order_status'],'order_no':orders.data['order_no'],
                    #       'seller':orders.data['seller'],'is_order_seller':orders.data['is_order_seller'] ,'id':orders.data['id'],'status':True}
                    logging.debug(orders)
                    #order={'order_details':orders.data,'status':True}
                    return Response(order, status=status.HTTP_201_CREATED)

                except Exception as ValidationError:
                    cont={"status":False,
                          "message":str(ValidationError)}

                    return Response(cont)

        except Exception as ValidationError:
            print(ValidationError)
            cont={"status":False,
                  "message":str(ValidationError)}
            return Response(cont)



class GenerateOrder(generics.CreateAPIView):
    """
    Create an order from server
    """
    serializer_class = EventOrderSerializer

    permission_classes = (AllowAny,)
    authentication_classes = (TokenAuthentication,)



    def create(self, request, *args, **kwargs):
            print("**************")
            print(request.data)
            print("END data")

            print(request)

            #
            # user=(Event.objects.filter(event_id=request.data['event_id']).values('owner','name'))
            # print(user[0]['owner'])
            # print(user[0]['name'])
            # print(User.objects.filter(id=user[0]['owner']).values("email"))
            print("*************")
            print("REQUEST USER")
            print(request.user)
            print(request.data['slot'])




            if(request.user.is_anonymous ):
                request.user=None
                print("Testi")



            try:
                totalCount=0
                limitSlot=SlotPC.objects.values_list('limitSlot', flat=True).get(pk=request.data['io_id'][0]['pc_slot'])
                print(limitSlot)
                print("Testi")
                logging.debug("Blocked IN")

                for i in (request.data['io_id']):
                    print(i)
                    remaining_seats=SlotPC.objects.values_list('remaining_seats', flat=True).get(pk=i['pc_slot'])
                    print(remaining_seats)
                    itemCount=i['count']
                    if(itemCount>remaining_seats):
                        cont={"status":False,
                              "message":"Limit exceeds remaining_seats"}
                        print(cont)
                        raise ValueError(cont)
                    totalCount+=(i['count'])

                print(totalCount)
                if(limitSlot<totalCount):
                    cont={"status":False,
                           "message":"Limit exceeds"}
                    print(cont)
                    raise ValueError(cont)





                #Limit check  for the seating availability in concurrent booking
                #
                #
                # max_size_slot=Slot.objects.values_list('max_size', flat=True).get(pk=request.data['slot'])
                # pcslot=SlotPC.objects.filter(slot=request.data['slot'])
                # total_max_size_pcslot=0
                # for i in (pcslot):
                #     print("limitCategory")
                #     print(i.limitCategory)
                #     print("limitSlot")
                #     print(i.limitSlot)
                #     limitSlot=i.limitSlot
                #
                #     total_max_size_pcslot+=(i.remaining_seats+i.booked_seats)
                # if(total_max_size_pcslot>max_size_slot):
                #     cont={"status":False,
                #           "message":"Limit exceeds"}
                #
                #     raise ValueError(cont)
                #
                #
                #
                # for i in (request.data['io_id']):
                #     total_max_size_pcslot+=(i['count'])
                #
                #
                # if(total_max_size_pcslot>limitSlot):
                #     cont={"status":False,
                #           "message":"Limit exceeds"}
                #     raise ValueError(cont)
                #
                # if(total_max_size_pcslot>max_size_slot):
                #     cont={"status":False,
                #           "message":"Limit exceeds"}
                #
                #     raise ValueError(cont)

                print("REACHED here***************")
                orders=super(GenerateOrder, self).create(request, *args, **kwargs)
                print("DONE here ORder id")
                print(orders.status_code)


                if(orders.status_code==201):

                    try:


                        razororder= createRazorpayOrder(orders.data)
                        print(razororder['id'])
                        logging.debug("ORDER SATAUS")
                        logging.debug(orders.status_code)
                        p = get_object_or_404(PaymentMethod, slug="razorpay")
                        print(p.name)

                        Orders.objects.filter(id=orders.data["id"]).update(payment_method=p,pm_order_id=razororder['id'],order_status="OC")
                        print("ORder completed")
                        print(orders.data['id'])

                        orders.data["order_status"]="Order Completed"
                        logging.debug("Order Completed")

                        order = {'razororder': razororder, 'order_details':orders.data,'status':True}
                        logging.debug(orders)
                        #order={"pm_order_id":razororder['id'],'ticket':orders.data['ticket_code'],'payment_status':orders.data['payment_status'],'order_status':orders.data['order_status'],'order_no':orders.data['order_no'],
                        #       'seller':orders.data['seller'],'is_order_seller':orders.data['is_order_seller'] ,'id':orders.data['id'],'status':True}
                        logging.debug(orders)
                        #order={'order_details':orders.data,'status':True}
                        if( not request.user is None ):
                            print(orders.data['id'])
                            request.user.customer.orders.add(orders.data['id'])
                        return Response(order, status=status.HTTP_201_CREATED)

                    except Exception as ValidationError:
                        cont={"status":False,
                              "message":str(ValidationError)}

                        return Response(cont)
            except Exception as ValidationError:
                print("VAlidation error")
                print(ValidationError)
                cont={"status":False,
                      "message":str(ValidationError)}
                return Response(cont)




class GenerateOrderRazorpay(GenerateOrder):
    def post(self, request, *args, **kwargs):


        return super(GenerateOrderRazorpay, self).post(request, *args, **kwargs)


class GenerateOrderSellerFree(GenerateOrderSeller):
    def post(self, request, *args, **kwargs):
        return super(GenerateOrderSellerFree, self).post(request, *args, **kwargs)


class GenerateOrderPayFort(GenerateOrderGeneric):
    def post(self, request, *args, **kwargs):
        return super(GenerateOrderPayFort, self).post(request, *args, **kwargs)






@csrf_exempt
def GenerateOrderFun(request,*args, **kwargs):

    return GenerateOrderRazorpay.as_view()(request, *args, **kwargs)


@csrf_exempt
def GenerateOrderSellerFun(request,*args, **kwargs):
    print("ORDER SELLER")
    return GenerateOrderSellerFree.as_view()(request, *args, **kwargs)


@csrf_exempt
def GenerateOrderGenericFun(request,*args, **kwargs):
    print("Donne")
    return GenerateOrderPayFort.as_view()(request, *args, **kwargs)




def process_data(self,request):
    # do processing...
    #result = json.dumps(data)
    try:

        print('Finished processing')
        print(request.data['id'])
        #print(result)
        ord=Orders.objects.filter(id=request.data['id'])
        if(not ord):
            raise  exceptions.NotFound("Object Not found")


        print(ord)
        for item in ord:
            oitems = OrderItems.objects.filter(io_id=item.id)
            grandtotal=float(item.grandtotal)/100
            address=str(item.event.address_venue)
            spl = address.split(",") # split into list of individual items
            venue_address="\n".join([",".join(spl[i:i+3]) for i in range(0,len(spl),3)])

            orderdetails={"cust_name":item.cust_name.capitalize(),
                          "cust_email":item.cust_email,
                          "event":item.event,
                          "venue":item.event.address_venue,

                          "event_image":item.event.image_thumb.url,
                          "slot":item.slot,
                          "date_begin":item.slot.start_time.date(),
                          "date_end":item.slot.end_time.date(),

                          "start_date":item.slot.start_time.strftime("%A %B %d, %Y %H:%M %p"),
                          "begin":item.slot.start_time.time(),
                          "end_date":item.slot.end_time.strftime("%A %B %d, %Y %H:%M %p"),
                          #"venue_address":str(item.event.address_venue).replace(',','\n'),
                          "venue_address":str(venue_address),

                          "end":item.slot.end_time.time(),

                          #"date":item.event.start_time.date(),
                          #"begin":item.event.start_time.time(),
                          #"end":item.event.end_time.time(),



                          "cust_phone":item.cust_phone,
                          "ticket_code":item.ticket_code,
                          "ticket_type":item.ticket_type,

                          "grandtotal":grandtotal,
                          "order_no":item.id,

                          "ticket":settings.AWS_MEDIA_URL+"email/img/ticket.png",
                          "logo":settings.AWS_MEDIA_URL+"email/img/logo.png",
                          "time":settings.AWS_MEDIA_URL+"email/img/time.png",
                          "location":settings.AWS_MEDIA_URL+"email/img/location.png",
                          "fb":settings.AWS_MEDIA_URL+"email/img/fb.png",
                          "tw":settings.AWS_MEDIA_URL+"email/img/tw.png",
                          "in":settings.AWS_MEDIA_URL+"email/img/in.png",
                          "li":settings.AWS_MEDIA_URL+"email/img/li.png",
                          "appicon":settings.AWS_MEDIA_URL+"email/img/app-icon.png",


                          }



        print("Event image****")
        print(orderdetails['date_begin'])


        print(orderdetails['begin'])
        print(orderdetails['date_end'])
        print(orderdetails['end'])
        orderi=[]


        for oi in oitems:
            print("IN ORDER ITEMS ***********")
            orderitems = { "item_name": oi.item_name,
                           "item_price": oi.item_price,
                           "count": oi.count,

                           }
            #Calculating and updating  seats update pnly if order is generated

            orderi.append(orderitems)


        #context = dict(
            #video_id='J9go2nj6b3M',
            #options_example=QRCodeOptions(size='t', border=6, error_correction='L'),
        #)

        order={"orderdetails":orderdetails,"itemdetails":orderi}
        #print(order)

        to=[item.cust_email,]
        #print(to)

        template='events_api/QRCode.html'
        context = dict(
            my_options=QRCodeOptions(size='t', border=6, error_correction='L'),)


        subject = 'Thanks, Your booking hasbeen confirmed with collabo Event '
        html_message = render_to_string(template, {'context': context,'order':order})
        plain_message = strip_tags(html_message)
        from_email = settings.EMAIL_HOST_USER
        #to = 'dbpillai@gmail.com'
        data=re.sub(r'(<img src="data:image/png;base64, )(.*?)" alt=".*?">', r'\2', html_message)


        filename=str(order['orderdetails']['ticket_code'])+str(".png")
        print("FILENAME")
        print(filename)
        fh = open(filename, "wb")
        fh.write(base64.b64decode(data))
        fh.close()


        #print("Email has to send")



        template = 'events_api/email.html'
        #template = 'events_api/finalTemplate.html'


        def email_embed_image(email, img_content_id, img_data):
            """
            email is a django.core.mail.EmailMessage object
            """
            img = MIMEImage(img_data)
            img.add_header('Content-ID', '<%s>' % img_content_id)
            img.add_header('Content-Disposition', 'inline')
            email.attach(img)

        subject = 'Thanks, Your booking hasbeen confirmed with collabo Event '
        html_message = render_to_string(template, {'context': context,'order':order})
        plain_message = strip_tags(html_message)
        from_email = settings.EMAIL_HOST_USER
        #to = 'dbpillai@gmail.com'
        recipient = [to,]
        sender = from_email
        image_path = filename
        image_name = Path(image_path).name


        subject = "Your booking on Collabo has been confirmed"
        text_message='events_api/email.html'




        # define function for sending email
        def send_email(subject, text_content, html_content=None, sender=sender, recipient=recipient, image_path=None, image_name=None,):
            email = EmailMultiAlternatives(subject=subject, body=text_content, from_email=sender, to=recipient if isinstance(recipient, list) else [recipient])

            if all([html_content,image_path,image_name]):
                email.attach_alternative(html_content, "text/html")
                email.content_subtype = 'html'  # set primary content to be text/html
                email.mixed_subtype = 'related' # it is important part that ensures embedding of image

                with open(image_path, mode='rb') as f:
                    image = MIMEImage(f.read())
                    email.attach(image)
                    print("Image PATH")
                    print(image)
                    print(image_name)

                    image.add_header('Content-ID', f'<{image_name}>')



            email.send()


        # send test email
        send_email(subject="Your booking on Collabo has been Confirmed", text_content=text_message, html_content=html_message, sender=sender, recipient=recipient, image_path=image_path, image_name=image_name,)
        #send sns

        path= request.build_absolute_uri()
        ticket=orderdetails['ticket_code']

        link="/api/"+ticket+"/ticket-code/"
        path = str(path)  # this returns the full system path to the original file
        base = path.rsplit('/api', 1)[0]  # the file name only (minus path or extension)
        link=base+link
        print(link)
        print("Date begin")
        date_begin=order["orderdetails"]["date_begin"]
        d = date_begin.strftime("%d %b, %Y")


        message=" Congratulations! Your ticket for {0} on {1} {2} {3} has been confirmed. Ticket Code is : {4} Go to link {5}".format(item.event ,item.slot.title, d, order["orderdetails"]["begin"],item.ticket_code,link)
        number="+91"+item.cust_phone
        sms=SendMessage(number,message)
        print("BASE DIR")
        print(settings.BASE_DIR)
        filetodel=settings.BASE_DIR+"//"+str(image_name)
        #delete QR code
        if os.path.exists(filetodel):
            print(filetodel)
            os.remove(filetodel)
            print("Deleted file")
        else:
            print("Can not delete the file as it doesn't exists")

        Orders.objects.filter(id=request.data['id']).update(payment_status="PC")
        print("UPDATE PAYMENT STATUS Payment complete")




    except Exception as e:
        cont={"status":False,
          "message":str(e)}

        raise  Exception (cont)


    cont={"cont": str(order),
      "success":"Payment Completed succesfully","notify sms":sms,
      }


    return (Response(cont))











#######

class PaymentFort(APIView):

    authentication_classes = ()
    permission_classes = (AllowAny,)

    def post(self, request,*args, **kwargs):


        try:
            id= get_object_or_404(Orders,order_no =request.data['merchant_reference'])
            grandtotal=str(int(id.grandtotal))
            print(grandtotal)
            cust_email=id.cust_email

            status=Orders.objects.filter(id=id.id).values('payment_status')
            print(status[0]['payment_status'])
            if(status[0]['payment_status'])=="PC":
                cont={"status":False,
                      "message":"Payment Already Done"}
                raise ValueError(cont)

            print("BOOKED SEATS")
            ord=Orders.objects.filter(id=id.id)
            ticket_code=ord[0].ticket_code
            print(ord[0])

            #ticket_code=ord.ticket_code
            for item in ord:
                slot=item.slot.pk

                print("SLOT")
                print(slot)
                oitems = OrderItems.objects.filter(io_id=item.id)
                for orderitems in oitems:
                    print("Current Itel reminag seats")
                    print(orderitems.pc_cat)
                    print(orderitems.pc_cat.pk)

                    pcslot_rem=SlotPC.objects.filter(slot=slot,price_cat=orderitems.pc_cat).values('remaining_seats')
                    curr_slot_rem=pcslot_rem[0]['remaining_seats']
                    print(curr_slot_rem)

                    if (curr_slot_rem<orderitems.count):
                        print("LimitCategory is none")

                        cont={"status":False,
                              "message":"Limit exceeds"}
                        raise ValueError(cont)



                #razorpay_signature = request.data['razorpay_signature']
                #content=""
                #Check Status of the Merchant

                # Do Puchase for the merchant


                purchaseData={
                    "command" : "PURCHASE",
                    'access_code' : settings.PAYFORT_ACCESS_CODE,
                    'merchant_identifier' : settings.PAYFORT_MERCHANT_IDENTIFIER,
                    'merchant_reference' : request.data['merchant_reference'],
                    'language' : settings.PAYFORT_LANGUAGE,
                    "amount" : grandtotal,
                    "currency" : settings.PAYFORT_CURRENCY,
                    "customer_email" :cust_email,
                    "token_name":request.data['token_name'],
                    #"check_3ds":request.data['check_3ds'],

                }
                purcahsesign=get_signature(purchaseData)
                print(purcahsesign)

                purchaseData={
                    "command" : "PURCHASE",
                    "access_code" : settings.PAYFORT_ACCESS_CODE,
                    "merchant_identifier": settings.PAYFORT_MERCHANT_IDENTIFIER,
                    "merchant_reference" : request.data['merchant_reference'],
                    "amount" :grandtotal,
                    "currency" : settings.PAYFORT_CURRENCY,
                    "language" : settings.PAYFORT_LANGUAGE,
                    "customer_email" :cust_email,
                    "signature" :purcahsesign,
                    "token_name":request.data['token_name'],
                    #"check_3ds":request.data['check_3ds'],

                }
                #Do purchase
                payfort_resp=payfort_operation(settings.PAYFORT_URL,purchaseData)
                return Response({"status":True,"message":payfort_resp})
        except Exception as e:
            cont={"status":False,
              "message":str(e),
              }
            return Response({"status":True,"message":cont})




class PayFortFinal(APIView):


    authentication_classes = ()
    permission_classes = (AllowAny,)

    def post(self, request,*args, **kwargs):


        try:
            id= get_object_or_404(Orders,order_no =request.data['merchant_reference'])

            grandtotal=str(int(id.grandtotal))
            cust_email=id.cust_email
            id=id.id


            status=Orders.objects.filter(id=id).values('payment_status')
            print(status[0]['payment_status'])
            if(status[0]['payment_status'])=="PC":
                cont={"status":False,
                      "message":"Payment Already Done"}
                raise ValueError(cont)

            print("BOOKED SEATS")
            ord=Orders.objects.filter(id=id)
            ticket_code=ord[0].ticket_code
            print(ord[0])

            #ticket_code=ord.ticket_code
            for item in ord:
                slot=item.slot.pk

                print("SLOT")
                print(slot)
                oitems = OrderItems.objects.filter(io_id=item.id)

                arrData={
                    'query_command' : 'CHECK_STATUS',
                    'access_code' : settings.PAYFORT_ACCESS_CODE,
                    'merchant_identifier' : settings.PAYFORT_MERCHANT_IDENTIFIER,
                    'merchant_reference' : request.data['merchant_reference'],
                    'language' : settings.PAYFORT_LANGUAGE,
                    }


                payfort_signature=get_signature(arrData)
                url = settings.PAYFORT_URL;
                arrData = {
                    'query_command' : 'CHECK_STATUS',
                    'access_code' : settings.PAYFORT_ACCESS_CODE,
                    'merchant_identifier' : settings.PAYFORT_MERCHANT_IDENTIFIER,
                    'merchant_reference' : request.data['merchant_reference'],
                    'language' : settings.PAYFORT_LANGUAGE,
                    'signature' : payfort_signature,
                }
                payfort_resp=payfort_operation(url,arrData)
                print(payfort_resp['response_code'])






                if payfort_resp['response_code'] != '12000':
                    print("not equal")
                    Orders.objects.filter(id=id).update(payment_status="PF")


                    return Response({"status":False,"message":"Payment Not captured/ Failed","payfort":payfort_resp})




                #Calculating and updating  seats update pnly if order is generated
                Orders.objects.filter(id=id).update(payment_status="PC", pm_payment_id=payfort_resp['fort_id'],pm_order_id=id)
                #oitems = OrderItems.objects.filter(io_id=item.id)
                pc_slot=SlotPC.objects.filter(slot=slot)
                #user=(Event.objects.filter(event_id=request.data['event_id']).values('owner','name'))
                for orderitems in oitems:
                    print("ORDER  Booked ITEMS")
                    print(orderitems.pc_slot.booked_seats)

                    orderitems.pc_slot.booked_seats=(orderitems.pc_slot.booked_seats + orderitems.count)
                    print(orderitems.pc_slot.booked_seats)
                    orderitems.pc_slot.save()



                    if(orderitems.pc_slot.limitCategory==None):


                        #thes is no limit for price category, set update on limit for slot and all corresponding  falling under this slot

                        pcslot1=SlotPC.objects.filter(slot=slot)
                        for pcs in pcslot1:

                            pcs.limitSlot=(pcs.limitSlot - orderitems.count)
                            print(pcs.limitSlot)
                            print(pcs.remaining_seats)
                            pcs.save()

                            if(pcs.limitCategory is None):
                                pcs.remaining_seats=(pcs.remaining_seats - orderitems.count)
                                print(pcs.remaining_seats)
                                pcs.save()


                    else:

                        orderitems.pc_slot.remaining_seats=(orderitems.pc_slot.remaining_seats - orderitems.count)

                        orderitems.pc_slot.save()
                        pcslot2=SlotPC.objects.filter(slot=slot)
                        print("Limit is not none")
                        for pcs in pcslot2:
                            pcs.limitSlot=(orderitems.pc_slot.limitSlot - orderitems.count)
                            print(pcs.limitSlot)
                            pcs.save()
                            if(pcs.limitCategory is None):
                                pcs.remaining_seats=pcs.limitSlot
                                pcs.save()


                finalpcs=SlotPC.objects.filter(slot=slot,).exclude(limitCategory__isnull=True)
                print("FINALLIST")
                for item in finalpcs:
                    print(item.seating_id)
                    if(item.remaining_seats>item.limitSlot):
                        item.remaining_seats=item.limitSlot
                        item.save()


            cont={"status":True,
                  "message":"Updated",
                  "ticket code":ticket_code

                  }




        except Exception as e:
            cont={"status":False,
                  "message":str(e),
                  }
        if(cont['status']==True):
            try:
                request.data['id']=id
                print("ID")
                print(request.data['id'])


                t = Thread(target=process_data, args=(self,request ))
                t.start()
            except Exception as e:
                cont={"status":False,
                      "messageThread":str(e),
                      }
        return Response((cont))


class  SellerPaymentFree(APIView):
    #permission_classes = (AllowAny,)
    permission_classes = (IsAuthenticated,)
    #permission_classes = (AllowAny,)
    authentication_classes = (TokenAuthentication,)

    def post(self, request,*args, **kwargs):


        try:

            status=Orders.objects.filter(id=request.data['id']).values('payment_status')
            print(status[0]['payment_status'])
            if(status[0]['payment_status']=="FE" or status[0]['payment_status']=="PC"):
                cont={"status":False,
                      "message":"Already Done"}
                raise ValueError(cont)

            print("BOOKED SEATS")
            ord=Orders.objects.filter(id=request.data['id'])
            ticket_code=ord[0].ticket_code
            print(ord[0])

            #ticket_code=ord.ticket_code
            for item in ord:
                slot=item.slot.pk

                print("SLOT")
                print(slot)
                oitems = OrderItems.objects.filter(io_id=item.id)
                for orderitems in oitems:
                    print("Current Itel reminag seats")
                    print(orderitems.pc_cat)
                    print(orderitems.pc_cat.pk)

                    pcslot_rem=SlotPC.objects.filter(slot=slot,price_cat=orderitems.pc_cat).values('remaining_seats')
                    curr_slot_rem=pcslot_rem[0]['remaining_seats']
                    print(curr_slot_rem)

                    if (curr_slot_rem<orderitems.count):
                        print("LimitCategory is none")

                        cont={"status":False,
                              "message":"Limit exceeds"}
                        raise ValueError(cont)



                #Calculating and updating  seats update pnly if order is generated
                Orders.objects.filter(id=request.data['id']).update(payment_status="FE", pm_payment_id="No Payment")
                #oitems = OrderItems.objects.filter(io_id=item.id)
                pc_slot=SlotPC.objects.filter(slot=slot)
                #user=(Event.objects.filter(event_id=request.data['event_id']).values('owner','name'))
                for orderitems in oitems:
                    print("ORDER  Booked ITEMS")

                    orderitems.pc_slot.booked_seats=(orderitems.pc_slot.booked_seats + orderitems.count)
                    print(orderitems.pc_slot.booked_seats)
                    orderitems.pc_slot.save()



                    if(orderitems.pc_slot.limitCategory==None):


                        #thes is no limit for price category, set update on limit for slot and all corresponding  falling under this slot

                        pcslot1=SlotPC.objects.filter(slot=slot)
                        for pcs in pcslot1:

                            pcs.limitSlot=(pcs.limitSlot - orderitems.count)
                            print(pcs.limitSlot)
                            print(pcs.remaining_seats)
                            pcs.save()

                            if(pcs.limitCategory is None):
                                pcs.remaining_seats=(pcs.remaining_seats - orderitems.count)
                                print(pcs.remaining_seats)
                                pcs.save()


                    else:

                        orderitems.pc_slot.remaining_seats=(orderitems.pc_slot.remaining_seats - orderitems.count)

                        orderitems.pc_slot.save()
                        pcslot2=SlotPC.objects.filter(slot=slot)
                        print("Limit is not none")
                        for pcs in pcslot2:
                            pcs.limitSlot=(orderitems.pc_slot.limitSlot - orderitems.count)
                            print(pcs.limitSlot)
                            pcs.save()
                            if(pcs.limitCategory is None):
                                pcs.remaining_seats=pcs.limitSlot
                                pcs.save()


                finalpcs=SlotPC.objects.filter(slot=slot,).exclude(limitCategory__isnull=True)
                print("FINALLIST")
                for item in finalpcs:
                    print(item.seating_id)
                    if(item.remaining_seats>item.limitSlot):
                        item.remaining_seats=item.limitSlot
                        item.save()
            event=ord[0].event.pk
            print("EVENT")
            print(event)
            seller = get_object_or_404(Seller, user=request.user)
            print("SELLER")
            print(seller)
            print("ORDER")
            print(ord[0].pk)
            print(ord[0].seller.event.all())

            seller=Seller.objects.filter(user=request.user,event__eventdetail__in=[event]).values("event")

            # for i in seller:
            #     print(i.event.all())
            #     for j in i.event.all():
            #
            #         print(j.pk)
            #         eveseller = get_object_or_404(EventSeller, id=j.pk)
            print(seller)
            print(type(seller))
            print(seller[0]['event'])


            print("ADD seller")
            eventseller = get_object_or_404(EventSeller, id=seller[0]['event'])
            eventseller.order.add(ord[0].pk)

            cont={"status":True,
                  "message":"Updated",
                  "ticket code":ticket_code

                  }




        except Exception as e:
            cont={"status":False,
                  "message":str(e),
                  }
        if(cont['status']==True):
            try:
                t = Thread(target=process_data, args=(self,request ))
                t.start()
            except Exception as e:
                cont={"status":False,
                      "messageThread":str(e),
                      }
        return Response((cont))




class PaymentFree(APIView):

    authentication_classes = ()
    permission_classes = (AllowAny,)

    def post(self, request,*args, **kwargs):


        try:

            status=Orders.objects.filter(id=request.data['id']).values('payment_status')
            print(status[0]['payment_status'])
            if(status[0]['payment_status'])=="FE":
                cont={"status":False,
                      "message":"Already Done"}
                raise ValueError(cont)

            print("BOOKED SEATS")
            ord=Orders.objects.filter(id=request.data['id'])
            ticket_code=ord[0].ticket_code
            print(ord[0])

            #ticket_code=ord.ticket_code
            for item in ord:
                slot=item.slot.pk

                print("SLOT")
                print(slot)
                oitems = OrderItems.objects.filter(io_id=item.id)
                for orderitems in oitems:
                    print("Current Itel reminag seats")
                    print(orderitems.pc_cat)
                    print(orderitems.pc_cat.pk)

                    pcslot_rem=SlotPC.objects.filter(slot=slot,price_cat=orderitems.pc_cat).values('remaining_seats')
                    curr_slot_rem=pcslot_rem[0]['remaining_seats']
                    print(curr_slot_rem)

                    if (curr_slot_rem<orderitems.count):
                        print("LimitCategory is none")

                        cont={"status":False,
                              "message":"Limit exceeds"}
                        raise ValueError(cont)



                #Calculating and updating  seats update pnly if order is generated
                Orders.objects.filter(id=request.data['id']).update(payment_status="FE", pm_payment_id="No Payment")
                #oitems = OrderItems.objects.filter(io_id=item.id)
                pc_slot=SlotPC.objects.filter(slot=slot)
                #user=(Event.objects.filter(event_id=request.data['event_id']).values('owner','name'))
                for orderitems in oitems:
                    print("ORDER  Booked ITEMS")

                    orderitems.pc_slot.booked_seats=(orderitems.pc_slot.booked_seats + orderitems.count)
                    print(orderitems.pc_slot.booked_seats)
                    orderitems.pc_slot.save()



                    if(orderitems.pc_slot.limitCategory==None):


                        #thes is no limit for price category, set update on limit for slot and all corresponding  falling under this slot

                        pcslot1=SlotPC.objects.filter(slot=slot)
                        for pcs in pcslot1:

                            pcs.limitSlot=(pcs.limitSlot - orderitems.count)
                            print(pcs.limitSlot)
                            print(pcs.remaining_seats)
                            pcs.save()

                            if(pcs.limitCategory is None):
                                pcs.remaining_seats=(pcs.remaining_seats - orderitems.count)
                                print(pcs.remaining_seats)
                                pcs.save()


                    else:

                        orderitems.pc_slot.remaining_seats=(orderitems.pc_slot.remaining_seats - orderitems.count)

                        orderitems.pc_slot.save()
                        pcslot2=SlotPC.objects.filter(slot=slot)
                        print("Limit is not none")
                        for pcs in pcslot2:
                            pcs.limitSlot=(orderitems.pc_slot.limitSlot - orderitems.count)
                            print(pcs.limitSlot)
                            pcs.save()
                            if(pcs.limitCategory is None):
                                pcs.remaining_seats=pcs.limitSlot
                                pcs.save()


                finalpcs=SlotPC.objects.filter(slot=slot,).exclude(limitCategory__isnull=True)
                print("FINALLIST")
                for item in finalpcs:
                    print(item.seating_id)
                    if(item.remaining_seats>item.limitSlot):
                        item.remaining_seats=item.limitSlot
                        item.save()


            cont={"status":True,
                  "message":"Updated",
                  "ticket code":ticket_code

                  }




        except Exception as e:
            cont={"status":False,
                  "message":str(e),
                  }
        if(cont['status']==True):
            try:
                t = Thread(target=process_data, args=(self,request ))
                t.start()
            except Exception as e:
                cont={"status":False,
                      "messageThread":str(e),
                      }
        return Response((cont))




class PaymentFetch1(APIView):

    permission_classes = (AllowAny,)
    authentication_classes = (TokenAuthentication,)


    def post(self, request,*args, **kwargs):


        try:

            ord=Orders.objects.filter(pm_order_id=request.data['pm_order_id'])
            print(ord[0].payment_status)
            Orders.objects.filter(pm_order_id=request.data['pm_order_id']).update( pm_payment_id=request.data['pm_payment_id'])


            if(ord[0].payment_status)=="PC":
                cont={"status":True,
                      "message":"Payment Already Done",
                      "ticket code":ord[0].ticket_code}
                return Response((cont))

            print("BOOKED SEATS")
            ord=Orders.objects.filter(pm_order_id=request.data['pm_order_id'])
            ticket_code=ord[0].ticket_code
            print(ord[0])

            #ticket_code=ord.ticket_code
            for item in ord:
                request.data['id']=item.id
                print("sdsdf REQUEST ID")
                print(request.data['id'])
                slot=item.slot.pk

                print("SLOT")
                print(slot)
                oitems = OrderItems.objects.filter(io_id=item.id)
                for orderitems in oitems:
                    print("Current Itel reminag seats")
                    print(orderitems.pc_cat)
                    print(orderitems.pc_cat.pk)

                    pcslot_rem=SlotPC.objects.filter(slot=slot,price_cat=orderitems.pc_cat).values('remaining_seats')
                    curr_slot_rem=pcslot_rem[0]['remaining_seats']
                    print(curr_slot_rem)

                    if (curr_slot_rem<orderitems.count):
                        print("LimitCategory is none")

                        cont={"status":False,
                              "message":"Limit exceeds"}
                        raise ValueError(cont)



                razorpay_signature = request.data['razorpay_signature']
                content=""
                if razorpay_signature is not None and razorpay_signature != '':

                    try:
                        client = razorpay.Client(auth=(RAZORPAY_API_KEY, RAZORPAY_API_SECRET))



                        # #params_dict = {'pm_order_id': request.data['pm_order_id'],
                        #                        'pm_payment_id': request.data['pm_payment_id'],
                        #                        'razorpay_signature': request.data['razorpay_signature']}
                        params_dict = {'razorpay_order_id': request.data['pm_order_id'],
                                                              'razorpay_payment_id': request.data['pm_payment_id'],
                                                               'razorpay_signature': request.data['razorpay_signature']}

                        print("Signature")
                        print(params_dict)

                        content = client.utility.verify_payment_signature(params_dict)

                        print("Content")
                        print(content)
                    except Exception as e:
                        cont={"status":False,
                              "message":str(e),
                              }
                        return Response((cont))
                else:
                    #Capture Payment
                    try:

                        content=CapturePaymnet(request.data['pm_payment_id'],request.data['payment_amount'])
                    except Exception as e:
                        cont={"status":False,
                              "message":str(e),
                              }
                        return Response((cont))


                cont = {'payment-fetch': FetchRazorPayment(request.data['pm_payment_id']),
                            'content':content}

                if(cont['payment-fetch']['status']!='captured'):
                        Orders.objects.filter(pm_order_id=request.data['pm_order_id']).update(payment_status="PF", pm_payment_id=request.data['pm_payment_id'])
                        return Response({"status":False,"message":"Payment Not captured/ Failed","cont":cont})
                        #raise serializers.ValidationError("Payment Not captured/ Failed")

                    #captured varified send sms and emila notifictaions

                print(request.data['pm_order_id'])
                    #Orders.objects.filter(pm_order_id=request.data['pm_order_id']).update(payment_status="PC", pm_payment_id=request.data['pm_payment_id'])
                    #Calculating and updating  seats update pnly if order is generated
                #Orders.objects.filter(pm_order_id=request.data['pm_order_id']).update(payment_status="PC", pm_payment_id=request.data['pm_payment_id'])
                Orders.objects.filter(pm_order_id=request.data['pm_order_id']).update( pm_payment_id=request.data['pm_payment_id'])
                #oitems = OrderItems.objects.filter(io_id=item.id)
                pc_slot=SlotPC.objects.filter(slot=slot)
                #user=(Event.objects.filter(event_id=request.data['event_id']).values('owner','name'))
                for orderitems in oitems:
                    print("ORDER  Booked ITEMS")

                    orderitems.pc_slot.booked_seats=(orderitems.pc_slot.booked_seats + orderitems.count)
                    print(orderitems.pc_slot.booked_seats)
                    orderitems.pc_slot.save()



                    if(orderitems.pc_slot.limitCategory==None):


                        #thes is no limit for price category, set update on limit for slot and all corresponding  falling under this slot

                        pcslot1=SlotPC.objects.filter(slot=slot)
                        for pcs in pcslot1:

                            pcs.limitSlot=(pcs.limitSlot - orderitems.count)
                            print(pcs.limitSlot)
                            print(pcs.remaining_seats)
                            pcs.save()

                            if(pcs.limitCategory is None):
                                pcs.remaining_seats=(pcs.remaining_seats - orderitems.count)
                                print(pcs.remaining_seats)
                                pcs.save()


                    else:

                        orderitems.pc_slot.remaining_seats=(orderitems.pc_slot.remaining_seats - orderitems.count)

                        orderitems.pc_slot.save()
                        pcslot2=SlotPC.objects.filter(slot=slot)
                        print("Limit is not none")
                        for pcs in pcslot2:
                            pcs.limitSlot=(orderitems.pc_slot.limitSlot - orderitems.count)
                            print(pcs.limitSlot)
                            pcs.save()
                            if(pcs.limitCategory is None):
                                pcs.remaining_seats=pcs.limitSlot
                                pcs.save()


                finalpcs=SlotPC.objects.filter(slot=slot,).exclude(limitCategory__isnull=True)
                print("FINALLIST")
                for item in finalpcs:
                    print(item.seating_id)
                    if(item.remaining_seats>item.limitSlot):
                        item.remaining_seats=item.limitSlot
                        item.save()
                # when total slot is reaches  total booked seats
                # pcslots=SlotPC.objects.filter(slot=slot)
                # booked_seats=0
                # limit
                # for pcslot in pcslots:
                #     booked_seats+==pcslot.booked_seats




            cont={"status":True,
              "message":"Updated",
              "ticket code":ticket_code

              }




        except Exception as e:
            cont={"status":False,
                  "message":str(e),
                  }
        if(cont['status']==True):
            try:

                t = Thread(target=process_data, args=(self,request ))
                t.start()
            except Exception as e:
                cont={"status":False,
                      "messageThread":str(e),
                      }
        return Response((cont))






class PaymentFetch(APIView):

    authentication_classes = ()
    permission_classes = (AllowAny,)

    def post(self, request,*args, **kwargs):

            try:
                status=Orders.objects.filter(pm_order_id=request.data['pm_order_id']).values('payment_status')
                print(status[0]['payment_status'])
                # if(status[0]['payment_status'])=="PC":
                #     cont={"status":False,
                #           "message":"Payment Already Done"}
                #     raise ValueError(cont)


                client = razorpay.Client(auth=(RAZORPAY_API_KEY, RAZORPAY_API_SECRET))

                params_dict = {'pm_order_id': request.data['pm_order_id'],
                               'pm_payment_id': request.data['pm_payment_id'],
                               'razorpay_signature': request.data['razorpay_signature']}
                print("Signature")
                print(params_dict)

                content = client.utility.verify_payment_signature(params_dict)

                print("Content")
                print(content)
            except Exception as e:
                cont={"status":False,
                      "message":str(e),
                      }
                return Response((cont))

            try:

                cont = {'payment-fetch': FetchRazorPayment(request.data['pm_payment_id']),
                        'content':content}

                print(cont['payment-fetch']['status'])
                if(cont['payment-fetch']['status']!='captured'):
                    Orders.objects.filter(pm_order_id=request.data['pm_order_id']).update(payment_status="PF", pm_payment_id=request.data['pm_payment_id'])
                    raise serializers.ValidationError("Payment Not captured/ Failed")

                #captured varified send sms and emila notifictaions

                print(request.data['pm_order_id'])
            except Exception as e:

                cont={"status":False,
                      "message":str(e)}

                raise  Exception (cont)




            try:

                Orders.objects.filter(pm_order_id=request.data['pm_order_id']).update(payment_status="PC", pm_payment_id=request.data['pm_payment_id'])
                #Calculating and updating  seats update pnly if order is generated


                #spc=SlotPC.objects.filter(seating_id=pc_slot)
                print("BOOKED SEATS")
                ord=Orders.objects.filter(pm_order_id=request.data['pm_order_id'])
                for item in ord:
                    slot=item.slot.pk

                    print("SLOT")
                    print(slot)
                    oitems = OrderItems.objects.filter(io_id=item.id)
                    for orderitems in oitems:
                        print("Current Itel reminag seats")
                        print(orderitems.pc_cat)
                        print(orderitems.pc_cat.pk)

                        pcslot_rem=SlotPC.objects.filter(slot=slot,price_cat=orderitems.pc_cat).values('remaining_seats')
                        curr_slot_rem=pcslot_rem[0]['remaining_seats']
                        print(curr_slot_rem)

                        if (curr_slot_rem<orderitems.count):
                            print("LimitCategory is none")

                            cont={"status":False,
                              "message":"Limit exceeds"}
                            raise ValueError(cont)



                    pcslot=SlotPC.objects.filter(slot=slot)
                # user=(Event.objects.filter(event_id=request.data['event_id']).values('owner','name'))


                    print("PCSLOT After")
                    print(pcslot)

                    for orderitems in oitems:
                        print("orderitems")
                        print(orderitems)
                        #print(orderitems.pc_slot.booked_seats)

                        orderitems.pc_slot.booked_seats=(orderitems.pc_slot.booked_seats + orderitems.count)
                        orderitems.pc_slot.save()

                        print("Booked seats")
                        print(orderitems.pc_slot.booked_seats)

                        if(orderitems.pc_slot.limitCategory==None):


                            #thes is no limit for price category, set update on limit for slot and all corresponding  falling under this slot


                            for pcs in pcslot:
                                #pcs.save()

                                #print(pcs.remaining_seats)
                                #print(pcs.booked_seats)
                                print("AFTER UPDATE")

                                #need to update  remianing seats aswell as limit Slot
                                pcs.remaining_seats=(pcs.remaining_seats - orderitems.count)
                                pcs.limitSlot=(pcs.limitSlot - orderitems.count)
                                print(pcs.seating_id)
                                print(pcs.remaining_seats)
                                SlotPC.objects.filter(slot=slot,price_cat=pcs.price_cat,seating_id=pcs.seating_id).update(remaining_seats=int(pcs.remaining_seats),limitSlot=int(pcs.limitSlot))
                                print(pcs.seating_id)
                                print(pcs.remaining_seats)
                                print("Updated")
                                #pcs.save()
                                #SlotPC(force_update=True)








                        else:
                            orderitems.pc_slot.remaining_seats=(orderitems.pc_slot.remaining_seats - orderitems.count)
                            for pcs in pcslot:
                                pcs.limitSlot=(orderitems.pc_slot.limitSlot - orderitems.count)
                                pcs.save()

                    orderitems.pc_slot.save()
                    pcs.save()

            # booked_seats=spc[0].booked_seats
                # remaining_seats=spc[0].remaining_seats
                # print('Booked Seats:{0} Remaining Seats:{1}'.format(booked_seats,remaining_seats))
                # print("After booking")
                #
                # booked_seats=booked_seats+int(order_item['count'])
                # remaining_seats=remaining_seats-int(order_item['count'])
                # print('Booked Seats:{0} Remaining Seats:{1}'.format(booked_seats,remaining_seats))
                # max_size=Price_Category.objects.values_list('max_size', flat=True).get(pk=itemid)

                # #varification
                # print(max_size)
                # print(booked_seats+remaining_seats)
                # print(spc[0].seating_id)
                # print(spc[0].remaining_seats)

                ord=Orders.objects.filter(pm_order_id=request.data['pm_order_id'])
                for item in ord:
                    oitems = OrderItems.objects.filter(io_id=item.id)
                    grandtotal=float(item.grandtotal)/100
                    orderdetails={"cust_name":item.cust_name,
                                  "cust_email":item.cust_email,
                                  "event":item.event,
                                  "slot":item.slot,
                                  "cust_phone":item.cust_phone,

                                  "grandtotal":grandtotal,
                                  "order_no":item.id
                                  }

                orderi=[]
                for oi in oitems:
                    print("IN ORDER ITEMS ***********")
                    orderitems = { "item_name": oi.item_name,
                                   "item_price": oi.item_price,
                                   "count": oi.count,

                                   }
                    #Calculating and updating  seats update pnly if order is generated

                    orderi.append(orderitems)


                context = dict(
                    video_id='J9go2nj6b3M',
                    options_example=QRCodeOptions(size='t', border=6, error_correction='L'),
                )

                order={"orderdetails":orderdetails,"itemdetails":orderi,"context":context}
                #print(order)

                to=[item.cust_email,]
                #print(to)

                template='events_api/QRCode.html'
                context = dict(
                    my_options=QRCodeOptions(size='t', border=6, error_correction='L'),)


                subject = 'Thanks, Your booking hasbeen confirmed with collabo Event '
                html_message = render_to_string(template, {'context': context,'order':order})
                #print(html_message)
                plain_message = strip_tags(html_message)
                #print(html_message)
                from_email = settings.EMAIL_HOST_USER
                to = 'dbpillai@gmail.com'
                data=re.sub(r'(<img src="data:image/png;base64, )(.*?)" alt=".*?">', r'\2', html_message)
                #data = base64.urlsafe_b64encode((re.sub('data:image/\w+;base64,#i', '', html_message)))
                #print(data)
                #print("Before Saving to image file")





                filename=str(order['orderdetails']['order_no'])+str(".png")
                #print(filename)
                fh = open(filename, "wb")
                fh.write(base64.b64decode(data))
                fh.close()


                #print("Email has to send")



                template = 'events_api/emailTemplate.html'
                #template='events_api/QRCode.html'
                #template1 = 'events_api/test.html'
                #context = dict(
                 #   my_options=QRCodeOptions(size='t', border=6, error_correction='L'),)


                def email_embed_image(email, img_content_id, img_data):
                    """
                    email is a django.core.mail.EmailMessage object
                    """
                    img = MIMEImage(img_data)
                    img.add_header('Content-ID', '<%s>' % img_content_id)
                    img.add_header('Content-Disposition', 'inline')
                    email.attach(img)

                subject = 'Thanks, Your booking hasbeen confirmed with collabo Event '
                html_message = render_to_string(template, {'context': context,'order':order})
                #print(html_message)
                plain_message = strip_tags(html_message)
                #print(html_message)
                from_email = settings.EMAIL_HOST_USER
                to = 'dbpillai@gmail.com'
                #mail.send_mail(subject, html_message, from_email, [to], html_message=html_message)
                #print("Email sent succesfully")


                #print("CODE to send attachmnet")

                recipient = [to,]
                sender = from_email
                image_path = filename
                image_name = Path(image_path).name

                subject = "Your booking on Collabo has been confirmed"
                #text_message = f"Congratulations! Your ticket has been booked."
                text_message='events_api/emailTemplate.html'

                # define function for sending email
                def send_email(subject, text_content, html_content=None, sender=sender, recipient=recipient, image_path=None, image_name=None):
                    email = EmailMultiAlternatives(subject=subject, body=text_content, from_email=sender, to=recipient if isinstance(recipient, list) else [recipient])

                    if all([html_content,image_path,image_name]):
                        email.attach_alternative(html_content, "text/html")
                        email.content_subtype = 'html'  # set primary content to be text/html
                        email.mixed_subtype = 'related' # it is important part that ensures embedding of image

                        with open(image_path, mode='rb') as f:
                            image = MIMEImage(f.read())
                            email.attach(image)
                            #print(image)
                            #print(image_name)

                            image.add_header('Content-ID', f'<{image_name}>')

                    email.send()


                # send test email
                send_email(subject="Your booking on Collabo has been Confirmed", text_content=text_message, html_content=html_message, sender=sender, recipient=recipient, image_path=image_path, image_name=image_name)
                #send sns

                path= request.build_absolute_uri()

                #print(request.build_absolute_uri)
                path="http://192.168.0.101:8000/api/ticket-code/2BD3F1/"
                message=" Congratulations! Your ticket for {0} on {1} has been confirmed. link {2}".format(item.event ,item.slot,path)
                #message=" Congratulations! Your ticket for {0} on {1} has been confirmed. link"+" {{ url 'ticket-code' }}".format(item.event ,item.slot)
                #print(message)
                number="+91"+item.cust_phone
                #print(number)

                sms=SendMessage(number,message)


            # send to phone number






            except Exception as e:
                cont={"status":False,
                      "message":str(e)}

                raise  Exception (cont)


            cont={"cont": str(order),
                  "success":"Payment Completed succesfully","notify sms":sms,
                  }


            return (Response(cont))




class TicketCodeJson(generics.ListAPIView):
    permission_classes = (AllowAny,)
    #serializer_class = ArtistListWebSerializer
    #pagination_class = LargeResultsSetPagination


    def list(self, request):
        try:

            slug =self.request.GET.get('code', None)
            print(slug)
            #try:
            timeline = self.filter_queryset(self.get_queryset(slug))
            print(" timeline")
            print(timeline)
            serializer = BookPageSerializer(timeline,context={'status': Response.status_code,"request": request})
            print("serilizer data")
            print(serializer.data)




            return Response(serializer.data)
        except Exception as e:
            cont={"messageout":str(e),"status":False}
            return Response(cont)

        # except Exception as e:
        #     cont={"message":str(e),"status":False}
        #     return Response(cont)


    def get_queryset(self,slug):
        try:
            print("sdfd")
            print(slug)
            qs = get_object_or_404(Orders, ticket_code=slug)
            print("ORDER ID")
            print(qs.id)
            id=qs.event.id
            print("Event id")
            print(id)
            bookpage = BookPage(
                bookinginfo=[qs],

                relatedartist=Event.objects.filter(id=id),


                context={'status': "ok"}


            )
            print(bookpage)

            return bookpage
        except Exception as e:
            cont={"message1":str(e),"status":False}
            return Response(cont)



@csrf_exempt
def webhookpayment(request,):
    try:
        # print()
        #request['data'] = {"pm_order_id":'order_9A33XWu170gUtm'}

        request.data = json.loads(request.body)
        print(request.data)
        if(not ( request.data['event'] == 'payment.captured') ):
            raise  exceptions.NotFound("Event Not found")
        pm_payment_id=request.data['payload']['payment']['entity']['id']
        print(pm_payment_id)
        id = get_object_or_404(Orders, pm_payment_id=pm_payment_id)





        request.data['id'] = id.id
        print("Web hook id")
        print(request.data['id'])

        process_data(None,request)
        cont={"message":True}
        return HttpResponse(cont,status=200)

    except Exception as e:
        cont = {(str(e))}
    return HttpResponse(cont, status=200)

@csrf_exempt
def webhook(request,):
    try:
        # print()
        #request['data'] = {"pm_order_id":'order_9A33XWu170gUtm'}

        request.data = json.loads(request.body)
        print(request.data)
        if(not (request.data['event'] == 'order.paid' or request.data['event'] == 'payment.captured') ):
            raise  exceptions.NotFound("Event Not found")
        if(request.data['event'] == 'payment.captured'):
            pm_payment_id=request.data['payload']['payment']['entity']['id']
            print(pm_payment_id)
            order_id=request.data['payload']['payment']['entity']['order_id']
            if(pm_payment_id is not None and order_id is not None ):
                ord=Orders.objects.filter(Q(pm_payment_id=pm_payment_id) | Q(pm_order_id=order_id))



                #id = get_object_or_404(Orders, pm_payment_id=pm_payment_id)
            id=ord[0]

        else:
            order_id=request.data['payload']['order']['entity']['id']

            print(order_id)
            id = get_object_or_404(Orders, pm_order_id=order_id)
        print("ID")
        print(id.id)
        request.data['id'] = id.id
        print("Web hook id")
        print(request.data['id'])
        print(id.payment_status)
        if(id.payment_status=='PC'):
            cont={"already payment done":True}
            return HttpResponse(cont, status=200)

        process_data(None,request)
        cont={"message":True}
        return HttpResponse(cont,status=200)

    except Exception as e:
        cont = {(str(e))}
    return HttpResponse(cont, status=200)



@csrf_exempt
def order1(request,):
        # print()
        #request['data'] = {"pm_order_id":'order_9A33XWu170gUtm'}

        request.data = json.loads(request.body)
        print(request.data)
        cont = {"status":True}
        return HttpResponse(cont, status=200)


@csrf_exempt
def webhook1(request,):
    try:
        # print()
        #request['data'] = {"pm_order_id":'order_9A33XWu170gUtm'}

        request.data = json.loads(request.body)
        print(request.data)
        if(not (request.data['event'] == 'order.paid' or request.data['event'] == 'payment.captured') ):
            raise  exceptions.NotFound("Event Not found")
        if(request.data['event'] == 'payment.captured'):
            pm_payment_id=request.data['payload']['payment']['entity']['id']
            print(pm_payment_id)
            order_id=request.data['payload']['payment']['entity']['order_id']
            if(pm_payment_id is not None and order_id is not None ):
                ord=Orders.objects.filter(Q(pm_payment_id=pm_payment_id) | Q(pm_order_id=order_id))



                #id = get_object_or_404(Orders, pm_payment_id=pm_payment_id)
            id=ord[0]

        else:
            order_id=request.data['payload']['order']['entity']['id']

            print(order_id)
            id = get_object_or_404(Orders, pm_order_id=order_id)
        print("ID")
        print(id.id)
        request.data['id'] = id.id
        print("Web hook id")
        print(request.data['id'])
        print(id.payment_status)
        if(id.payment_status=='PC'):
            cont={"already payment done":True}
            return HttpResponse(cont, status=200)

        #booking Update
        id=ord
        for item in ord:
            slot=item.slot.pk

            oitems = OrderItems.objects.filter(io_id=item.id)


            for orderitems in oitems:
                print("ORDER  Booked ITEMS")

                orderitems.pc_slot.booked_seats=(orderitems.pc_slot.booked_seats + orderitems.count)
                print(orderitems.pc_slot.booked_seats)
                orderitems.pc_slot.save()



                if(orderitems.pc_slot.limitCategory==None):


                    #thes is no limit for price category, set update on limit for slot and all corresponding  falling under this slot

                    pcslot1=SlotPC.objects.filter(slot=slot)
                    for pcs in pcslot1:

                        pcs.limitSlot=(pcs.limitSlot - orderitems.count)
                        print(pcs.limitSlot)
                        print(pcs.remaining_seats)
                        pcs.save()

                        if(pcs.limitCategory is None):
                            pcs.remaining_seats=(pcs.remaining_seats - orderitems.count)
                            print(pcs.remaining_seats)
                            pcs.save()


                else:

                    orderitems.pc_slot.remaining_seats=(orderitems.pc_slot.remaining_seats - orderitems.count)

                    orderitems.pc_slot.save()
                    pcslot2=SlotPC.objects.filter(slot=slot)
                    print("Limit is not none")
                    for pcs in pcslot2:
                        pcs.limitSlot=(orderitems.pc_slot.limitSlot - orderitems.count)
                        print(pcs.limitSlot)
                        pcs.save()
                        if(pcs.limitCategory is None):
                            pcs.remaining_seats=pcs.limitSlot
                            pcs.save()


            finalpcs=SlotPC.objects.filter(slot=slot,).exclude(limitCategory__isnull=True)
            print("FINALLIST")
            for item in finalpcs:
                print(item.seating_id)
                if(item.remaining_seats>item.limitSlot):
                    item.remaining_seats=item.limitSlot
                    item.save()

        process_data(None,request)
        cont={"message":True}
        return HttpResponse(cont,status=200)

    except Exception as e:
        cont = {(str(e))}
    return HttpResponse(cont, status=200)




@csrf_exempt

def TicketCode(request,ticket_code):
    p = get_object_or_404(Orders, ticket_code=ticket_code)
    print(p)
    print(p.cust_name)
    try:


        oitems = OrderItems.objects.filter(io_id=p.id)
        grandtotal=float(p.grandtotal)/100
        orderdetails={"cust_name":p.cust_name,
                      "cust_email":p.cust_email,
                      "event":p.event,
                      "slot":p.slot,
                      "cust_phone":p.cust_phone,
                      "ticket_code":p.ticket_code,
                      "ticket_type":p.ticket_type,
                      "event_image":p.event.image_thumb.url,

                      "grandtotal":grandtotal,
                      "order_no":p.id
                      }
        orderi=[]
        for oi in oitems:
            print("IN ORDER ITEMS ***********")
            orderitems = { "item_name": oi.item_name,
                           "item_price": oi.item_price,
                           "count": oi.count,

                           }
            #Calculating and updating  seats update pnly if order is generated

            orderi.append(orderitems)

        order={"orderdetails":orderdetails,"itemdetails":orderi}
        print(order)
        template='events_api/QRCode.html'
        context = dict(
            my_options=QRCodeOptions(size='t', border=6, error_correction='L'),)
        subject = 'Thanks, Your booking hasbeen confirmed with collabo Event '
        html_message = render_to_string(template, {'context': context,'order':order})
        plain_message = strip_tags(html_message)
        from_email = settings.EMAIL_HOST_USER
        #to = 'dbpillai@gmail.com'
        data=re.sub(r'(<img src="data:image/png;base64, )(.*?)" alt=".*?">', r'\2', html_message)
        filename=str(order['orderdetails']['ticket_code'])+str(".png")
        #print(filename)
        fh = open(filename, "wb")
        fh.write(base64.b64decode(data))
        fh.close()
        html_message = render_to_string('events_api/ticketTemplate.html', {'context': context,'order':order})

        #return render(request,'events_api/ticketTemplate.html', {'context': context,'order':order})
    except Exception as e:
        return render(request,'events_api/TKT_NOT_FOUND.html')




class GetInTouch(APIView):

    authentication_classes = ()
    permission_classes = (AllowAny,)

    def post(self, request,*args, **kwargs):
        try:

            print(request.data)
            def email_embed_image(email, img_content_id, img_data):
                """
                email is a django.core.mail.EmailMessage object
                """
                img = MIMEImage(img_data)
                img.add_header('Content-ID', '<%s>' % img_content_id)
                img.add_header('Content-Disposition', 'inline')
                email.attach(img)

            subject = 'Getin touch message '
            from_email = settings.EMAIL_HOST_USER
            #to = 'dbpillai@gmail.com'
            recipient = [settings.EMAIL_HOST_USER]
            sender = from_email
            message=request.data['message']+"\n\n\n"+request.data['name']+"\n"+request.data['phone']
            print(message)
            text_message=message
            html_message=None
            image_path=None
            image_name=None

            # define function for sending email
            def send_email(subject, text_content, html_content=None, sender=sender, recipient=recipient, image_path=None, image_name=None):
                email = EmailMultiAlternatives(subject=subject, body=text_content, from_email=sender, to=recipient if isinstance(recipient, list) else [recipient])

                if all([html_content,image_path,image_name]):
                    email.attach_alternative(html_content, "text/html")
                    email.content_subtype = 'html'  # set primary content to be text/html
                    email.mixed_subtype = 'related' # it is important part that ensures embedding of image

                    with open(image_path, mode='rb') as f:
                        image = MIMEImage(f.read())
                        email.attach(image)
                        print("Image PATH")
                        print(image)
                        print(image_name)

                        image.add_header('Content-ID', f'<{image_name}>')

                email.send()


            # send test email
            send_email(subject=subject, text_content=text_message, html_content=html_message, sender=sender, recipient=recipient, image_path=image_path, image_name=image_name)
            #send sns
            cont={"status":True,
                  "message":"Sent email to  "+str(from_email)}
            print(cont)
            return Response((cont))




        #return render(request,'events_api/ticketTemplate.html', {'context': context,'order':order})
        except Exception as e:
            cont={"status":False,
                  "message":str(e)}
            return Response((cont))





# function to generate OTP
def genOTP() :

    # Declare a digits variable
    # which stores all digits
    digits = "0123456789"
    OTP = ""

    # length of password can be chaged
    # by changing value in range
    for i in range(4) :
        OTP += digits[math.floor(random.random() * 10)]

    return OTP

@csrf_exempt

@api_view(["POST"])
@permission_classes((AllowAny,))

def generate_otp(request):
    mobile = request.data.get("mobile")
    print(mobile)
    if mobile:
        otp = genOTP()
        print(otp)
        number="+91"+mobile


        seller=Seller.objects.filter(user__username=mobile).update(otp=otp)
        print(seller)
        if(seller):
            msg="Dear Seller, "+otp+ " is the SECRET OTP to authenticate your login to Collabo Reseller App."
            sms=SendMessage(number,msg)
            print(sms)
            return Response({'status': True,'otp':otp})
        else:


        #User.objects.create(mobile=mobile, otp=otp)
            return Response({'status': False,'message':"Invalid phone number"})


    else:
        return Response({'status':False,"message": 'Please provide valid number'})



@csrf_exempt

@api_view(['POST'])
@permission_classes((AllowAny,))
def UserLogin(request):
    mobile = request.data.get("mobile")
    country_prefix=request.data.get("country_prefix")
    print(mobile)
    try:
        if mobile:
            otp = genOTP()
            print(otp)
            number=country_prefix+mobile


            customer=Customer.objects.filter(user__username=number).update(otp=otp,phone=number)
            print("customer")
            print(customer)
            if(customer):
                msg="Dear Collabo User, "+otp+ " is the SECRET OTP to authenticate your user login to Collabo."
                sms=SendMessage(number,msg)
                print(sms)
                return Response({'status': True,'otp':otp})
            else:


                #User.objects.create(mobile=mobile, otp=otp)
                return Response({'status':False,"message":"Please sign up!","error_code":"E00"})


        else:
            return Response({'status':False,"message": 'Please provide valid number',"error_code":"E01"})
    except Exception as e:

        return Response({'status':False,"message": str(e),"error_code":"E01"})






@csrf_exempt

@api_view(["POST"])
@permission_classes((AllowAny,))

def SingUpGenOTP(request):
    mobile = request.data.get("mobile")
    display_name=request.data.get("display_name")
    country_prefix=request.data.get("country_prefix")



    print(mobile)
    try:
        user=None
        if mobile:
            otp = genOTP()
            print(otp)
            country_prefix=country_prefix
            number=country_prefix+mobile



            #seller=Seller.objects.filter(user__username=mobile).update(otp=otp)



            try:
                user = User.objects.filter(username=str(number)).exists()
                #cust = Customer.objects.filter(user__username=(mobile),first_name=display_name).exists()
                print(user)
                if(user):
                    user= User.objects.get(username=str(number))
                    print("reached here")
                    print(user)
                    user.is_customer=True
                    user.save()
                else:

                    #return Response({'status':False,"message": "User already exists with same phone number. Please login ! ","error_code":"E01"})
                    user = User.objects.create(username=str(number),password="userautopwd",first_name=display_name)
                #print(user)
            except Exception as e:
                user = User.objects.create(username=str(number),password="userautopwd",first_name=display_name)

            #return Response({'status':False,"message": "Customer already exists with same phone number ! ","error_code":"E01"})

            print("user")
            print(user)

            user.is_customer=True
            print("test")
            user.save()
            print("user saved")

            customer = Customer.objects.get(user__username=number)


            customer.otp=otp
            customer.display_name=display_name
            print("USEROTP")

            customer.phone=number
            customer.country_prefix=country_prefix
            customer.save()
            #user.save()



            if(user):
                msg="Dear User, "+otp+ " is the SECRET OTP to authenticate your login to Collabo Reseller App."
                sms=SendMessage(number,msg)
                print(sms)
                return Response({'status': True,'otp':otp})
            else:


                #User.objects.create(mobile=mobile, otp=otp)
                user.delete()

                return Response({'status': False,'message':"Invalid phone number"})


        else:
            return Response({'status':False,"message": 'Please provide valid number'})
    except Exception as e:
        if("not a valid phone number" in str(e)):
            user.delete()

        return Response({'status':False,"message": str(e),"error_code":"E02"})




class CheckTicket(APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        try:
            ticket_code =request.data.get('ticket_code')
            print(ticket_code)
            print(request.user)

            if ticket_code :
                try:
                    order=get_object_or_404(Orders,ticket_code=ticket_code)
                    city = order.event.city
                    tz_city = pytz.timezone(str(city.timezone1))
                    today = datetime.now(tz_city).replace(tzinfo=None)
                    print(today)


                    ord=Orders.objects.filter(Q(ticket_code=ticket_code) & Q (event__organizer__user=request.user) & Q (attended=False) & (Q(payment_status='PC') |(Q(payment_status='FE')))).count()
                    #Orders.objects.filter(id=orders.data["id"]).update(pm_order_id=razororder['id'],order_status="OC")
                    print("Order **********")
                    print(ord)
                    if(ord==0):
                        return Response({'status':False,"message": 'Ticket rejected, It can be any of the following reasons: 1. Already attended for this ticket, 2. Payment not done, 3. Event not for this organizer',"error_code":"E13"})
                    else:
                        items=OrderItems.objects.filter(Q(io_id=order.id))
                        print(items)
                        io_id=[]
                        for item in items:
                            io_id.append({"item_name":item.item_name,"count":item.count})
                        print(io_id)


                        return Response({'message': "Token Scan completed","status":True, "event":{"title":order.event.title,"customer":order.cust_name,"customer_phone":order.cust_phone,"cust_email":order.cust_email,"io_id":io_id,"slot_name":order.slot.title,"slot_start_time":order.slot.start_time,"slot_end_name":order.slot.end_time}})




                except Orders.DoesNotExist:
                    return Response({'status':False,"message": 'Ticket invalid',"error_code":"E11"})


            else:
                return Response({'message': "Please provide ticket code","status":False,"error_code":"E10"})



        except Exception as e:
            resp = {"status":False,"message": str(e),"error_code":"E00"}
            return Response(resp)



class ScanTicket(APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        try:
            ticket_code =request.data.get('ticket_code')
            print(ticket_code)
            print(request.user)

            if ticket_code :
                try:
                    order=get_object_or_404(Orders,ticket_code=ticket_code)
                    city = order.event.city
                    tz_city = pytz.timezone(str(city.timezone1))
                    today = datetime.now(tz_city).replace(tzinfo=None)
                    print(today)


                    ord=Orders.objects.filter(Q(ticket_code=ticket_code) & Q (event__organizer__user=request.user) & Q (attended=False) & (Q(payment_status='PC') |(Q(payment_status='FE')))).update(attended=True,scan_time=today)
                    #Orders.objects.filter(id=orders.data["id"]).update(pm_order_id=razororder['id'],order_status="OC")
                    print("Order **********")
                    print(ord)
                    if(ord==0):
                        return Response({'status':False,"message": 'Ticket rejected, It can be any of the following reasons: 1. Already attended for this ticket, 2. Payment not done, 3. Event not for this organizer',"error_code":"E13"})
                    else:
                        items=OrderItems.objects.filter(Q(io_id=order.id))
                        print(items)
                        io_id=[]
                        for item in items:
                            io_id.append({"item_name":item.item_name,"count":item.count})

                        resp={'message': "Token Scan completed","status":True, "event":{"title":order.event.title,"customer":order.cust_name,"customer_phone":order.cust_phone,"cust_email":order.cust_email,"io_id":io_id,"slot_name":order.slot.title,"slot_start_time":order.slot.start_time,"slot_end_name":order.slot.end_time}}


                except Orders.DoesNotExist:
                    return Response({'status':False,"message": 'Ticket invalid',"error_code":"E12"})


                return Response(resp)
            else:
                return Response({'status':False,"message": 'Please provide Ticket Code',"error_code":"E10"})



        except Exception as e:
            resp = {"status":False,"message": str(e),"error_code":"E00"}
            return Response(resp)



class verify_opt(APIView):
    authentication_classes = ()
    permission_classes = (AllowAny,)

    def post(self, request, *args, **kwargs):
        try:
            mobile =request.data.get('mobile')
            print(mobile)
            otp = request.data['otp']
            print(otp)

            if mobile and otp:
                try:
                    seller = Seller.objects.get(user__username=mobile, otp=otp)
                    print(seller)
                    user = User.objects.get(username=mobile,)
                    print(user)
                except Seller.DoesNotExist:
                    return Response({'status':False,"message": 'Invalid OTP'})

                token = Token.objects.get_or_create(user=user)

                print(token[0])
                return Response({'token': str(token[0]),"firstname":user.first_name,"status":True})
            else:
                return Response({'status':False,"message": 'Please provide required inputs'})


        except Exception as e:
            resp = {"status":False,"message": str(e)}
            return Response(resp)


class Logout(APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get(self, request, format=None):
        # simply delete the token to force a login
        print(request.user)
        request.user.auth_token.delete()
        resp={"status":True,"message":"User Logged out"}
        return Response(resp)

class user_verify_opt(APIView):
    authentication_classes = ()
    permission_classes = (AllowAny,)


    def post(self, request, *args, **kwargs):
        try:
            mobile =request.data.get('mobile')
            country_prefix =request.data.get('country_prefix')
            otp = request.data['otp']
            print(otp)
            number=country_prefix+mobile
            print(mobile)



            if number and otp:
                try:
                    customer = Customer.objects.get(user__username=number, otp=otp)
                    print(customer)
                    print(customer.user)
                    user=customer.user
                    #user = Customer.objects.get(username=customer)
                    print(user)
                    phone=customer.phone
                    #email


                except Customer.DoesNotExist:
                    return Response({'status':False,"message": 'Invalid OTP'})

                token = Token.objects.get_or_create(user=user)

                print(token[0])
                return Response({'token': str(token[0]),"display_name":customer.display_name,"username":user.username,"mobile":(user.username),"country_prefix":str(customer.country_prefix),"status":True})
            else:
                return Response({'status':False,"message": 'Please provide required inputs'})


        except Exception as e:
            resp = {"status":False,"message": str(e)}
            return Response(resp)



class resendOTPUser(APIView):
    authentication_classes = ()
    permission_classes = (AllowAny,)

    def post(self, request, *args, **kwargs):
        try:
            mobile =request.data.get('mobile')
            country_prefix=request.data.get('country_prefix')
            country_prefix=country_prefix
            number=country_prefix+mobile

            if mobile :
                try:

                    cust = Customer.objects.get(user__username=number,)
                    print(cust)
                    if(cust):
                        otp=cust.otp
                        print(otp)

                        msg="Dear Collabo User, "+otp+ "This is your one-time password."
                        sms=SendMessage(number,msg)
                        print(sms)
                        return Response({'status': True,'message':"otp sent successfully"})

                except Customer.DoesNotExist:
                    return Response({'status':False,"message": 'User not exists'})


            else:
                return Response({'status':False,"message": 'Please provide required inputs'})


        except Exception as e:
            resp = {"status":False,"message": str(e)}
            return Response(resp)


class resendOTPseller(APIView):
    authentication_classes = ()
    permission_classes = (AllowAny,)

    def post(self, request, *args, **kwargs):
        try:
            mobile =request.data.get('mobile')
            country_prefix=request.data.get('country_prefix')
            country_prefix=country_prefix
            number=country_prefix+mobile

            if mobile :
                try:

                    seller = Seller.objects.get(user__username=mobile,)
                    print(seller)
                    if(seller):
                        otp=seller.otp
                        print(otp)

                        msg="Dear Collabo Seller, "+otp+ "This is your one-time password."
                        sms=SendMessage(number,msg)
                        print(sms)
                        return Response({'status': True,'message':"otp sent successfully"})

                except Seller.DoesNotExist:
                    return Response({'status':False,"message": 'Seller not exists'})


            else:
                return Response({'status':False,"message": 'Please provide required inputs'})


        except Exception as e:
            resp = {"status":False,"message": str(e)}
            return Response(resp)



class hostlogin(APIView):
    authentication_classes = ()
    permission_classes = (AllowAny,)


    def post(self, request, *args, **kwargs):
        try:
            username =request.data.get('username')
            password =request.data.get('password')
            if username and password:
                try:
                    user = authenticate(username=username, password=password)
                    print("AUTH")
                    print(user)
                    if(user is  None):
                        return Response({'status':False,"message": 'Invalid username or password'})

                    #login(request, user)
                    #print(user)


                    cust = get_object_or_404(Host, user__username=user)
                    print(cust)


                except Host.DoesNotExist:
                    return Response({'status':False,"message": 'Invalid OTP'})

                token = Token.objects.get_or_create(user=user)

                print(token[0])
                return Response({'token': str(token[0]),"display_name":user.first_name,"username":user.username,"status":True})
            else:
                return Response({'status':False,"message": 'Please provide required inputs'})


        except Exception as e:
            resp = {"status":False,"message": str(e)}
            return Response(resp)


class HostCard(generics.ListAPIView):
    permission_classes = (IsAuthenticated,)
    #permission_classes = (AllowAny,)
    authentication_classes = (TokenAuthentication,)



    #serializer_class = SellerSerializer
    #serializer_class = EventHostSerializer
    serializer_class=HostEventSerializer
    pagination_class = LargeResultsSetPagination
    def get_queryset(self):
        try:

            """
            This view should return  list of all categories and its details
            """

            #queryset = Host.objects.filter(user=self.request.user)
            print(self.request.user)
            host=Host.objects.filter(user=self.request.user)
            queryset = Event.objects.filter(organizer=host[0])
            print(queryset)


        except Exception as e:
            raise APIException(detail=str(e))
        return (queryset)




class MyEarnings(generics.ListAPIView):
    permission_classes = (IsAuthenticated,)
    #permission_classes = (AllowAny,)
    authentication_classes = (TokenAuthentication,)



    #serializer_class = SellerSerializer
    serializer_class = EventSellerSerializer
    pagination_class = LargeResultsSetPagination
    def get_queryset(self):
        try:

            """
            This view should return  list of all categories and its details
            """

            seller = Seller.objects.get(user=self.request.user,)
            queryset=seller.event.all()

        except ValueError:
                raise APIException(detail='Custom message')
        return (queryset)
