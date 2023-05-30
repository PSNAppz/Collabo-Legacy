from django.forms import inlineformset_factory
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.views.generic import TemplateView
from rest_framework.views import APIView

from collabo_events.admin import BannerAdmin
from collabo_events.models import Event,Banner,HomeBanner
from collabo_events.forms import *
from ..filters import UserFilter
from rest_framework.response import Response

from django.core import serializers
from ..forms import SellerEditForm


class SignUpView(TemplateView):
    template_name = 'registration/signup.html'


class jqueryserver1(BannerAdmin):


    def formfield_for_manytomany(self, db_field, *args, **kwargs):
        print ("in jqueryserver1dsdsd")
        response_string="hello"
        #request.POST._mutable = True
        #print(request.auth.application)

        #SAINA_APPLICATION_CLIENT_ID = getattr(settings, "SAINA_APPLICATION_CLIENT_ID", None)
        #print(SAINA_APPLICATION_CLIENT_ID)

        #request.POST['client_id']=SAINA_APPLICATION_CLIENT_ID
        try:
            response = super(jqueryserver, self).formfield_for_manytomany(db_field, *args, **kwargs)
        except Exception as e:

            cont={"sttaus":False,
                  "message":str(e),
                  }
        return response


def homefeatureeventcity(request, format=None, kwargs=None):
    print ("in jqueryserver asd")
    response_string="hello"
    if request.method == 'POST':
        if request.is_ajax()== True:
            import json

            print ("**ajax  **")
            for k,v in request.POST.items():
                print(k,v)
                if(k=='city'):
                    city=v

            print('Raw Data: "%s"' % request.body)
            print(city)
            qs= Event.objects.filter(city=city)
            data = serializers.serialize ( "json", qs )
            print(data)
            return HttpResponse(data, content_type="text/json" )



class SignUpView(TemplateView):
    template_name = 'registration/signup.html'


def sellerslist(request):
    template_name='collabo_events/home.html'
    page=1
    limit=4
    print('page', page)
    print('limit', limit)
    print("REQUEST GET METHOD")

    print(request.method)
    print(request.GET.get('event_title', None))
    #sellerlist = S()
    event_title=request.GET.get('event_title', None)
    #content = {'user_content': apiVdo.getList(page, limit)}
    #print(content['user_content']['rows'][0])
    return redirect('owners:sellerslistview',event_title=event_title)




def subscribers(request):
    template_name='collabo_events/home.html'
    page=1
    limit=4
    print('page', page)
    print('limit', limit)

    #sellerlist = S()
    #content = {'user_content': apiVdo.getList(page, limit)}
    #print(content['user_content']['rows'][0])
    return redirect('owners:subscribersview')


def userslist(request):
    template_name='collabo_events/home.html'
    page=1
    limit=4
    print('page', page)
    print('limit', limit)

    #sellerlist = S()
    #content = {'user_content': apiVdo.getList(page, limit)}
    #print(content['user_content']['rows'][0])
    return redirect('owners:userslistview')


    #return render(request,template_name,{'content':content, 'row': 4})

def addseller(request):
    if(request.method=='POST'):
        pass
    else:
        template_name='collabo_events/home.html'
        page=1
        limit=4
        print('page', page)
        print('limit', limit)
        print("REQUEST GET METHOD")

        print(request.method)
        print(request.GET.get('event_title', None))
        #sellerlist = S()
        event_title=request.GET.get('event_title', None)
        #content = {'user_content': apiVdo.getList(page, limit)}
        #print(content['user_content']['rows'][0])
    return redirect('owners:sellersaddlistview',event_title=event_title)


def addsellertoevent1(request):
    if(request.method=='POST'):
        pass
    else:
        template_name='collabo_events/home.html'
        page=1
        limit=4
        print('page', page)
        print('limit', limit)
        print("REQUEST GET METHOD")

        print(request.method)
        print(request.GET.get('event_title', None))
        #sellerlist = S()
        event_title=request.GET.get('event_title', None)
        #content = {'user_content': apiVdo.getList(page, limit)}
        #print(content['user_content']['rows'][0])
    return redirect('owners:sellersaddeventview',event_title=event_title)

def addsellertoevent(request):
    if request.method == 'POST':
        # POST, generate bound form with data from the request
        form = SellerForm(request.POST)
        #form=inlineformset_factory(Seller,EventSeller,fields=('event','commission'))
        # check if it's valid:
        if form.is_valid():
            # Insert into DB
            form.save()
            print("SA?VE FORM")
            # redirect to a new URL:
            return HttpResponseRedirect('/about/contact/thankyou')
    else:
        # GET, generate unbound (blank) form
        form = SellerForm()
        print("GET FORM")
    return render(request,'collabo_events/owners//addsellertoevent.html',{'form':form})

def editseller(request):
    if(request.method=='POST'):
        pass
    else:
        template_name='collabo_events/home.html'
        page=1
        limit=4
        print('page', page)
        print('limit', limit)
        print("REQUEST GET METHOD")

        print(request.method)
        print(request.GET.get('id', None))
        #sellerlist = S()
        id=request.GET.get('id', None)
        form = SellerEditForm()
        form.addPlaceholder(id)
        print('inside else')
        print(id)
        return render(request, 'collabo_events/owners/editsellers.html', {
            'form': form,'id':id,
        })
        #content = {'user_content': apiVdo.getList(page, limit)}
        #print(content['user_content']['rows'][0])



def home(request):


    if request.user.is_authenticated:
        if request.user.is_host:
            print("in view")
            print(request.user)
            return redirect('owners:quiz_change_list')
        elif request.user.is_superuser:
            print("in view")
            print(request.user)
            #return redirect('owners:admin_view')
            if request.method == 'POST':
                print("POST METHOD")
                form = SignUpForm(request.POST)
                if form.is_valid():
                    form.save()
                    username = form.cleaned_data.get('username')
                    raw_password = form.cleaned_data.get('password1')
                    user = authenticate(username=username, password=raw_password)
                    login(request, user)
                    return redirect('home')
            else:
                print("ELSE HOME")
                form = SignUpForm()
            return render(request, 'collabo_events/owners/createhost.html', {'form': form})

        else:
            print("not user")
            return redirect('operators:event_list')
    print("home ")
    return render(request, 'collabo_events/home.html')



from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect

from collabo_events.forms import SignUpForm

def signup(request):
    if request.method == 'POST':
        print("**sign up*****")
        form = SignUpForm(request.POST)
        form.save()
        return render(request, 'collabo_events/owners/createseller.html', {'form': form})
        # if form.is_valid():
        #     form.save()
        #     username = form.cleaned_data.get('username')
        #     raw_password = form.cleaned_data.get('password1')
        #     user = authenticate(username=username, password=raw_password)
        #     login(request, user)
        #     return redirect('home')
    else:
        form = SignUpForm()
        print("****else****")
    return render(request, 'collabo_events/owners/createseller.html', {'form': form})