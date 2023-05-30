from django.contrib import admin

# Register your models here.
from django.contrib import admin
from django.apps import apps
from events_api.models import Customer,Orders,OrderItems
from django.shortcuts import get_object_or_404, redirect, render
import csv
from django.http import HttpResponse

app = apps.get_app_config('events_api')


from django.contrib import admin
from django.contrib.admin import AdminSite

class MyAdminSite(AdminSite):
    site_header = 'Collano new Custom'

admin_site = MyAdminSite(name='myadmin')




class CustomerAdmin(admin.ModelAdmin):


    fieldsets = (
        ('Customer Details', {
            'fields': ('user', 'email_address',('phone','country_prefix'),
                       'bio','location','birth_date','exptime','is_previously_logged_in','otp','display_name')
        }),


        ('Subscription Details', {
            'fields': ('subscription','user_device')
        }),
        ('Follow Details', {
            'fields': ('follow_artist','follow_venue')
        }),
        ('Order Details', {
            'fields': ('orders',)
        }),


    )


    list_display = ['user','id','phone','exptime','display_name']
    search_fields = ['id',]
    list_filter = ['country_prefix']
    filter_horizontal = ['subscription','follow_artist','follow_venue','orders']
    def get_readonly_fields(self, request, obj=None):
        if request.user.is_superuser:
            return []
        elif obj:
            # obj is not None, so this is an edit
            return ['user','exptime','user_device','subscription','email_address','location','is_previously_logged_in','birth_date'] # Return a list or tuple of readonly fields' names
        else:
            # This is an addition
            return []

admin.site.register(Customer,CustomerAdmin)


class ExportCsvMixin:
    def export_as_csv(self, request, queryset):

        meta = self.model._meta
        field_names = [field.name for field in meta.fields]

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename={}.csv'.format(meta)
        writer = csv.writer(response)

        #writer.writerow(field_names)
        flag=0


        for obj in queryset:

            row=[getattr(obj, field) for field in field_names]
            heading=[]
            heading.extend(field_names)
            meta = OrderItems._meta
            qs=OrderItems.objects.filter(io_id=obj)
            field_names1 = [field.name for field in meta.fields]
            print("inside  heading")
            if(flag==0):
                heading.extend(field_names1)
                print(heading)
                writer.writerow(heading)
                print("**************")
                flag=1
            headingrow=[]
            headingrow.extend(row)

            for obj in qs:
                eachrow=[]
                eachrow.extend(headingrow)
                row=[getattr(obj, field) for field in field_names1]
                eachrow.extend(row)
                print(eachrow)
                writer.writerow(eachrow)


        #row = writer.writerow([field.count for field in qs])


        return response

    export_as_csv.short_description = "Export Selected"

@admin.register(Orders)
class OrdersAdmin(admin.ModelAdmin,ExportCsvMixin):

    fieldsets = (
        ('Order Details', {
            'fields': ('user', 'event',
                       'slot','ticket_code','ticket_type','order_no','is_order_seller','seller')
        }),


        ('Customer Details', {
            'fields': ('cust_name',
                       ('cust_email','cust_phone','phone_number'),)
        }),


        ('Payment Details', {
            'fields': ('payment_method','pm_order_id','pm_payment_id','grandtotal')
        }),


        ('Status', {
            'fields': ('order_status','payment_status','attended','scan_time')
        }),




    )




    list_display = ['event','id','cust_name','ticket_type','ticket_code', 'attended' ,'scan_time','payment_method','order_status','payment_status','pm_order_id','pm_payment_id','is_order_seller']
    search_fields = ['ticket_code','cust_name','order_no','id','pm_order_id','pm_payment_id','attended']
    list_filter = ['ordercreatedtime','event','is_order_seller','payment_status','order_status','seller','payment_method']
    actions = ["export_as_csv"]
    list_per_page = 250
    # def export_as_csv(self, request, queryset):
    #     meta = self.model._meta
    #     field_names = [field.name for field in meta.fields]
    #
    #     response = HttpResponse(content_type='text/csv')
    #     response['Content-Disposition'] = 'attachment; filename={}.csv'.format(meta)
    #     writer = csv.writer(response)
    #
    #     writer.writerow(field_names)
    #     for obj in queryset:
    #         row = writer.writerow([getattr(obj, field) for field in field_names])
    #
    #     return response
    #
    # export_as_csv.short_description = "Export Selected"



@admin.register(OrderItems)
class OrderItemsAdmin(admin.ModelAdmin,ExportCsvMixin):


    list_display = ['io_id','item_name','pc_cat','pc_slot','item_description','item_price','additional_charge','discounted_price','discount_rate','count']
    search_fields = ['item_name',]
    list_filter = ['pc_cat','pc_slot','io_id']
    actions = ["export_as_csv"]
    list_per_page = 250




# class CustomerAdmin(admin.ModelAdmin):
#
#     list_display = ['user','id','exptime','user_device',]
#     search_fields = ['id',]
#     list_filter = ['user_device']
#     filter_horizontal = ['bookmark']
#
#     def get_readonly_fields(self, request, obj=None):
#         if request.user.is_superuser:
#             return []
#         elif obj:
#             # obj is not None, so this is an edit
#             return ['user','exptime','user_device','bookmark','email_address','location','is_previously_logged_in','bio','birth_date'] # Return a list or tuple of readonly fields' names
#         else:
#             # This is an addition
#             return []
#
# admin.site.register(Customer,CustomerAdmin)

#
#
# @admin.register(Orders)
# class OrdersAdmin(admin.ModelAdmin):
#     list_display = ['user','saloon_name','id','cust_name',"cust_email"]
#     search_fields = ['saloon_name__name','id']
#     #list_filter = ['saloon_name']
#     def get_readonly_fields(self, request, obj=None):
#         if request.user.is_superuser:
#             return []
#         elif obj:
#             # obj is not None, so this is an edit
#             return ['user','saloon_name','id'] # Return a list or tuple of readonly fields' names
#         else:
#             # This is an addition
#             return []
#
#
#     #filter_horizontal = ['weekday']
#
#
#     def get_queryset(self, request):
#         if request.user.is_superuser:
#             print("Superuser")
#             return Orders.objects.all()
#         else:
#             print("NOT super user")
#             print(request.user.pk)
#             self.owner = get_object_or_404(Owners, owner=request.user.pk)
#             print("OWMERR")
#             print(self.owner.owner)
#             saloons=(Saloons.objects.filter(owner=self.owner))
#             list=[]
#             print(saloons)
#             for saloon in saloons:
#                 list.append(saloon)
#
#             print(list)
#
#
#
#             #get saloons of this particular owner
#
#             return Orders.objects.filter(saloon_name__in=list)
#
#     def save_model(self, request, obj, form, change):
#         if request.user.is_superuser:
#             obj.save()
#         else:
#             if getattr(obj, 'owners', None) is None:
#                 print(obj)
#                 print(request.user)
#                 print(request.user.pk)
#                 obj.owner = get_object_or_404(Owners, owner=request.user.pk)
#
#             obj.save()
#
#
#
#
# class OrderItemsAdmin(admin.ModelAdmin):
#
#     list_display = ['io_id','item_name','item_description','item_price','count']
#     search_fields = ['item_name','io_id__id',]
#
#     def get_readonly_fields(self, request, obj=None):
#         if request.user.is_superuser:
#             return []
#         elif obj:
#             # obj is not None, so this is an edit
#             return ['io_id','item_name','item_description','item_price','count'] # Return a list or tuple of readonly fields' names
#         else:
#             # This is an addition
#             return []
#
#
#     def get_queryset(self, request):
#         if request.user.is_superuser:
#             print("Superuser")
#             return OrderItems.objects.all()
#         else:
#             print("NOT super user")
#             print(request.user.pk)
#             self.owner = get_object_or_404(Owners, owner=request.user.pk)
#             print("OWMERR")
#             print(self.owner.owner)
#
#
#             saloons=(Saloons.objects.filter(owner=self.owner))
#             list=[]
#             print(saloons)
#             for saloon in saloons:
#                 list.append(saloon)
#
#             print(list)
#
#
#             orders=(Orders.objects.filter(saloon_name__in=list))
#             listorder=[]
#             print(orders)
#             for order in orders:
#                 listorder.append(order)
#
#             print(listorder)
#
#
#
#             #get saloons of this particular owner
#
#             return OrderItems.objects.filter(io_id__in=listorder)
#
#
#
# admin.site.register(OrderItems,OrderItemsAdmin)


for model_name, model in app.models.items():
    print(model)
    print(model_name)
    if  not (model_name =='orders' or model_name=='orderitems' or model_name=='customer'):
        #admin.site.register(model)
        admin_site.register(model)
# Register your models here.




