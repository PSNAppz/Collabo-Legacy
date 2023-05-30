# do easy_install razorpay or
#    pip install razorpay

import razorpay
from django.conf import settings
from .RAZORAPISECRETS import RAZORPAY_API_SECRET,RAZORPAY_API_KEY
from django.http import HttpResponse

def createRazorpayOrder(orders):

    client=razorpay.Client(auth=(RAZORPAY_API_KEY,RAZORPAY_API_SECRET ))


    order_currency = 'INR'
    order_receipt = 'recept1'
    notes = {'key': 'value'}   # OPTIONAL

    DATA = {
        'amount': orders['grandtotal']  ,
        'receipt': orders['order_no'],
        'payment_capture': 1,
        'notes':notes,
        'currency':order_currency,

    }




    resp=(client.order.create(data=DATA))
    print(resp)
    print(DATA)
    return(resp)



# do easy_install razorpay or
#    pip install razorpay


def FetchRazorPayment(payment_id):


    client = razorpay.Client(auth=(RAZORPAY_API_KEY,RAZORPAY_API_SECRET))

    #payment_id = "pay_AtdLeRXapGyipw"

    resp = client.payment.fetch(payment_id)
    return (resp)



def CapturePaymnet(payment_id,payment_amount):


    client = razorpay.Client(auth=(RAZORPAY_API_KEY,RAZORPAY_API_SECRET))

    #payment_id = "pay_AtdLeRXapGyipw"

    resp = client.payment.capture(payment_id,payment_amount)
    return (resp)





