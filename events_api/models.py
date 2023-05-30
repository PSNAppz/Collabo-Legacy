from django.db import models

# Create your models here.

import uuid
from phonenumber_field.modelfields import PhoneNumberField

from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save,pre_save
# Create your models here.
from django.conf import settings

from rest_framework import exceptions

#from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

import sys
sys.path.append("..")

from collabo_events.models import User,Category,item,Event,SlotPC,Slot,Price_Category,Seller,Host,PaymentMethod,Artist,Venue1





class Customer(models.Model):
    USER_DEVICE = (
        ('N', None),
        ('ARD', 'ANDROID DEVICE'),
        ('IOS','IOS DEVICE'),


    )

    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    display_name=models.CharField(max_length=20,null=True,blank=True)
    email_address = models.EmailField(blank=True)
    phone = PhoneNumberField()
    country_prefix=models.CharField(max_length=5,default='+91')
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    exptime = models.DateTimeField(blank=True, null=True)
    is_previously_logged_in = models.BooleanField(default=False)
    subscription=models.ManyToManyField(Host,blank=True,null=True,related_name="events")
    user_device = models.CharField(choices=USER_DEVICE, max_length=128,default='N')
    follow_artist=models.ManyToManyField(Artist,blank=True,null=True,related_name="customer")
    follow_venue=models.ManyToManyField(Venue1,blank=True,null=True,related_name="customer")
    otp=models.CharField(max_length=4,null=True,blank=True)
    orders=models.ManyToManyField("Orders",blank=True,null=True,related_name="customer")








#
# def __str__(self):
#     return (str(self.user)+ str(self.user_id))

    def __str__(self):
        return (str(self.user))




@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_user_customer(sender, instance, created, **kwargs):
    if created and  instance.is_customer:
        print("create userciust")

        Customer.objects.create(user=instance)
#
@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def post_save_receiver(sender, instance,created, **kwargs):
    print(created)
    try:
        print("POST SAVE REC")

        if not Customer.is_previously_logged_in:
            print("save as cust")
            Customer.objects.create(user=instance)

            Customer.is_previously_logged_in = True
            instance.customer.save()

        elif instance.is_customer:
            print("CUST IS CUST")
            instance.customer.is_previously_logged_in = True
            print("CUST IS PREV")
            instance.customer.save()
            print("SAVES")
            print(instance.customer.is_previously_logged_in)
            print("saved")
    except Customer.DoesNotExist:
        #previous code
        # print("except")
        # Customer.objects.create(user=instance)
        # instance.customer.is_previously_logged_in = True
        # instance.customer.save()
        #previous cde end ************
        print("EXCEPTIONNN")


        try:
            Customer.objects.create(user=instance,email_address=instance.email or '')
            print("INSTANCE")
            print(instance)
            #instance.customer.is_previously_logged_in = True
            instance.customer.save()
            return True
        except Exception as e:

            content = {'mesage': str(e)}
            content.update({"status": False})

            raise exceptions.NotFound(detail=content)

    try:
        print("POST SAVE REC seller")

        if not Seller.is_previously_logged_in:
            print("save as cust in seller")
            Seller.objects.create(user=instance)

            Seller.is_previously_logged_in = True
            instance.seller.save()

        elif instance.is_seller:
            print("is selelr")
            instance.seller.is_previously_logged_in = True
            print("CUST IS PREV")
            instance.seller.save()
            print("SAVES")
            print(instance.seller.is_previously_logged_in)
            print("saved")
    except Seller.DoesNotExist:
        #previous code
        # print("except")
        # Customer.objects.create(user=instance)
        # instance.customer.is_previously_logged_in = True
        # instance.customer.save()
        #previous cde end ************
        print("EXCEPTIONNN")


        try:
            Seller.objects.create(user=instance)
            print("INSTANCE")
            print(instance)
            #instance.customer.is_previously_logged_in = True
            instance.seller.save()
            return True
        except Exception as e:

            content = {'mesage': str(e)}
            content.update({"status": False})

            raise exceptions.NotFound(detail=content)
    try:
        print("POST SAVE REC")

        if not Host.is_previously_logged_in:
            print("save as cust")
            Host.objects.create(user=instance)

            Host.is_previously_logged_in = True
            instance.host.save()

        elif instance.is_host:
            print("CUST IS CUST")
            instance.host.is_previously_logged_in = True
            print("CUST IS PREV")
            instance.host.save()
            print("SAVES")
            print(instance.host.is_previously_logged_in)
            print("saved")
    except Host.DoesNotExist:
        #previous code
        # print("except")
        # Customer.objects.create(user=instance)
        # instance.customer.is_previously_logged_in = True
        # instance.customer.save()
        #previous cde end ************
        print("EXCEPTIONNN")


        try:
            Host.objects.create(user=instance)
            print("INSTANCE")
            print(instance)
            #instance.customer.is_previously_logged_in = True
            instance.host.save()
            return True
        except Exception as e:

            content = {'mesage': str(e)}
            content.update({"status": False})

            raise exceptions.NotFound(detail=content)



class Meta:
    verbose_name_plural = 'Customer'









class OrderMethod(models.Model):
    pass

class Orders(models.Model):

    PAYMENT_CHOICES = (
        ('PP', 'Payment Pending'),
        ('PC', 'Payment Complete'),
        ('PF', 'Payment Failed'),
        ('FE', 'Free Events'),

    )
    ORDER_CHOICES = (
        ('OF', 'Order Failed due to errors'),
        ('OC', 'Order Created'),

    )

    PAYMENT_METHOD = (
        ('PAYTM', "PAYTM"),
        ('RAZORPAY', 'RAZOR PAY'),
        ('STRIPE','STRIPE'),


    )




    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL,blank=True,null=True)

    event = models.ForeignKey(Event,max_length=200,blank=True,null=True,on_delete=models.SET_NULL)
    slot=models.ForeignKey(Slot,blank=True,null=True,on_delete=models.SET_NULL)
    #event=models.ForeignKey(Slot,blank=True,null=True,on_delete=models.SET_NULL)



    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    ticket_code=models.CharField(max_length=6,null=True,blank=True)
    ticket_type=models.CharField(max_length=30,null=True,blank=True)

    is_order_seller=models.BooleanField(default=False,verbose_name="Booked Through Seller")
    seller = models.ForeignKey(Seller, on_delete=models.SET_NULL,blank=True,null=True)




#ticket_code = models.UUIDField(primary_key=True, default=uuid.uuid4().hex[:6].upper(), editable=False)

    order_no=models.CharField(max_length=100,blank=True,verbose_name="Receipt")
    cust_name=models.CharField(max_length=30, blank=True)
    cust_email=models.EmailField( blank=True)
    cust_phone=models.CharField(max_length=12,blank=True)
    phone_number = PhoneNumberField(blank=True)

    ordercreatedtime = models.DateTimeField(auto_now_add=True,)
    grandtotal=models.FloatField(default=0.00)
    pm_order_id=models.CharField(max_length=100,blank=True,verbose_name="PM Order Id ")
    #payment_method=models.CharField(choices=PAYMENT_METHOD,default='PAYTM',max_length=50)
    payment_method=models.ForeignKey(PaymentMethod,on_delete=models.SET_NULL,null=True,related_name='orders',blank=True)




    #items=models.ManyToManyField(OrderItems,on_delete=models.CASCADE,blank=True,null=True)
    #items = models.ManyToManyField(item )
    #total = models.FloatField(null=True, blank=True, default=None)

    #bookingtime = models.DateTimeField(blank=True, null=True)
    order_status = models.CharField(max_length=2,choices=ORDER_CHOICES, default='OF')
    payment_status=models.CharField(max_length=2,choices=PAYMENT_CHOICES,default='PP')
    pm_payment_id=models.CharField(max_length=100,blank=True,verbose_name="PM Payment Id")
    attended=models.BooleanField(default=False,verbose_name="Ticket Attended")
    scan_time = models.DateTimeField(blank=True, null=True)




    def __str__(self):
        return str(self.id)

        #return str(self.order_no) + " User: " + str(self.cust_name)+str(self.saloon_name)

    def short_desc(self):
        """Default short description visible on reservation button"""
        return str(self.id)


    def save(self, *args, **kwargs):
        if self.event is not None:
            print("TICKET_TYPE")
            self.ticket_type=self.event.get_booking_type_display()

            print((self.ticket_type))
        super(Orders, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'Order Event'



class OrderCustomText(models.Model):


    io_id=models.ForeignKey(Orders,on_delete=models.CASCADE,blank=True,null=True,related_name="ordercustomtext")


    answer = models.CharField(blank=True,null=True, max_length=20)


    def __str__(self):
        return str(self.io_id)
    class Meta:
        verbose_name_plural = 'Order Custom  Text'

class OrderItems(models.Model):


    io_id=models.ForeignKey(Orders,on_delete=models.CASCADE,blank=True,null=True,related_name="io_id")
    item_name = models.CharField(max_length=200)
    pc_cat=models.ForeignKey(Price_Category,blank=True,on_delete=models.SET_NULL,null=True)
    pc_slot=models.ForeignKey(SlotPC,blank=True,on_delete=models.SET_NULL,null=True)
    item_description = models.TextField(max_length=90)
    item_price = models.FloatField()
    additional_charge=models.FloatField(blank=True,default=0.0)
    discounted_price=models.FloatField(blank=True,null=True)
    discount_rate=models.PositiveIntegerField(blank=True, default=0)
    count = models.IntegerField(blank=True)


    def __str__(self):
        return str(self.io_id)
    class Meta:
        verbose_name_plural = 'Order Event Item'
        #return '{0} {1} {2}'.format(self.io_id,self.item_name, self.count)



# @receiver(post_save, sender=User)
# def save_user(sender, instance, **kwargs):
#     try:
#         print("saveiser")
#         #user = Customer.objects.get(user=instance.customer)
#         if Customer.objects.get(user=instance.user_name).DoesNotExist:
#             print("created as cust")
#             Customer.objects.create(user=instance)
#         else:
#             instance.customer.save()
#             print("saved")
#     except Customer.DoesNotExist:
#             print("custdoesnot exuis")
#             pass






#
#
# #
# @receiver(pre_save, sender=User)
# def check_email(sender, instance, **kwargs):
#     try:
#         usr = User.objects.get(email=instance.email)
#         if usr.username == instance.username:
#             pass
#         else:
#             raise ValidationError('Email already exists')
#     except User.DoesNotExist:
#         pass
#
#
#
# def get_first_name(self):
#     return self.first_name
#


