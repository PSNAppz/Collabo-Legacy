from django import forms
from django.forms import BaseInlineFormSet

from .models import Seller,Event,EventSeller,Host
from django.contrib.auth.forms import UserCreationForm
#from django.contrib.auth.models import User
from .models import User,Banner,Seller

class EventSellerInlineFormset(BaseInlineFormSet):
    def queryset(self, request):

        current = EventSeller.objects.all() # or whatever to get the current cycle
        print("current")
        print("current")
        qs = super(EventSellerInlineFormset, self).queryset(request)
        return qs.filter(school_class__cycle=current)



class SellerForm(forms.ModelForm):
    event = forms.ModelMultipleChoiceField(queryset=EventSeller.objects.all())

    class Meta:
        model = Seller
        #inlines = (EventSellerInlineFormset,)
        #exclude = ("event",)
        fields = '__all__'


class BannerForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        try:
            print(kwargs)
            print(args)
            domain = kwargs['instance'].domain
            print("INSIDE FORM")
            print(domain)
        except Exception as e:

            print("Exception")
            domain = 1
        super(BannerForm, self).__init__(*args, **kwargs)
        self.fields['event'].queryset = Event.objects.filter(city__state__country__domain=domain)
    class Meta:
        model = Banner
        #event=Seller.objects.filter(id=2)

        fields = ('title', 'domain','event')




class CustomItemForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        try:
            country = kwargs['instance'].country
        except KeyError:
            country = 1
        super(CustomItemForm, self).__init__(*args, **kwargs)
        self.fields['region'].queryset = Region.objects.filter(country=country)



class SellerEditForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        #id = kwargs.pop('id')
        print("IDDDD")
        #print(id)

        super(SellerEditForm, self).__init__(*args, **kwargs)

        #self.fields['event'].queryset=
        #self.fields['event'].queryset = EventSeller.objects.filter(id=2)




    #self.fields['title'].widget.attrs.update({'placeholder': 'sdsf'})

    def addPlaceholder(self, id):
        keys = Seller.objects.filter(id=id)
        #qs=Host.objects.filter(user=self.host.user).values_list('event')
        #print(qs)
        for item in keys:
            print("FORMS")
            print(item.event.all())
            print(self.data)

            #print(item['event__event_title'])

            self.fields['user'].widget.attrs.update({'placeholder': item.user})
            self.fields['phone'].widget.attrs.update({'placeholder': item.phone})
            #self.fields['event'].queryset=item.event.all()
            self.fields['event'].widget = forms.HiddenInput()
            #self.fields['event'].widget.attrs.update({'placeholder': item.event.all()})


    class Meta:
        model = Seller
        #event=Seller.objects.filter(id=2)

        widgets = {
            'user': forms.TextInput(attrs={'class': 'form-control form-control-line'}),
            'phone': forms.TextInput(attrs={'class': 'form-control form-control-line'}),
            #'event': forms.CheckboxSelectMultiple(attrs={'class': 'leaflet-control-layers-selector'}),
            'event': forms.HiddenInput(),
            'ticket_sold': forms.TextInput(attrs={'class': 'form-control form-control-line'}),
            #'tags':forms.MultipleChoiceField(attrs={'class': 'form-control form-control-line'}),
            #'ifile': forms.HiddenInput()


        }

        fields = ('user', 'phone','event','ticket_sold')





class SignUpForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        #id = kwargs.pop('id')
        print("IDDDD")
        #print(id)

        super(SignUpForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs.update({'class': 'form-control form-control-line', 'cols':'10'})
        self.fields['last_name'].widget.attrs.update({'class': 'form-control form-control-line', 'cols':'10'})
        self.fields['email'].widget.attrs.update({'class': 'form-control form-control-line', 'cols':'10'})
        self.fields['username'].widget.attrs.update({'class': 'form-control form-control-line', 'cols':'10'})
        self.fields['password1'].widget.attrs.update({'class': 'form-control form-control-line', 'cols':'10'})
        self.fields['password2'].widget.attrs.update({'class': 'form-control form-control-line', 'cols':'10'})
        self.fields['username'].widget.attrs.update({'placeholder': ""})
        print("static")

    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    #username = forms.CharField(max_length=30, required=False, help_text='Optional.')

    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    # widgets = {
    #     'first_name': forms.TextInput(attrs={'class': 'form-control form-control-line'}),
    #     'last_name': forms.TextInput(attrs={'class': 'form-control form-control-line'}),
    #     #'event': forms.CheckboxSelectMultiple(attrs={'class': 'leaflet-control-layers-selector'}),
    #
    #     'email': forms.TextInput(attrs={'class': 'form-control form-control-line'}),
    #     #'tags':forms.MultipleChoiceField(attrs={'class': 'form-control form-control-line'}),
    #     #'ifile': forms.HiddenInput()
    #
    #
    # }


    class Meta:
        model = User


        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2','is_seller','is_host' )