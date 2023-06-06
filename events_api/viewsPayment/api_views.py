from django.http import HttpResponse
from rest_framework import status, generics
from drf_accountkit.views import LoginSuccess
from oauth2_provider.models import AccessToken
from rest_framework.response import Response
from django.conf import settings
from django.shortcuts import redirect
import bottle
from threading import Thread
import json
import requests
import re
from .sendSMS import SendMessage

from django.shortcuts import render
from qr_code.qrcode.utils import QRCodeOptions

import datetime as dtime
from datetime import datetime as DateTime, timedelta as TimeDelta
from datetime import datetime
from django.views.decorators.csrf import csrf_exempt
from .serializers import  EventOrderSerializer
from collabo_events.models import Event,User
from .viewsPayment.createorders import createRazorpayOrder,FetchRazorPayment,CapturePaymnet
from rest_framework.views import APIView
from .viewsPayment.RAZORAPISECRETS import RAZORPAY_API_SECRET,RAZORPAY_API_KEY
import razorpay
from django.core import serializers
from .mails import WelcomeMail

from rest_framework.permissions import IsAuthenticated,AllowAny
import sys
sys.path.append("..")
from .models import Orders,OrderItems,Slot,SlotPC,Price_Category
from datetime import date
from django.shortcuts import render
from qr_code.qrcode.utils import ContactDetail, WifiConfig, Coordinates, QRCodeOptions

from django.core import mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.core.exceptions import ValidationError


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






class GenerateOrder(generics.CreateAPIView):
    """
    Create an order from server
    """
    serializer_class = EventOrderSerializer

    permission_classes = (AllowAny,)

    def create(self, request, *args, **kwargs):
        self.serializer_class = EventOrderSerializer
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
            orders=super(GenerateOrder, self).create(request, *args, **kwargs)
            print("DONE here")
            print(orders.status_code)
            if(orders.status_code==201):

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
        except Exception as ValidationError:
            print(ValidationError)
            cont={"status":False,
                  "message":str(ValidationError)}
            return Response(cont)




class GenerateOrderRazorpay(GenerateOrder):
    def post(self, request, *args, **kwargs):


        return super(GenerateOrderRazorpay, self).post(request, *args, **kwargs)






@csrf_exempt
def GenerateOrderFun(request,*args, **kwargs):
    print("Donne")
    return GenerateOrderRazorpay.as_view()(request, *args, **kwargs)







def process_data(self,request):
    # do processing...
    #result = json.dumps(data)
    try:

        print('Finished processing')
        #print(result)
        ord=Orders.objects.filter(pm_order_id=request.data['pm_order_id'])
        for item in ord:
            oitems = OrderItems.objects.filter(io_id=item.id)
            grandtotal=float(item.grandtotal)/100
            orderdetails={"cust_name":item.cust_name,
                          "cust_email":item.cust_email,
                          "event":item.event,
                          "slot":item.slot,
                          "cust_phone":item.cust_phone,
                          "ticket_code":item.ticket_code,

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
        #print(filename)
        fh = open(filename, "wb")
        fh.write(base64.b64decode(data))
        fh.close()


        #print("Email has to send")



        template = 'events_api/emailTemplate.html'


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

        path="http://192.168.0.101:8000/api/ticket-code/A0562C/"
        message=" Congratulations! Your ticket for {0} on {1} has been confirmed. Ticket Code: {2}".format(item.event ,item.slot,item.ticket_code)
        number="+91"+item.cust_phone
        sms=SendMessage(number,message)


    except Exception as e:
        cont={"status":False,
          "message":str(e)}

        raise  Exception (cont)


    cont={"cont": str(order),
      "success":"Payment Completed succesfully","notify sms":sms,
      }


    return (Response(cont))









#######




class PaymentFetch1(APIView):

    authentication_classes = ()
    permission_classes = (AllowAny,)

    def post(self, request,*args, **kwargs):


        try:

            status=Orders.objects.filter(pm_order_id=request.data['pm_order_id']).values('payment_status')
            print(status[0]['payment_status'])
            if(status[0]['payment_status'])=="PC":
                cont={"status":False,
                      "message":"Payment Already Done"}
                raise ValueError(cont)

            print("BOOKED SEATS")
            ord=Orders.objects.filter(pm_order_id=request.data['pm_order_id'])
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



                razorpay_signature = request.data['razorpay_signature']
                content=""
                if razorpay_signature is not None and razorpay_signature != '':

                    try:
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
                else:
                    #Capture Payment
                        content=CapturePaymnet(request.data['pm_payment_id'],request.data['payment_amount'])


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
                Orders.objects.filter(pm_order_id=request.data['pm_order_id']).update(payment_status="PC", pm_payment_id=request.data['pm_payment_id'])
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





