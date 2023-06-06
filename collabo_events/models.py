import math
import urllib.request
from PIL import Image as Img
from timezone_field import TimeZoneField

import datetime
#from events_api.models import Orders
from django.contrib.auth.models import AbstractUser
from django.contrib.gis.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save,pre_save,pre_delete
#from django.db import models
#from django.db import models
from django.contrib.postgres.fields import JSONField
from django.contrib import admin
from django.core.files.storage import default_storage as storage

from tinymce.models import HTMLField
from django.core.exceptions import ValidationError
from django.db.models.signals import m2m_changed
from django.utils.text import slugify
from django_unique_slugify import unique_slugify
import uuid
from places.fields import PlacesField
from django.utils import timezone


from django.core.files.storage import default_storage as storage

import sys
from rest_framework import exceptions


sys.path.append("..")


from ckeditor.fields import RichTextField


from django.conf import settings

from PIL import Image
import sys, time






class Place(models.Model):
    location = PlacesField(blank=True)

    def __unicode__(self):
        return self.location.place

    def __str__(self):
        return self.__unicode__()





class Route(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class RoutePoint(models.Model):
    name = models.CharField(max_length=50)
    location = PlacesField()
    route = models.ForeignKey(Route, on_delete=models.CASCADE)

    def __str__(self):
        return self.name





class User(AbstractUser):
    is_operator = models.BooleanField(default=False)
    is_owner = models.BooleanField(default=False)
    is_customer = models.BooleanField(default=False)
    is_seller = models.BooleanField(default=False)
    is_host = models.BooleanField(default=False)







class Owners(models.Model):
    owner = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)




    def __str__(self):
        return str(self.owner)


def user_directory_path(instance, filename):
    print(instance.owner)
    return 'user_{0}/item_{1}/{2}'.format(instance.owner,instance.item_name, filename)

class Country(models.Model):
    DOMAIN = (
        ('com', 'com'),
        ('in', 'in')
    )

    name = models.CharField(max_length=30,null=True,blank=True)
    country_code=models.CharField(max_length=5,null=True,blank=True)


    domain = models.CharField(choices=DOMAIN, max_length=10,editable=True,default='com')

    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = 'Countries'
    def save(self, *args, **kwargs):
        slug = "%s" % (self.name)
        if(slug=='india' or slug=='India'):
            self.domain='in'
        else:
            self.domain='com'

        super(Country, self).save(**kwargs)


class State(models.Model):
    name = models.CharField(max_length=30,null=True,blank=True)
    country=models.ForeignKey(Country, on_delete=models.SET_NULL,null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'States'


class PaymentMethod(models.Model):
    name=models.CharField(max_length=30,null=True,blank=True)
    slug=models.SlugField(blank=True,max_length=50,unique=True)

    def save(self, *args, **kwargs):
        slug = "%s" % (self.name)
        unique_slugify(self, slug)
        super(PaymentMethod, self).save(**kwargs)

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name_plural = 'Payment Method'





class City(models.Model):



    state = models.ForeignKey(State, on_delete=models.SET_NULL,null=True)
    name = models.CharField(max_length=30,null=True,blank=True)
    short_name=models.CharField(max_length=30,null=True,blank=True)
    slug=models.SlugField(max_length=100,blank=True,unique=True)
    payment_method=models.ManyToManyField(PaymentMethod,blank=True,null=True)
    timezone1 = TimeZoneField(default='Asia/Kolkata')
    #payment_method=models.CharField(choices=PAYMENT_METHOD,default='PAYTM',max_length=50)




    def __str__(self):
        return str(self.name)


    def save(self, *args, **kwargs):
        slug = "%s" % (self.name)
        unique_slugify(self, slug)
        super(City, self).save(**kwargs)
    class Meta:
        verbose_name_plural = 'Cities'




class item(models.Model):
    item_id = models.AutoField(primary_key=True,editable=False)
    owner=models.ForeignKey(Owners,on_delete=models.CASCADE)
    item_name=models.CharField(max_length=200)
    item_description=models.TextField(max_length=90)
    item_price=models.FloatField()
    upload = models.FileField(upload_to=user_directory_path)
    tax = models.PositiveIntegerField(blank=True, default=2)
    discounted_price=models.FloatField(blank=True,null=True)
    discount_rate=models.PositiveIntegerField(blank=True, default=0)
    duration=models.DurationField(blank=True,null=True)

    def __str__(self):
        return '{0}  {1}'.format(self.item_name, self.pk)
    class Meta:
        verbose_name_plural = 'Sub Category'


class itemAdmin(admin.ModelAdmin):
    readonly_fields = ('item_id',)



def user_directory_path_category(instance, filename):
    print(instance.owner)

    return 'user_{0}/Catagory_{1}/{2}'.format(instance.owner, instance.category_name,filename)


class Category(models.Model):
    owner = models.ForeignKey(Owners, on_delete=models.CASCADE)
    category_name = models.CharField(max_length=30)
    category_items = models.ManyToManyField(item, )
    upload = models.ImageField(upload_to=user_directory_path_category)

    def __str__(self):
        return (self.category_name)
    class Meta:
        verbose_name = ("Category")
        verbose_name_plural = 'Categories'





class Products(models.Model):
    name=models.CharField(max_length=50)
    def __str__(self):
        return str(self.name)





def user_directory_path_categoryimage(instance, filename):
    print(instance)
    print("user_directory_path_categoryimage")

    return 'Catagory_{0}/{1}'.format( instance.category_name,filename)

class CategoryImage(models.Model):


    CATEGORY_TYPE = (
        ('VDO', 'Video'),
        ('IMG', 'Image'),
    )


    category_type = models.CharField(choices=CATEGORY_TYPE, max_length=128, default='IMG')
    category_name = models.CharField(max_length=30)
    upload = models.FileField(upload_to=user_directory_path_categoryimage)

    def __str__(self):
        return (self.category_name)
    class Meta:
        verbose_name_plural = 'Category Image'



class ButtonText(models.Model):

    text = models.CharField(max_length=30)

    def __str__(self):
        return (self.text)
    class Meta:
        verbose_name = 'Button Text'


class EventCategory(models.Model):

    category_id= models.AutoField(primary_key=True)
    name=models.CharField(max_length=30)
    slug=models.SlugField(blank=True,max_length=50,unique=True)
    weight=models.IntegerField(default=0)


    def save(self, *args, **kwargs):
        slug = "%s" % (self.name)
        unique_slugify(self, slug)
        super(EventCategory, self).save(**kwargs)



    def __str__(self):
        return (self.name)
    class Meta:
        verbose_name_plural = 'Promotion Category'
        ordering = ['weight']






#testing mdels
class Genre(models.Model):
    name = models.CharField(max_length=250, unique=True)


class Movie(models.Model):
    name = models.CharField(max_length=250)
    genre = models.ManyToManyField(Genre)




class OfferGeo(models.Model):
    price = models.PositiveIntegerField()
    goal = models.PositiveIntegerField()

class Offer(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    geo = models.ManyToManyField(OfferGeo, related_name='offers')


class Price_Category(models.Model):

    title = models.CharField(max_length=30,null=True,blank=True)
    description = models.TextField(null=True,blank=True)
    price=models.FloatField(default=0.00)
    false_price=models.FloatField(default=0.00)
    #discounted_price=models.FloatField(null=True,blank=True)
    max_size=models.IntegerField(null=True,blank=True)
    additional_charge=models.FloatField(default=0.00)
    additional_charge_label= models.CharField(max_length=30,null=True,blank=True)
    #false_price=models.FloatField(null=True,blank=True)


    show_change_link = True





    def __str__(self):
        return '{0}     :{1}  '.format(self.title, self.price)


class Slot(models.Model):
    def validate_date(date):
        if date <  datetime.datetime.today():
            raise ValidationError("Date cannot be in the past")


    #event_id=models.OneToOneField(Event,unique=True)
    title=models.CharField(max_length=50,null=True,blank=True)
    start_time = models.DateTimeField(null=True,blank=True,)
    end_time = models.DateTimeField(null=True,blank=True,)
    max_size=models.PositiveIntegerField(default=1000)

    class Meta:
        verbose_name = 'SLOT'
        verbose_name_plural = 'SLOTS'




    def __str__(self):
        return '{0}:{1}  :{2} '.format(self.title, self.start_time ,self.pk)






##############

def user_directory_path_artistimage(instance, filename):

    return 'ArtistPhotos/{0}/{1}'.format( instance.image_name,filename)

class ArtistImage(models.Model):

    image_name = models.CharField(max_length=30,verbose_name="Photo Title")
    upload = models.FileField(upload_to=user_directory_path_artistimage,verbose_name="Upload Photo")


    def __str__(self):
        return (self.image_name)
    class Meta:
        verbose_name_plural = 'Artists Photos'


def user_directory_path_artistsong(instance, filename):

    return 'ArtistPhotos/{0}/{1}'.format( instance.image_name,filename)

class ArtistSong(models.Model):
    MEDIA_LINKS = (
        ('YT', 'Youtube'),
        ('SC', 'Soundcloud'),
        ('SF', 'Spotify'),
        ('MC', 'Mixcloud'),
        ('BC', 'Bandcamp'),
        ('BP', 'Beatport'),

     )



    image_name = models.CharField(max_length=30,verbose_name="Song Title")
    upload = models.URLField(blank=True,null=True,verbose_name="Paste Url")
    links=models.CharField(max_length=2,choices=MEDIA_LINKS,default='YT')
    #upload = models.FileField(upload_to=user_directory_path_artistsong)

    def __str__(self):
        return (self.image_name)
    class Meta:
        verbose_name_plural = 'Artists Songs'




def user_directory_artist(instance, filename):

    return 'Artist/{0}/{1}'.format( instance.title,filename)



class ArtistGenre(models.Model):
    title=models.CharField(max_length=30)


    def __str__(self):
        return (self.title)
    class Meta:
        verbose_name_plural = 'Artist Genre'


class Artist(models.Model):

    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=30)
    city=models.ForeignKey(City,on_delete=models.SET_NULL,null=True,related_name='artist')
    thumbnail=models.ImageField(upload_to=user_directory_artist,blank=True,null=True)
    slug=models.SlugField(max_length=100,blank=True,unique=True)


    fb_followers=models.IntegerField(blank=True,null=True)
    inst_followers=models.IntegerField(blank=True,null=True)
    genre = models.ForeignKey(ArtistGenre, on_delete=models.CASCADE,related_name='artist',blank=True,null=True)

    #city=models.ForeignKey(City,on_delete=models.CASCADE,default=6)
    #artist_city=models.ForeignKey(City,on_delete=models.SET_NULL,null=True,related_name='artist')


    rate=models.FloatField(blank=True,null=True)
    about = HTMLField(blank=True,null=True)

    artistSong=models.ManyToManyField(ArtistSong,related_name='artists',verbose_name="ArtistSong")
    artistImage=models.ManyToManyField(ArtistImage,related_name='atrists',verbose_name="Artists Photos and videos")

    def __str__(self):
        return (self.title)
    class Meta:
        verbose_name_plural = 'Artists'


    def save(self, *args, **kwargs):
        print("address_json")
        #self.slug = slugify(self.title)
        #print(self.artist_address)
        slug = "%s" % (self.title)
        unique_slugify(self, slug)


        super(Artist, self).save(*args, **kwargs)





#############

def user_directory_path_venueimage(instance, filename):

    return 'VenuePhotos/{0}/{1}'.format( instance.image_name,filename)


class Type(models.Model):
    title=models.CharField(max_length=30)



    def __str__(self):
        return (self.title)
    class Meta:
        verbose_name_plural = 'Venue Type'





class VImage(models.Model):

    image_name = models.CharField(max_length=30,blank=True)
    upload = models.FileField(upload_to=user_directory_path_venueimage,)

    def __str__(self):
        return (self.image_name)
    class Meta:
        verbose_name_plural = 'Venue Photos'


class Facility(models.Model):
    name=models.CharField(max_length=100)

    def __str__(self):
        return '{0}'.format(self.name)


    class Meta:
        verbose_name_plural = 'Facility'



class Venue1(models.Model):
    RATE_TYPE = (
        ('d', 'Day'),
        ('h', 'Hour')
    )

    location = PlacesField(blank=True)
    title = models.CharField(max_length=30,blank=True,null=True)
    label=models.TextField(max_length=500,blank=True,null=True)
    city=models.ForeignKey(City,on_delete=models.SET_NULL,null=True,related_name='venue1')
    slug=models.SlugField(max_length=100,blank=True,unique=True)


#city=models.ForeignKey(City,on_delete=models.CASCADE,blank=True)

    capacity=models.IntegerField(blank=True,null=True)
    rate=models.FloatField(blank=True,null=True)
    rate_type = models.CharField(choices=RATE_TYPE, max_length=10, default='d')
    about = HTMLField(blank=True,null=True)
    type = models.ForeignKey(Type, on_delete=models.CASCADE,related_name='venue1',blank=True,null=True)
    upload=models.ManyToManyField(VImage,related_name='venue1',verbose_name="Venue Photos",blank=True)
    facilities=models.ManyToManyField(Facility,related_name='venue',blank=True)

    class Meta:
        verbose_name_plural = 'Venue'





    def __unicode__(self):
            return self.location.place

    def __str__(self):
        return self.__unicode__()

    def save(self, *args, **kwargs):
        #self.slug = slugify(self.title)
        slug = "%s" % (self.title)
        unique_slugify(self, slug)
        super(Venue1, self).save()








def filepath(instance, filename):

    return '{0}/event_{1}'.format( instance.title,filename)








class CustomText(models.Model):

    select_text = models.CharField(max_length=200)
    def __str__(self):
        return self.select_text

    def save(self, *args, **kwargs):

        super(CustomText, self).save(*args, **kwargs)


class CouponCode(models.Model):

    code = models.CharField(max_length=6)
    rate=models.PositiveIntegerField(default=0)
    def __str__(self):
        return self.code

    def save(self, *args, **kwargs):

        super(CouponCode, self).save(*args, **kwargs)



class Choice(models.Model):

    cust_text = models.ForeignKey(CustomText, on_delete=models.CASCADE,related_name='choice')
    choice_text = models.CharField(max_length=200)

    def __str__(self):
        return str(self.cust_text)


class Event(models.Model):
    def validate_date(date):
        print(date)
        print(datetime.datetime.today())
        if date <  datetime.datetime.today():
            raise ValidationError("Date cannot be in the past")


    SCHEDULE_TICKET = (
        ('S', 'Single Ticket'),
        ('M', 'Multiple Ticket')
    )
    BOOKING_TYPE = (
        ('B', 'Bookable'),
        ('NB', 'External/Non-Bookable'),
        ('P',"Promotion/URL"),
    )
    title = models.CharField(max_length=60)
    now = str(int(time.time()))
    #filepath='Events/'+now+'/'
    category = models.ForeignKey(EventCategory, on_delete=models.CASCADE,related_name='events')


    id = models.AutoField(primary_key=True)




    short_title=models.CharField(max_length=30,null=True,blank=True)
    slug = models.SlugField(max_length=100,blank=True,unique=True)

    city=models.ForeignKey(City,on_delete=models.SET_NULL,null=True,related_name='events')

    address_venue=models.ForeignKey(Venue1, on_delete=models.SET_NULL,default="",blank=True,null=True)
    artists=models.ManyToManyField(Artist,related_name="events",verbose_name="Artists Name", blank=True,null=True)
    description = HTMLField(blank=True,null=True)
    #host=models.ForeignKey('Host',blank=True,null=True)

    itinerary=HTMLField(blank=True,null=True)
    organizer=models.ForeignKey("Host",on_delete=models.SET_NULL,blank=True,null=True,related_name="Host",verbose_name="Host")

    cancellation_policy=HTMLField(blank=True,null=True,)

    booking_type = models.CharField(choices=BOOKING_TYPE, max_length=128, default='B')
    external_url=models.URLField(null=True,blank=True)
    button_text=models.ForeignKey(ButtonText,on_delete=models.CASCADE,related_name='events',blank=True,null=True)
    categoryImage=models.ManyToManyField(CategoryImage,related_name='events',verbose_name="Category Image")

    #image_original = models.FileField('original file upload', upload_to=filepath,default='')
    image_original = models.FileField(upload_to=filepath,blank=True,null=True)
    image_medium = models.FileField(upload_to=filepath,blank=True,null=True)
    image_thumb = models.FileField(upload_to=filepath,blank=True,null=True)
    start_time = models.DateTimeField(null=True,blank=True)
    end_time = models.DateTimeField(null=True,blank=True)
    #start_time = models.DateTimeField(null=True,blank=True,validators=[validate_date])
    #end_time = models.DateTimeField(null=True,blank=True,validators=[validate_date])

    slots=models.ManyToManyField(Slot,related_name='events',verbose_name="Slot time")
    ticket_type = models.CharField(choices=SCHEDULE_TICKET, max_length=128, default='S')
    pricing_category=models.ManyToManyField(Price_Category,related_name='events',editable=True,)
    lowest_price=models.FloatField(default=0.00)
    custom_field=models.ManyToManyField(CustomText,related_name='events',editable=True,)
    couponcode=models.ManyToManyField(CouponCode,related_name='events',editable=True,)


# def get_thumb(self):
    #     return "/media/%s" % self.image_thumb
    #
    # def get_medium(self):
    #     print("sdsdg")
    #     print("/media/%s" % self.image_medium)
    #     return "/media/%s" % self.image_medium
    #
    # def get_original(self):
    #     #print( "/media/%s" % self.photo_original)
    #     return "/media/%s" % self.image_original


    def save(self, *args, **kwargs):
        print("address_json")
        self.slug = slugify(self.title)
        sizes = {'thumbnail': {'height': 100, 'width': 100}, 'medium': {'height': 300, 'width': 300},}





        if(self.image_original):
            print("SAVEIMAGE")
            original_image=self.image_original

            image = Image.open(original_image)
            (w, h) = image.size
            r900 = 900.0/w
            im900 = image.resize((int(math.floor(r900*w)), int(math.floor(r900*h))), Image.ANTIALIAS)
            rgb_im900 = im900.convert('RGB')
            rgb_im900.save(self.image_original,'jpeg')

            r350 = 350.0/w
            im350 = image.resize((int(math.floor(r350*w)), int(math.floor(r350*h))), Image.ANTIALIAS)
            rgb_im350 = im350.convert('RGB')
            rgb_im350.save(self.image_medium,'jpeg')

            r120 = 120.0/w
            im120 = image.resize((int(math.floor(r120*w)), int(math.floor(r120*h))), Image.ANTIALIAS)
            rgb_im120 = im120.convert('RGB')
            rgb_im120.save(self.image_thumb,'jpeg')



    #self.image_thumb=self.image_original
        super(Event, self).save()

        # size = 500, 500
        # print("image")
        # print(self.image_original.name)
        # image = Image.open(self.image_original)
        # image.thumbnail(size, Image.ANTIALIAS)
        # fh = storage.open(self.image_original.name, "w")
        # image.save(fh)
        # fh.close()
        #
        #
        # imagepath = str(self.image_original)  # this returns the full system path to the original file
        # extension = imagepath.rsplit('.', 1)[1]  # the file extension
        # filename = imagepath.rsplit('/', 1)[1].rsplit('.', 1)[0]  # the file name only (minus path or extension)
        # fullpath = imagepath.rsplit('/', 1)[0]  # the path only (minus the filename.extension)
        #
        # # use the file extension to determine if the image is valid before proceeding
        # if extension not in ['jpg', 'jpeg', 'gif', 'png',]: sys.exit()
        #
        # tsize = 300, 1500
        # im = Image.open(self.image_original)
        # im.thumbnail(tsize, Image.ANTIALIAS)
        # medname = filename + "_" + str(sizes['medium']['width']) + "x" + str(sizes['medium']['height']) + ".jpg"
        # print(fullpath + '/' + medname)
        # print("--------")
        #
        # fh = storage.open(fullpath + '/' + medname, "w")
        # im.save(fh)
        # fh.close()
        # print("Done")
        # self.image_thumb=fullpath + '/' + medname

        #im.save(fullpath + '/' + medname)


        # # create thumbnail
        # im.thumbnail((sizes['thumbnail']['width'], sizes['thumbnail']['height']), Image.ANTIALIAS)
        # thumbname = filename + "_" + str(sizes['thumbnail']['width']) + "x" + str(sizes['thumbnail']['height']) + ".jpg"
        # im.save(fullpath + '/' + thumbname)
        # self.image_thumb = self.filepath + thumbname




        #Function to save Slot

        print("PPPPPPPPPPPP ORGANIZER")
        if(self.organizer):
            qs=Host.objects.filter(event__exact=self)
            for i in qs:
                i.event.remove(self)



            qs=Host.objects.filter(id__exact=self.organizer.id)
            print(qs)
            for i in qs:
                i.event.add(self)

        super(Event, self).save(*args, **kwargs)

    def __str__(self):
        return '{0}'.format(self.title)


    class Meta:
        verbose_name_plural = 'Promotion Events'
        ordering = ['category']








def user_directory_path_header(instance, filename):
    return 'saloon_header/{0}'.format(filename)

class SlotPC(models.Model):
    event=models.ForeignKey(Event,on_delete=models.CASCADE,related_name='slot_event',null=True)
    slot=models.ForeignKey(Slot,on_delete=models.SET_NULL,null=True,)
    price_cat=models.ForeignKey(Price_Category,on_delete=models.SET_NULL,null=True)
    booked_seats=models.PositiveIntegerField(default=0,null=True,blank=True)
    remaining_seats=models.PositiveIntegerField(default=0,null=True,blank=True)
    limitCategory=models.PositiveIntegerField(default=0,null=True,blank=True,verbose_name="Total Category Seats")
    limitSlot=models.PositiveIntegerField(default=0,null=True,blank=True,verbose_name="Remaining Slot Seats")
    totalSlot=models.PositiveIntegerField(default=0,verbose_name="Total Slot Seats")

    seating_id = models.UUIDField(primary_key=True, default=uuid.uuid4,)



    def __str__(self):
        return '{0}'.format(self.seating_id)


    class Meta:
        verbose_name_plural = 'SLOTPC'



class Seo_Footer(models.Model):
    FOOTER_TYPE = (
        ('I', 'Internal'),
        ('E', 'External')
    )

    city=models.ForeignKey(City,on_delete=models.SET_NULL,null=True,)
    seo_title= models.CharField(max_length=30)
    seo_keyword= models.CharField(max_length=30)

    seo_description=models.TextField(max_length=100,null=True,blank=True)
    footer_title= models.CharField(max_length=30)
    footer_type= models.CharField(choices=FOOTER_TYPE,default="I",max_length=32)
    footer_url=models.URLField(max_length=100,null=True,blank=True)
    def __str__(self):
        return '{0}     :{1}  '.format(self.seo_title, self.footer_title)

    def save(self, *args, **kwargs):
        if not self.seo_description:
            print(self.seo_description)

            self.seo_description="Discover and book concerts, stand up comedies, workshops, sports and other activities in " +str( self.city ) +"  on Collabo."
            print((self.seo_description))
        super(Seo_Footer, self).save(*args, **kwargs)




class EventSeller(models.Model):

    eventdetail = models.ForeignKey(Event,on_delete=models.SET_NULL,null=True)
    commission = models.FloatField(null=True)
    show_change_link = True
    order=models.ManyToManyField("events_api.Orders",related_name='order',null=True,blank=True)


    def __str__(self):
        return '{0}     :{1}  '.format(self.eventdetail, self.commission)


class Seller(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,related_name="seller")
    phone = models.CharField(max_length=10, blank=True)
    event = models.ManyToManyField(EventSeller,blank=True,null=True,related_name='seller')
    ticket_sold=models.PositiveIntegerField(default=0,)
    otp=models.CharField(max_length=5,blank=True)
    is_previously_logged_in=models.BooleanField(default=False)

    #bookmark=models.ManyToManyField(Saloons,blank=True,null=True,related_name="saloonss")

    def __str__(self):
        return (str(self.user))



    def get_event_commission(self):
        print("test")
        return ",   ".join([ str(p.eventdetail)+"  " + str(p.commission) +" %" for p in self.event.all()])










#

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_user_seller(sender, instance, created, **kwargs):
    if created and  instance.is_seller:
        print("create seller")
        Seller.objects.create(user=instance)
        instance.seller.save()
        return True

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def post_save_receiver(sender, instance,created, **kwargs):
    print(created)
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

class Meta:
    verbose_name_plural = 'Seller'






class Host(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    phone = models.CharField(max_length=10, blank=True)
    details=HTMLField(blank=True,null=True)
    event=models.ManyToManyField(Event,null=True,blank=True)
    cust=models.ManyToManyField('events_api.Customer',null=True,blank=True,related_name='+',verbose_name='Subscribers')
    is_previously_logged_in=models.BooleanField(default=False)
    #code=models.
    #event = models.ForeignKey(Event,on_delete=models.SET_NULL,blank=True,null=True,)
    #commission = models.FloatField(null=True)
    #bookmark=models.ManyToManyField(Saloons,blank=True,null=True,related_name="saloonss")

    def __str__(self):
        return (str(self.user))


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_user_host(sender, instance, created, **kwargs):
    if created and  instance.is_host:
        print("create host")
        Host.objects.create(user=instance)
        instance.host.save()
        return True

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def post_save_receiver(sender, instance,created, **kwargs):
    print(created)
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
    verbose_name_plural = 'Host'




#




class HomeFeatureEvent(models.Model):

    #category_id= models.AutoField(primary_key=True)
    name=models.CharField(max_length=30)
    slug=models.SlugField(blank=True,max_length=50,unique=True)
    city=models.ForeignKey(City,on_delete=models.SET_NULL,related_name='homefeature',null=True)
    event=models.ManyToManyField(Event,null=True,related_name="homefeatureevent"  )
    #weight=models.IntegerField(default=0)


    def save(self, *args, **kwargs):
        slug = "%s" % (self.name)
        unique_slugify(self, slug)
        super(HomeFeatureEvent, self).save(**kwargs)



    def __str__(self):
        return (self.name)
    class Meta:
        verbose_name_plural = 'Home Feature Event'





class HomeFeatureArtist(models.Model):

    #category_id= models.AutoField(primary_key=True)
    name=models.CharField(max_length=30)
    slug=models.SlugField(blank=True,max_length=50,unique=True)
    city=models.ForeignKey(City,on_delete=models.SET_NULL,related_name='hfartist',null=True)
    artist=models.ManyToManyField(Artist,null=True  )
    #weight=models.IntegerField(default=0)


    def save(self, *args, **kwargs):
        slug = "%s" % (self.name)
        unique_slugify(self, slug)
        super(HomeFeatureArtist, self).save(**kwargs)



    def __str__(self):
        return (self.name)
    class Meta:
        verbose_name_plural = 'Home Feature Artist'


class HomeFeatureVenue(models.Model):

    #category_id= models.AutoField(primary_key=True)
    name=models.CharField(max_length=30)
    slug=models.SlugField(blank=True,max_length=50,unique=True)
    city=models.ForeignKey(City,on_delete=models.SET_NULL,related_name='hfvenue',null=True)
    venue=models.ManyToManyField(Venue1,null=True  )
    #weight=models.IntegerField(default=0)


    def save(self, *args, **kwargs):
        slug = "%s" % (self.name)
        unique_slugify(self, slug)
        super(HomeFeatureVenue, self).save(**kwargs)



    def __str__(self):
        return (self.name)
    class Meta:
        verbose_name_plural = 'Home Feature Venue'




def user_directory_path_header(instance, filename):

    return 'collabo_banner/{0}'.format(filename)

class HomeBanner(models.Model):


    #models.OneToOneField(Owners, on_delete=models.CASCADE)
    image = models.ImageField(upload_to=user_directory_path_header)
    title=models.CharField(max_length=100, blank=True)
    #message=models.CharField(max_length=100, blank=True)
    #rate = models.IntegerField(primary_key=True)
    event=models.ForeignKey(Event, on_delete=models.CASCADE,)


    def __str__(self):
        return (self.title)
    class Meta:
        verbose_name_plural = 'Home Banner'

class Banner(models.Model):
    DOMAIN = (
        ('com', 'com'),
        ('in', 'in')
    )

    title = models.CharField(max_length=30,)

    domain = models.CharField(choices=DOMAIN, max_length=10,editable=True,default='com')
    event=models.ManyToManyField(HomeBanner,related_name='banner')



    def __str__(self):
        return str(self.title)
    class Meta:
        verbose_name_plural = 'Banner'

class ArtistBanner(models.Model):


    #models.OneToOneField(Owners, on_delete=models.CASCADE)
    image = models.ImageField(upload_to=user_directory_path_header)
    title=models.CharField(max_length=100, blank=True)
    #message=models.CharField(max_length=100, blank=True)
    #rate = models.IntegerField(primary_key=True)
    artist=models.ForeignKey(Artist, on_delete=models.CASCADE,)


    def __str__(self):
        return (self.title)
    class Meta:
        verbose_name_plural = 'Artist Banner'



class VenueBanner(models.Model):


    #models.OneToOneField(Owners, on_delete=models.CASCADE)
    image = models.ImageField(upload_to=user_directory_path_header)
    title=models.CharField(max_length=100, blank=True)
    #message=models.CharField(max_length=100, blank=True)
    #rate = models.IntegerField(primary_key=True)
    venue=models.ForeignKey(Venue1, on_delete=models.CASCADE,)


    def __str__(self):
        return (self.title)
    class Meta:
        verbose_name_plural = 'Venue Banner'




class Document(models.Model):
    uploaded_at = models.DateTimeField(auto_now_add=True)
    upload = models.FileField()
    image=models.ImageField(upload_to=user_directory_path_header)
