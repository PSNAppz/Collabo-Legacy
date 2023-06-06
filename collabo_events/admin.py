from django.contrib import admin

# Register your models here.
from django.contrib import admin
from django.apps import apps

from collabo_events.forms import BannerForm, EventSellerInlineFormset

from collabo_events.models import Banner,Type, HomeBanner, User,PaymentMethod,Price_Category,Event,EventCategory,OfferGeo,Offer,Slot,Artist,CategoryImage,City,SlotPC,Host,Seller,HomeFeatureArtist,HomeFeatureVenue,HomeFeatureEvent,Document,ArtistImage,ArtistSong,ArtistGenre,VImage,Country,State,Choice,CustomText,EventSeller,CouponCode
#from saloonapi.models import Customer,Orders,BookingSaloon,OrderItems
from django.contrib.admin.views.main import ChangeList
#from collabo_events.forms import EventChangeListForm

from django.shortcuts import get_object_or_404, redirect, render
from django.core.exceptions import ValidationError
from django.db.models import Q
from django.contrib import messages

from django.contrib import admin
from django.contrib.admin.views.main import ChangeList
from django.conf import settings
import csv
from django.http import HttpResponse



from .models import Place, RoutePoint, Route,Venue1,Host,Facility
app = apps.get_app_config('collabo_events')


from django.contrib import admin
from django.contrib.admin import AdminSite





class MyAdminSite(AdminSite):
    site_header = 'Collano new Custom'

admin_site = MyAdminSite(name='myadmin')




class ImageInline(admin.TabularInline):
    #model = Event.categoryImage.through
    model=Venue1.upload.through
    extra=0
    can_delete = True
    show_change_link = True
    verbose_name = 'Image/Video Upload'
    verbose_name_plural = 'Image/Video Upload'



@admin.register(Venue1)
class Venue1Admin(admin.ModelAdmin):
    fieldsets = (
        ('Venue Details', {
            'fields': ('title','city',
                       'label','capacity',('rate','rate_type'),'slug','facilities')
        }),


        ('Location', {
            'fields': ( 'location',
                       )
        }),


        ('About', {
            'fields': ('about', 'type')
        }),







    )

    list_display = ( 'location','title','city','label','capacity','rate','rate_type','type','slug',)
    inlines = (ImageInline,)
    exclude = ('upload',)
    filter_horizontal = ['facilities']
    search_fields = ['title']
    list_filter = ['type','city','capacity']



    def position_map(self, instance):
        print("LOCATION")
        print(instance.location)
        if instance.location is not None:
            return '<img src="http://maps.googleapis.com/maps/api/staticmap?center=%(latitude)s,%(longitude)s&zoom=%(zoom)s&size=%(width)sx%(height)s&maptype=roadmap&markers=%(latitude)s,%(longitude)s&sensor=false&visual_refresh=true&scale=%(scale)s&key=%(key)s" width="%(width)s" height="%(height)s">' % {
                'latitude': instance.location.latitude,
                'longitude': instance.location.longitude,
                'key': getattr(settings, 'PLACES_MAPS_API_KEY'),
                'zoom': 15,
                'width': 100,
                'height': 100,
                'scale': 2
            }
    position_map.allow_tags = True


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    list_display = ('position_map', 'location')

    def position_map(self, instance):
        print("LOCATION")
        print(instance.location)
        if instance.location is not None:
            return '<img src="http://maps.googleapis.com/maps/api/staticmap?center=%(latitude)s,%(longitude)s&zoom=%(zoom)s&size=%(width)sx%(height)s&maptype=roadmap&markers=%(latitude)s,%(longitude)s&sensor=false&visual_refresh=true&scale=%(scale)s&key=%(key)s" width="%(width)s" height="%(height)s">' % {
                'latitude': instance.location.latitude,
                'longitude': instance.location.longitude,
                'key': getattr(settings, 'PLACES_MAPS_API_KEY'),
                'zoom': 15,
                'width': 100,
                'height': 100,
                'scale': 2
            }
    position_map.allow_tags = True


class RoutePointInline(admin.StackedInline):
    '''Stacked Inline View for RoutePoint model'''

    model = RoutePoint
    min_num = 1
    extra = 1


@admin.register(Route)
class RouteAdmin(admin.ModelAdmin):
    inlines = [RoutePointInline, ]


@admin.register(Type)
class TypeAdmin(admin.ModelAdmin):
    list_display = ['title',]





@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = [ 'name','id','state',]
    filter_horizontal = ('payment_method',)


#@admin.register(HomeBanner)
class HomeBannerAdmin(admin.ModelAdmin):
    list_display = [ 'id','image','title','event',]

admin.site.register(HomeBanner)

class HomeBannerInline(admin.TabularInline):
    model = Banner.event.through
    extra=0
    can_delete = True
    show_change_link =False


    verbose_name = 'Home Banner'
    verbose_name_plural='Home Banner'


@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    list_display = [ 'id','title',]
    filter_horizontal = ('event',)
    #form = BannerForm
    inlines = (HomeBannerInline,)
    exclude=('event',)

    #
    #
    #
    #
    #
    #
    # def formfield_for_choice_field(self, db_field, request, **kwargs):
    #     if db_field.name == 'domain':
    #         print(db_field.name)
    #
    #         return super().formfield_for_choice_field(db_field, request, **kwargs)
    # def get_changelist_form(self, request, **kwargs):
    #     print("sdsf")
    #     return BannerForm
    #
    #






@admin.register(State)
class StateAdmin(admin.ModelAdmin):
    list_display = [ 'name','id','country',]

@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = [ 'name','id','domain','country_code']



@admin.register(Price_Category)
class Price_CategoryAdmin(admin.ModelAdmin):
    list_display = [ 'id','title','price']

@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    list_display = [ 'id','uploaded_at','upload','image']


@admin.register(VImage)
class VImageAdmin(admin.ModelAdmin):
    list_display = [ 'id','image_name','upload']




@admin.register(ArtistGenre)
class ArtistGenreAdmin(admin.ModelAdmin):
    list_display = [ 'id','title']



@admin.register(Facility)
class FacilityAdmin(admin.ModelAdmin):
    list_display = [ 'id','name']















from django.contrib.auth.admin import UserAdmin


from django.contrib.auth.admin import UserAdmin

class UserAdmin(UserAdmin):
    model = User
    list_display = ['username','id','first_name']

    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('is_owner','is_host','is_customer','is_seller')}),
    )

admin.site.register(User, UserAdmin)

#
# @admin.register(User)
# class UserAdmin(UserAdmin):
#     list_display = [ 'username','email','is_owner','id','is_host','is_seller','is_customer']


@admin.register(EventCategory)
class EventCategoryAdmin(admin.ModelAdmin):
    list_display = ['category_id','name','weight','slug']




@admin.register(SlotPC)
class SlotPCAdmin(admin.ModelAdmin):
    list_display = ['event','slot','price_cat','seating_id','booked_seats','remaining_seats','limitCategory','limitSlot','totalSlot']
    search_fields = ['event__title','slot__title',]
    list_filter = ['event','remaining_seats',]





class EventChangeList(ChangeList):
    def __init__(self, request, model, list_display,
        list_display_links, list_filter, date_hierarchy,filter_horizontal,
        search_fields, list_select_related, list_per_page,
        list_max_show_all, list_editable, model_admin):
        super(EventChangeList, self).__init__(request, model,
                                            list_display, list_display_links, list_filter,
                                            date_hierarchy, search_fields, list_select_related,
                                            list_per_page, list_max_show_all, list_editable,
                                            model_admin)

        # these need to be defined here, and not in MovieAdmin
        self.list_display = ['title','slug','venue', 'ticket_type','category','start_time','end_time','totalSlot']
        self.list_display_links = ['title']
        self.list_editable = ['slot_time']
        self.filter_horizontal=['categoryImage','slot_time','pricing_category']
        self.fields = ('title','slug','venue','upload','location','Latitude','Longitude',('start_time','end_time'),'slot_time','ticket_type','category','categoryImage','pricing_category','content',)





class EventInline(admin.StackedInline):
    model = Event
    filter_horizontal = ('slot_time',)



admin.site.register(OfferGeo)

class GeoInline(admin.TabularInline):
    model = Offer.geo.through

@admin.register(Offer)
class OfferAdmin(admin.ModelAdmin):
    inlines = (GeoInline,)
    exclude = ('geo',) # Excluding field to hide unnecessary field, as mentioned in the docs

admin.site.register(Slot)

class SlotInline(admin.TabularInline):
    model = Event.slots.through
    extra=0
    can_delete = True
    show_change_link =False


    verbose_name = 'Time Slot'
    verbose_name_plural='Time Slot'









class CouponCodeInline(admin.TabularInline):
    model = Event.couponcode.through
    extra=0
    can_delete = True
    show_change_link = True
    verbose_name = 'Coupon Code'
    verbose_name_plural= 'Coupon Code'

class CustomFieldInline(admin.TabularInline):
    model = Event.custom_field.through
    extra=0
    can_delete = True
    show_change_link = True
    verbose_name = 'Custom Field'
    verbose_name_plural='Custom Field'

    #site_header="asasd"


class PriceCategoryInline(admin.TabularInline):
    model = Event.pricing_category.through
    extra=0
    can_delete = True
    show_change_link = True
    verbose_name = 'Pricing Category'
    verbose_name_plural='Pricing Category'

    site_header="asasd"










class categoryImageInline(admin.TabularInline):
    #model = Event.categoryImage.through
    model=Event.categoryImage.through
    extra=0
    can_delete = True
    show_change_link = True
    verbose_name = 'Image/Video Upload'
    verbose_name_plural = 'Image/Video Upload'








class ArtistImageInline(admin.TabularInline):
    #model = Event.categoryImage.through
    model=Artist.artistImage.through
    extra=0
    can_delete = True
    show_change_link = True
    verbose_name = 'Image/Video Upload'
    verbose_name_plural = 'Image/Video Upload'

class ArtistSongInline(admin.TabularInline):
    #model = Event.categoryImage.through
    model=Artist.artistSong.through
    extra=0
    can_delete = True
    show_change_link = True
    verbose_name = 'Image/Video Upload'
    verbose_name_plural = 'Image/Video Upload'




@admin.register(Artist)
class ArtistAdmin(admin.ModelAdmin):

    fieldsets = (
        ('Artist Details', {
            'fields': ('title','city', 'slug',
                       'fb_followers','inst_followers','rate','thumbnail','genre')
        }),





        ('About', {
            'fields': ('about',)
        }),







    )


    inlines = (ArtistImageInline,ArtistSongInline)
    exclude = ('artistSong','artistImage') # Excluding field to hide unnecessary field, as mentioned in the docs
    #fields = ('location','Latitude','Longitude',('event_start_time','event_end_time'),'ticket_type','category')

    list_display = ['title','id', 'fb_followers','inst_followers','rate','city','thumbnail','slug','genre']
    search_fields = ['title','id','genre']
    list_filter = ['city','genre','rate']


    class Media:
        css = {
            'all': ('collabo_events/css/custom_admin.css', )     # Include extra css
        }


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):

    fieldsets = (
        ('Event Details', {
            'fields': ('title','short_title','city','address_venue','artists',
                       'category','slug','lowest_price','organizer')
        }),

        ('Landscape Image ',{
            'fields':('image_original','image_medium','image_thumb')
        }),

        ('Event Details Advanced ',{
            'fields':('description','itinerary','cancellation_policy')
        }),


        ('Booking',{
            'fields':('booking_type','external_url','button_text')
        }),


        ('Event Timings', {
            'fields': ('ticket_type',
                      ('start_time','end_time'))
        }),




    )


    inlines = (SlotInline,PriceCategoryInline,categoryImageInline,CustomFieldInline,CouponCodeInline)
    exclude = ('slots','pricing_category','categoryImage','custom_field','couponcode') # Excluding field to hide unnecessary field, as mentioned in the docs
    #fields = ('location','Latitude','Longitude',('event_start_time','event_end_time'),'ticket_type','category')

    list_display = ['title','short_title','id','start_time','organizer','end_time','city', 'ticket_type','category','slug','lowest_price','organizer','address_venue']
    search_fields = ['title','slug']
    list_filter = ['ticket_type','artists','category','start_time','city','organizer']
    filter_horizontal = ['artists']


    class Media:
        css = {
            'all': ('collabo_events/css/custom_admin.css', )     # Include extra css
        }





    def render_change_form(self, request, context, *args, **kwargs):

        print("DSFDGFDHGFHG")

        print(context)

        for formset in context['inline_admin_formsets']:
            qs = formset.formset.queryset
            print("CHANGE FORM")
            print(qs)
            for model_obj in qs:
                print(model_obj)
                model_obj._hide = True

        return super(EventAdmin, self).render_change_form(request, context, *args, **kwargs)

    def response_add(self, request, new_object):
        print("RESPONSE ADD")

        obj = self.after_saving_model_and_slot_pricecategory_inlines(new_object)

        return super(EventAdmin, self).response_add(request, obj)


    def get_changeform_initial_data(self, request):
        """
        Get the initial form data from the request's GET params.
        """
        initial = dict(request.GET.items())

        for k in initial:
            print(k)



    def response_change(self, request, obj):
        obj = self.after_saving_model_and_slot_pricecategory_inlines(obj)

        return super(EventAdmin, self).response_change(request,obj)


            #SlotPC.objects.filter(slot=).update(billed=False)
            #o.delete()




    def after_saving_model_and_slot_pricecategory_inlines(self, obj):

        pcobj=obj.pricing_category.all()
        slotpc=SlotPC.objects.filter(event=obj)
        for spc in slotpc:
            if spc.price_cat in pcobj:
                pass
            else:
                print("Not Present in list")
                print(spc.price_cat)
                spc.delete()



        for slot in obj.slots.all():
            for pc in obj.pricing_category.all():
                try:
                     d, created = SlotPC.objects.get_or_create(
                         event=obj,
                         slot=slot,
                         price_cat=pc,
                         limitCategory=pc.max_size,
                         totalSlot=slot.max_size,



                     )

                     if(created==True):
                        print("Created")

                        qs=SlotPC.objects.filter(event=obj,slot=slot,price_cat=pc)
                        count=SlotPC.objects.filter(event=obj,slot=slot,price_cat=pc).count()
                        print(count)
                        if count == 1:
                            print("created only one rec")

                            d.limitCategory=pc.max_size
                            d.limitSlot=slot.max_size
                            print(d.limitCategory)
                            if(d.limitCategory is None):
                                d.remaining_seats=d.remaining_seats+ d.limitSlot
                            else:
                                d.remaining_seats=d.remaining_seats+d.limitCategory
                            d.booked_seats=d.booked_seats+0
                            d.totalSlot=slot.max_size
                            d.save()
                        else:
                            for item in qs:
                                if(str(item) == str(d.seating_id)):
                                    currentobj=item
                                else:
                                    prevobj=item
                                    item.delete()

                            d.booked_seats=prevobj.booked_seats

                            d.limitSlot=currentobj.totalSlot-d.booked_seats
                            if(d.limitCategory is None):
                                print("currentobj.limitSlot")
                                print(d.limitSlot)
                                d.remaining_seats=d.limitSlot
                            else:
                                d.remaining_seats=currentobj.limitCategory-d.booked_seats
                            d.save()
                     #updatelimiSlot
                     evslot=SlotPC.objects.filter(event=obj,slot=slot)
                     totalBooked=0
                     for evs in evslot:
                        totalBooked+=evs.booked_seats
                     for evs in evslot:
                        evs.limitSlot=evs.totalSlot-totalBooked
                        if(evs.limitCategory is None):
                            evs.remaining_seats=evs.limitSlot
                        evs.save()




                                # if(str(item) == str(d.seating_id)):
                                #     print("Current obj")
                                #     print(item)
                                #     # if(d.limitCategory is None):
                                #     #     d.remaining_seats=d.limitSlot
                                #     #     d.save()
                                #     # else:
                                #     #     d.remaining_seats=d.limitCategory
                                #     #     d.save()
                                #
                                #     d.limitSlot=d.totalSlot-d.booked_seats
                                #     if(d.limitCategory is None):
                                #         d.remaining_seats=d.limitSlot
                                #     else:
                                #         d.remaining_seats=d.limitCategory-d.booked_seats
                                #     d.save()
                                #
                                # else:
                                #     # print("Other Obj")
                                #     # print(item)
                                #     # d.booked_seats=item.booked_seats
                                #     # if(d.limitCategory is None):
                                #     #
                                #     #     d.remaining_seats=item.limitSlot
                                #     # else:
                                #     #     d.remaining_seats=d.limitCategory-d.booked_seats
                                #
                                #     #d.limitSlot=item.limitSlot
                                #     d.booked_seats=item.booked_seats
                                #     d.save()
                                #     #d.remaining_seats=d.remaining_seats-d.booked_seats
                                #     item.delete()


                     else:
                         print(d.totalSlot)


                         pass


                     print(d)

                except Exception as e:
                    print(e)












        # for slot in obj.slots.all():
        #     print(slot.pk)
        #     print("**********")
        #     for pc in obj.pricing_category.all():
        #
        #         try:
        #             d, created = SlotPC.objects.\(
        #                 event=obj,
        #                 slot=slot,
        #                 price_cat=pc,
        #                 limitCategory=pc.max_size,
        #                 limitSlot=slot.max_size,
        #
        #                )
        #
        #             #limitCategory=pc.max_size,
        #             #limitSlot=slot.max_size,
        #
        #
        #             if(created==True):
        #                 print("Created True")
        #                 qs=SlotPC.objects.filter(event=obj,slot=slot,price_cat=pc)
        #                 count=SlotPC.objects.filter(event=obj,slot=slot,price_cat=pc).count()
        #                 print("Count")
        #                 print(count)
        #                 if count == 1:
        #                     print("created only one rec")
        #                     d.limitSlot=slot.max_size
        #                     d.limitCategory=pc.max_size
        #                     d.remaining_seats=pc.max_size or slot.max_size
        #                     d.booked_seats=0
        #                     d.save()
        #                 else:
        #                     for item in qs:
        #                         if(str(item) == str(d.seating_id)):
        #                             d.save()
        #                         #d.limitCategory=item.limitCategory
        #                         #d.remaining_seats=item.remaining_seats
        #                         #d.limitSlot=slot.max_size
        #
        #
        #
        #                         else:
        #                             print("Booked Seats")
        #                             print(item)
        #                             print(item.booked_seats)
        #                             if(item.booked_seats!=0):
        #
        #
        #                                 d.remaining_seats=item.remaining_seats
        #                                 d.limitSlot=item.limitSlot
        #                                 d.save()
        #                             d.booked_seats=item.booked_seats
        #                             d.save()
        #                             item.delete()
        #
        #





                # except Exception as e:
                #     print(e)
        # now we have what we need here... :)
        return obj



class HostAdmin(admin.ModelAdmin):




    list_display = ['user','phone','id']
    search_fields = ['user','phone','event']
    list_filter = ['event','cust']
    filter_horizontal = ['cust','event']

    def get_cust(self, obj):
        print("OBJ")
        print(obj)
        return "\n".join([p for p in obj.cust.all()])

admin.site.register(Host,HostAdmin)




@admin.register(HomeFeatureEvent)
class HomeFeatureEventAdmin(admin.ModelAdmin):

    list_display = ['name','city','slug']
    search_fields = ['name','city','slug']
    list_filter = ['event','city']
    filter_horizontal = ('event',)

    class Media:
        #this path may be any you want,
        #just put it in your static folder
        js = ('admin/js/placeholder.js', )





@admin.register(HomeFeatureVenue)
class HomeFeatureVenueAdmin(admin.ModelAdmin):

    list_display = ['name','city','slug']
    search_fields = ['name','city','slug']
    list_filter = ['venue','city']
    filter_horizontal = ('venue',)

@admin.register(HomeFeatureArtist)
class HomeFeatureArtistAdmin(admin.ModelAdmin):

    list_display = ['name','city','slug']
    search_fields = ['name','city','slug']
    list_filter = ['artist','city']
    filter_horizontal = ('artist',)



@admin.register(CategoryImage)
class CategoryImagetAdmin(admin.ModelAdmin):

    list_display = ['category_type','category_name','upload']
    search_fields = ['category_name']


@admin.register(ArtistSong)
class ArtistSongAdmin(admin.ModelAdmin):

    list_display = ['image_name','upload','links']
    search_fields = ['image_name']

@admin.register(ArtistImage)
class ArtistImageAdmin(admin.ModelAdmin):

    list_display = ['image_name','upload']
    search_fields = ['image_name']


@admin.register(PaymentMethod)
class PaymentMethodAdmin(admin.ModelAdmin):

    list_display = ['name','slug']


@admin.register(EventSeller)
class EventSellerAdmin(admin.ModelAdmin):

    list_display = ['eventdetail','commission','show_change_link','id']
    filter_horizontal = ('order',)








class EventSellerInline(admin.TabularInline):
    model = Seller.event.through
    extra=0
    can_delete = True
    show_change_link = True
    verbose_name = 'Event for this seller'
    verbose_name_plural='Events for this seller'

    site_header="asasd"
    #formset = EventSellerInlineFormset




class ExportCsvMixin:
    def export_as_csv(self, request, queryset):

        meta = self.model._meta
        field_names = [field.name for field in meta.fields]

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename={}.csv'.format(meta)
        writer = csv.writer(response)

        writer.writerow(field_names)
        #field_names.append('get_event_commission()')
        print(field_names)



        for obj in queryset:



            #row = writer.writerow([getattr(obj, field) for field in field_names])
            row = writer.writerow([getattr(obj,field) for field in field_names])

            method=(getattr(obj,"get_event_commission"))
            print(method())

            #print(obj.get_event_commission())


            #",   ".join([ str(p.event)+"  " + str(p.commission) +" %" for p in self.event.all()])





        return response



    export_as_csv.short_description = "Export Selected"


@admin.register(Seller)
class SellerAdmin(admin.ModelAdmin,ExportCsvMixin):
    inlines = (EventSellerInline,)
    exclude = ("event",)

    list_display = ('user','phone', 'get_event_commission','ticket_sold')
    search_fields = ['user','event','phone',]
    list_filter = ['event',]
    filter_horizontal = ('event',)
    actions = ["export_as_csv"]
    list_per_page = 250
    csv_fields = list_display





class ChoiceInline(admin.TabularInline):

    model=Choice
    extra=0
    can_delete = True
    show_change_link = True

@admin.register(CustomText)
class CustomTextAdmin(admin.ModelAdmin):

    fieldsets = [
        (None, {'fields': ['select_text']}),

    ]
    inlines = [ChoiceInline,]
    exclude = ('choice',)



class CouponCodeAdmin(admin.ModelAdmin):
    list_display = ('code','rate',)



admin.site.register(CouponCode, CouponCodeAdmin)



for model_name, model in app.models.items():
    print(model)
    print(model_name)
    if not(model_name=='banner'  or model_name== 'type' or model_name=='homebanner' or model_name=='choicetext' or model_name=='paymentmethod' or model_name=='vimage' or model_name=='artistgenre' or model_name=='document' or  model_name=='artistimage' or model_name=='artistsong' or model_name=='homefeatureevent' or model_name=='homefeatureartist' or model_name=='homefeaturevenue' or model_name=='category'  or model_name=='item' or model_name=='user' or  model_name=='event'or model_name=='eventcategory' or model_name=='offer' or model_name=='offergeo' or model_name=='slot' or model_name=='artist' or model_name=='city'  or model_name=='price_category' or model_name=='slotpc' or model_name=='route'  or model_name=='place' or model_name=='venue1' or model_name=='seller' or model_name=='host'):
    #if not( model_name=='user' or model_name=='event'or model_name=='eventcategory'):

        #admin.site.register(model)
        admin_site.register(model)





