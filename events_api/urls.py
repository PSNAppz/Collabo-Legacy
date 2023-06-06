from django.urls import include, path
from django.urls import re_path as url

from django.conf.urls.static import static
from django.conf import settings
from . import api_views
from . import views
from django.urls import include
from qr_code import urls as qr_code_urls
urlpatterns = [



    url(r'^convert-token/?$', api_views.MyTokenView.as_view(), name="convert_token"),
    #url(r'^order', api_views.GenerateOrder.as_view(), name='order'),
    #url(r'^order', api_views.GenerateOrder1.as_view()),
    url(r'^test', api_views.order1, name="order1"),
    url(r'^order', api_views.GenerateOrderFun , name='order'),
    url(r'^sellerorder', api_views.GenerateOrderSellerFun , name='sellerorder'),
    url(r'^payment-fetch/$', api_views.PaymentFetch1.as_view()),
    url(r'^paymentfree/$', api_views.PaymentFree.as_view()),
    url(r'^sellerpayment/$', api_views.SellerPaymentFree.as_view()),
    url(r'^myearnings/$', api_views.MyEarnings.as_view()),

    #payfort APIS
    url(r'^generic-order', api_views.GenerateOrderGenericFun , name='generic_order'),
    url(r'^payfort/$', api_views.PaymentFort.as_view()),
    url(r'^payfortfinal/$', api_views.PayFortFinal.as_view()),

    #url(r'^ticket-code/(?P<ticket_code>[0-9A-Z]+)/$', TicketCodeView.TicketCode),
    url(r'^(?P<ticket_code>[0-9A-Z]+)/ticket-code/$', views.TicketCode,name='TicketCode' ),
    url(r'^ticket/$', api_views.TicketCodeJson.as_view(),name='ticket'),


    url(r'^login_success/?$', api_views.MyTokenView.as_view(), name="convert_token"),
    url(r'^mobilelogin/?$', api_views.MobileLogin.as_view(), name="mobilelogin"),

    url(r'^mobile/?$', api_views.generate_otp, name="mobile"),
    url(r'^verifyotp/?$', api_views.verify_opt.as_view(), name="verifyotp"),
    url(r'^sellerresendotp/?$', api_views.resendOTPseller.as_view(), name="resendsellerotp"),


    #user sign up
    url(r'^usersignup/?$', api_views.SingUpGenOTP, name="usersingup"),
    url(r'^userlogin/?$', api_views.UserLogin, name="userlogin"),

    #common for both  User Signup and login
    url(r'^userverifyotp/?$', api_views.user_verify_opt.as_view(), name="userverifyotp"),
    url(r'^resendotp/?$', api_views.resendOTPUser.as_view(), name="resendotp"),


    #host login
    url(r'^hostlogin/?$', api_views.hostlogin.as_view(), name="hostlogin"),

    url(r'^hostcard/$', api_views.HostCard.as_view()),
    url(r'^scanticket/$', api_views.ScanTicket.as_view(),name='scanticket'),
    url(r'^checkticket/$', api_views.CheckTicket.as_view(),name='checkicket'),

    url(r'^logout/', api_views.Logout.as_view()),











    url(r'^webhook/razorpay/order-paid/$', api_views.webhook1, name="webhook"),
    url(r'^getintouch/$', api_views.GetInTouch.as_view(),name='getintouch'),



    #url(r'^webhook/razorpay/order-paid1/$', api_views.webhook1, name="webhook1"),
    #url(r'^webhook/razorpay/payment-captured/$', api_views.webhookpayment, name="webhook")


]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


#old webhook https://testing.gocollabo.in/participation/webhooks/razorpay/order-paid/



#BHD and QAR