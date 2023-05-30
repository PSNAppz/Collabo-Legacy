from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.db.models import Avg, Count
from django.forms import inlineformset_factory
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import (CreateView, DeleteView, DetailView, ListView,
                                  UpdateView)
from django.views import View

from ..decorators import owner_required
#from ..forms import BaseAnswerInlineFormSet, QuestionForm, OwnerSignUpForm
from ..models import EventSeller,Owners,Host,Seller
from events_api.models import Customer,Orders


# class OwnerSignUpView(CreateView):
#     model = User
#     form_class = OwnerSignUpForm
#     template_name = 'registration/signup_form.html'
#
#     def get_context_data(self, **kwargs):
#         kwargs['user_type'] = 'owner'
#         return super().get_context_data(**kwargs)
#
#     def form_valid(self, form):
#         user = form.save()
#         login(self.request, user)
#         return redirect('owner:quiz_change_list')


# @method_decorator([login_required, owner_required], name='dispatch')
# class QuizListView(ListView):
#     #model = Saloons
#     #ordering = ('name', )
#     #context_object_name = 'saloons'
#
#     #return render(request,template_name,{'content':content, 'row': 4})
#
#     #template_name = 'collabo_events/index.html'
#
#     #return render(request, template_name, {'documents': documents, })
#
#     def get(self, request, *args, **kwargs):
#         template_name = 'collabo_events/owners/quiz_change_list.html'
#         documents = Saloons.objects.all()
#         print(documents)
#         #form = self.form_class(initial=self.initial)
#         return render(request, template_name, {'documents': documents, })



#@method_decorator([login_required, owner_required], name='dispatch')
@method_decorator([login_required,], name='dispatch')
class QuizListView(ListView):
    model = Host
    ordering = ('ticket_sold', )
    fields=('user','ticket_sold','phone')
    context_object_name = 'host'
    template_name = 'collabo_events/owners/saloon.html'
    print("QuizListView Owners")

    def get_queryset(self):
        self.host = get_object_or_404(Host, user=self.request.user)
        print("GET queryset")
        print(self.host.user)
        queryset = Host.objects.filter(user=(self.host.user))
        print(queryset)
        #queryset1 = Saloons.objects.get(owner=self.owner)
        #object = super(Saloons, self).get_object(owner=self.owner)
        #print(object)

        for item in queryset:
            print(item.user)
            print(item.phone)

            for i in item.event.all():
                print(i)

            #print(item.item_description)
            #print(item.item_price)

        print(queryset)
        #print(queryset1)
        return queryset






@method_decorator([login_required,], name='dispatch')
class AdminView(ListView):
    model = Host
    ordering = ('ticket_sold', )
    fields=('user','ticket_sold','phone')
    context_object_name = 'host'
    template_name = 'collabo_events/owners/createhost.html'
    print("QuizListView Owners")

    def get_queryset(self):
        self.host = get_object_or_404(Host, user=self.request.user)
        print("GET queryset")
        print(self.host.user)
        queryset = Host.objects.filter(user=(self.host.user))
        print(queryset)
        #queryset1 = Saloons.objects.get(owner=self.owner)
        #object = super(Saloons, self).get_object(owner=self.owner)
        #print(object)

        for item in queryset:
            print(item.user)
            print(item.phone)

            for i in item.event.all():
                print(i)

            #print(item.item_description)
            #print(item.item_price)

        print(queryset)
        #print(queryset1)
        return queryset


@method_decorator([login_required,], name='dispatch')
class SellerListView(ListView):
    model = Seller
    ordering = ('ticket_sold', )
    fields=('user','ticket_sold','phone')
    context_object_name = 'sellerslist'
    template_name = 'collabo_events/owners/saloonseller.html'
    print("QuizListView Owners")
    lookup_url_kwarg = "event_title"
    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['event_title'] = self.request.GET.get('event_title')
        print(self.request.GET.get('event_title'))
        return ctx


    def get_queryset(self,*args, **kwargs):
        self.host = get_object_or_404(Host, user=self.request.user)
        print("GET SellerListView")

        event_title=self.kwargs.get(self.lookup_url_kwarg)
        print(event_title)
        if(event_title == 'None'):
            print("Event title none")

            event = Host.objects.filter(user=self.host.user).values_list('event')
            print(event)
            event_title = Host.objects.filter(user=self.host.user).values('event__title')
            event_title=[event_title,]
            print(event_title)
            print("Event title")
        else:

        #print(self.host.user)
            #event = Host.objects.filter(user=self.host.user).values_list('event')
            #event_title = Host.objects.filter(user=self.host.user).values('event__title')
            print("event_title is not None")
            event = Host.objects.filter(user=self.host.user,event__title=event_title).values_list('event')
            print(event)
            event_title=[event_title,]

        queryset = Seller.objects.filter(event__eventdetail__in=event).values('user__username','phone','event__eventdetail__title', 'event__commission')
        print(queryset)
        event_title = Host.objects.filter(user=self.host.user).values('event__title')
        print(event_title)
        #queryset1 = Saloons.objects.get(owner=self.owner)
        #object = super(Saloons, self).get_object(owner=self.owner)
        #print(object)

        for item in queryset:
            pass
            #print("ITEM")
            #print(item)
            #print(item['user__username'])


            #for i in item.event.all():
            #print(i)

            #print(item.item_description)
            #print(item.item_price)

        #print(queryset1)
        queryset={"seller":(queryset)   ,
                  "event":(event_title)}
        print(queryset)

        return queryset


@method_decorator([login_required,], name='dispatch')
class SellerAddEventView(ListView):

    model = Seller
    ordering = ('ticket_sold', )
    fields=('user','ticket_sold','phone')
    context_object_name = 'addseller'
    template_name = 'collabo_events/owners/addsellertoevent.html'
    print("QuizListView Owners")
    lookup_url_kwarg = "event_title"
    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['event_title'] = self.request.GET.get('event_title')
        print(self.request.GET.get('event_title'))
        return ctx


    def get_queryset(self,*args, **kwargs):
        self.host = get_object_or_404(Host, user=self.request.user)
        print("GET SellerListView")

        event_title=self.kwargs.get(self.lookup_url_kwarg)
        print(event_title)
        if(event_title == 'None'):

            event = Host.objects.filter(user=self.host.user).values_list('event')
            event_title = Host.objects.filter(user=self.host.user).values('event__title')
        else:

            #print(self.host.user)
            #event = Host.objects.filter(user=self.host.user).values_list('event')
            #event_title = Host.objects.filter(user=self.host.user).values('event__title')
            print("event_title is not None")
            event = Host.objects.filter(user=self.host.user,event__title=event_title).values_list('event')
            print(event)
            event_title=[event_title,]

        queryset = Seller.objects.filter(event__event__in=event).values('user__username','phone','event__event__title','event__commission','ticket_sold','id')
        #print(queryset)
        event_title = Host.objects.filter(user=self.host.user).values('event__title')
        #queryset1 = Saloons.objects.get(owner=self.owner)
        #object = super(Saloons, self).get_object(owner=self.owner)
        #print(object)

        for item in queryset:
            pass
            #print("ITEM")
            #print(item)
            #print(item['user__username'])


            #for i in item.event.all():
            #print(i)

            #print(item.item_description)
            #print(item.item_price)

        #print(queryset1)
        queryset={"seller":(queryset)   ,
                  "event":(event_title)}
        print(queryset)

        return queryset


@method_decorator([login_required,], name='dispatch')
class SellerAddListView(ListView):
    model = Seller
    ordering = ('ticket_sold', )
    fields=('user','ticket_sold','phone')
    context_object_name = 'addseller'
    template_name = 'collabo_events/owners/addseller.html'
    print("QuizListView Owners")
    lookup_url_kwarg = "event_title"
    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['event_title'] = self.request.GET.get('event_title')
        print(self.request.GET.get('event_title'))
        return ctx


    def get_queryset(self,*args, **kwargs):
        self.host = get_object_or_404(Host, user=self.request.user)
        print("GET SellerListView Add seller")

        event_title=self.kwargs.get(self.lookup_url_kwarg)
        print(event_title)
        if(event_title ==  "None"):
            print("event_title is  None")
            event = Host.objects.filter(user=self.host.user).values_list('event')
            print(event[0])
            print(event[0])
            event_title = Host.objects.filter(user=self.host.user).values('event__title')
            print(event_title)
        else:

            #print(self.host.user)
            #event = Host.objects.filter(user=self.host.user).values_list('event')
            #event_title = Host.objects.filter(user=self.host.user).values('event__title')

            event = Host.objects.filter(user=self.host.user,event__title=event_title).values_list('event')
            print(event)
            event_title=[event_title,]

        queryset = Seller.objects.filter(event__eventdetail__in=event).values('user__username','phone','event__eventdetail__title','event__commission','ticket_sold','id')
        #print(queryset)
        event_title = Host.objects.filter(user=self.host.user).values('event__title')
        #queryset1 = Saloons.objects.get(owner=self.owner)
        #object = super(Saloons, self).get_object(owner=self.owner)
        #print(object)

        for item in queryset:
            pass
            #print("ITEM")
            #print(item)
            #print(item['user__username'])


            #for i in item.event.all():
            #print(i)

            #print(item.item_description)
            #print(item.item_price)

        #print(queryset1)
        queryset={"seller":(queryset)   ,
                  "event":(event_title)}
        print(queryset)

        return queryset

@method_decorator([login_required,], name='dispatch')
class SellerEditListView(ListView):
    model = Seller
    ordering = ('ticket_sold', )
    fields=('user','ticket_sold','phone')
    context_object_name = 'addseller'
    template_name = 'collabo_events/owners/addseller.html'
    print("QuizListView Owners")
    lookup_url_kwarg = "id"



    def get_queryset(self,*args, **kwargs):
        self.host = get_object_or_404(Host, user=self.request.user)
        print("GET SellerListView")

        id=self.kwargs.get(self.lookup_url_kwarg)
        print(id)
        event_title=""
        print(event_title)
        if(event_title == 'None'):

            event = Host.objects.filter(user=self.host.user).values_list('event')
            event_title = Host.objects.filter(user=self.host.user).values('event__title')
        else:

            #print(self.host.user)
            #event = Host.objects.filter(user=self.host.user).values_list('event')
            #event_title = Host.objects.filter(user=self.host.user).values('event__title')
            print("event_title is not None")
            event = Host.objects.filter(user=self.host.user,event__title=event_title).values_list('event')
            print(event)
            event_title=[event_title,]

        queryset = Seller.objects.filter(event__event__in=event).values('user__username','phone','event__event__title','event__commission','ticket_sold','id')
        #print(queryset)
        event_title = Host.objects.filter(user=self.host.user).values('event__title')
        #queryset1 = Saloons.objects.get(owner=self.owner)
        #object = super(Saloons, self).get_object(owner=self.owner)
        #print(object)

        for item in queryset:
            pass
            #print("ITEM")
            #print(item)
            #print(item['user__username'])


            #for i in item.event.all():
            #print(i)

            #print(item.item_description)
            #print(item.item_price)

        #print(queryset1)
        queryset={"seller":(queryset)   ,
                  "event":(event_title)}
        print(queryset)

        return queryset


@method_decorator([login_required,], name='dispatch')
class SellerListView1(ListView):
    model = Seller
    ordering = ('ticket_sold', )
    fields=('user','ticket_sold','phone')
    context_object_name = 'sellerslist'
    template_name = 'collabo_events/owners/saloonseller.html'
    print("QuizListView Owners")

    def get_queryset(self,*args, **kwargs):
        self.host = get_object_or_404(Host, user=self.request.user)
        print("GET SellerListView")
        #print(self.host.user)
        #event = Host.objects.values('event').get(user=(self.host.user))
        event_title=[]

        if 'event_title' in self.kwargs:
            print("EVENT TITLE")
            #print(self.kwargs['event_title'])

            event=[18]
            event_title.append(str(self.kwargs['event_title']))

        else:
            print("HAS NOT EVENT TITLE ")


            event = Host.objects.filter(user=self.host.user).values_list('event')
            event_title = Host.objects.filter(user=self.host.user).values('event__title')
            #print(event_title)
            #print(event)


        queryset = Seller.objects.filter(event__event__in=event).values('user__username','phone','event__event__title','event__commission','ticket_sold')
        #print(queryset)

        #queryset1 = Saloons.objects.get(owner=self.owner)
        #object = super(Saloons, self).get_object(owner=self.owner)
        #print(object)

        for item in queryset:
            print("ITEM")
            #print(item)
            #print(item['user__username'])


            #for i in item.event.all():
                #print(i)

            #print(item.item_description)
            #print(item.item_price)

        #print(queryset1)
        queryset={"seller":(queryset)   ,
                  "event":(event_title)}
        #print(queryset)

        return queryset



@method_decorator([login_required,], name='dispatch')
class UserListView(ListView):
    model = Orders
    ordering = ('ticket_sold', )
    fields=('user','ticket_sold','phone')
    context_object_name = 'userslist'
    template_name = 'collabo_events/owners/ceusers.html'
    print("QuizListView Owners")

    def get_queryset(self):
        self.host = get_object_or_404(Host, user=self.request.user)
        print("GET UserListView")
        print(self.host.user)
        #event = Host.objects.values('event').get(user=(self.host.user))
        event = Host.objects.filter(user=self.host.user).values_list('event')

        print("EVENT")
        print(event)
        queryset = Orders.objects.filter(event__in=event).values('user__username','cust_name','cust_email','cust_phone','event__title')
        print(queryset)

        #queryset1 = Saloons.objects.get(owner=self.owner)
        #object = super(Saloons, self).get_object(owner=self.owner)
        #print(object)

        for item in queryset:
            print("ITEM")
            if (item['user__username']==None):
                item['user__username']="Guest"

        return queryset


@method_decorator([login_required,], name='dispatch')
class SubscribersView(ListView):
    model = Orders
    ordering = ('ticket_sold', )
    fields=('user','ticket_sold','phone')
    context_object_name = 'userslist'
    template_name = 'collabo_events/owners/subscribers.html'
    print("QuizListView Owners")

    def get_queryset(self):
        self.host = get_object_or_404(Host, user=self.request.user)
        print("GET UserListView")
        print(self.host)
        #event = Host.objects.values('event').get(user=(self.host.user))
        queryset = Customer.objects.filter(subscription__in=[self.host])

        print(queryset)

        #queryset1 = Saloons.objects.get(owner=self.owner)
        #object = super(Saloons, self).get_object(owner=self.owner)
        #print(object)

        for item in queryset:
            print(item)

        return queryset


#
# @method_decorator([login_required, teacher_required], name='dispatch')
# class QuizListView(ListView):
#     model = Quiz
#     ordering = ('name', )
#     context_object_name = 'quizzes'
#     template_name = 'classroom/teachers/quiz_change_list.html'
#
#     def get_queryset(self):
#         queryset = self.request.user.quizzes \
#             .select_related('subject') \
#             .annotate(questions_count=Count('questions', distinct=True)) \
#             .annotate(taken_count=Count('taken_quizzes', distinct=True))
#
#         print(self.request.user)
#         print(self.request.user.quizzes.select_related('subject'))
#         #print(queryset)
#         return queryset


