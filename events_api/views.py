import base64

from django.shortcuts import render
from django.contrib import messages
import var_dump
from pprint import pprint
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.db.models import Count
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, ListView, UpdateView,TemplateView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import datetime
from.models import Orders,OrderItems
from django.views.decorators.csrf import csrf_exempt
from qr_code.qrcode.utils import ContactDetail, WifiConfig, Coordinates, QRCodeOptions
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.conf import settings
import re

from django.core.paginator import Paginator


@csrf_exempt
def TicketCode(request,ticket_code):
    item = get_object_or_404(Orders, ticket_code=ticket_code)
    try:


        oitems = OrderItems.objects.filter(io_id=item.id)
        grandtotal=float(item.grandtotal)/100
        orderdetails={"cust_name":item.cust_name,
                      "cust_email":item.cust_email,
                      "event":item.event,
                      "venue":item.event.address_venue,

                      "event_image":item.event.image_thumb.url,
                      "slot":item.slot,
                      "date_begin":item.slot.start_time.date(),

                      "begin":item.slot.start_time.time(),
                      "date_end":item.slot.end_time.date(),
                      "end":item.slot.end_time.time(),
                      "cust_phone":item.cust_phone,
                      "ticket_code":item.ticket_code,
                      "ticket_type":item.ticket_type,

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
        #html_message = render_to_string('events_api/ticketTemplate.html', {'context': context,'order':order})

        return render(request,'events_api/ticketTemplate.html', {'context': context,'order':order})
        #return render(request,'events_api/emailTemplate.html', {'context': context,'order':order})
    except Exception as e:
        return render(request,'events_api/TKT_NOT_FOUND.html')











def Generate(self,request):
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






class TicketCodeView(TemplateView):


    template_name = 'event_api/emailTemplate.html'
    print(template_name)






# Create your views here.
