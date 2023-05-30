# from simple_mail.mailer import BaseSimpleMail, simple_mailer
#
#
# class WelcomeMail(BaseSimpleMail):
#     email_key = 'welcomeZartek'
#
#
# simple_mailer.register(WelcomeMail)
#
from datetime import date
from django.shortcuts import render
from qr_code.qrcode.utils import ContactDetail, WifiConfig, Coordinates, QRCodeOptions

#
from simple_mail.mailer import BaseSimpleMail, simple_mailer


class WelcomeMail(BaseSimpleMail):
    email_key = 'EventEmailTemplateCh'
    template = 'events_api/emailTemplate.html'


simple_mailer.register(WelcomeMail)


# from simple_mail.mailer import BaseSimpleMail, simple_mailer
# from .models import Customer
#
# class WelcomeMail(BaseSimpleMail):
#     email_key = 'welcomeTest'
#
#     def set_context(self, user_id, welcome_link):
#         user = Customer.objects.get(user=user_id)
#         print("User")
#         print(user)
#         self.context = {
#             'user': user,
#             'welcome_link': welcome_link
#         }
#
#
# simple_mailer.register(WelcomeMail)

from .models import Customer
from simple_mail.mailer import BaseSimpleMail, simple_mailer
class WelcomeMail(BaseSimpleMail):
    #email_key =
    email_key = 'EventEmailTemplateBackendChng'
    template = 'events_api/emailTemplate.html'
    #3,order, template
    def set_context(self,order, template):
        #user = Customer.objects.get(user=user_id)
        print("INSIDE TEMPLATE")
        print(template)
        print(order)
        self.context = dict(

            video_id='J9go2nj6b3M',

            options_example=QRCodeOptions(size='t', border=6, error_correction='L'),
        )


        self.context = {
            'order': order,
            'subject':"test",


            #'welcome_link': welcome_link
        }

    # def set_test_context(self):
    #     user_id = Customer.objects.order_by('?').first().id
    #     print(user_id)
    #     self.set_context(user_id, 'http://192.168.0.107:8000')
    #

simple_mailer.register(WelcomeMail)