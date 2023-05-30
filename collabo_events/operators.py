from django.contrib import messages
import var_dump
from pprint import pprint
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.db.models import Count
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, ListView, UpdateView,TemplateView
from ..models import Event,Owners,EventSeller,EventCategory
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import datetime

from ..decorators import operator_required
from django.core.paginator import Paginator
#from ..forms import CustomerSignUpForm, TakeQuizForm
from ..models import  User



# class OperatorSignUpView(CreateView):
#      model = User
#      #form_class = CustomerSignUpForm
#      #template_name = 'registration/signup_form.html'
#
#      def get_context_data(self, **kwargs):
#          kwargs['user_type'] = 'operator'
#          return super().get_context_data(**kwargs)
#
#      def form_valid(self, form):
#          user = form.save()
#          login(self.request, user)
#          return redirect('operator:quiz_list')
#     pass



@method_decorator([login_required, operator_required], name='dispatch')
class QuizListView(ListView):
    model = EventSeller
    ordering = ('name','address', )
    fields=('name','address')
    context_object_name = 'saloons'
    template_name = 'collabo_events/operators/saloon.html'
    print("QuizListView First")

    def get_queryset(self):
        print("QuizListView")
        #self.owner = get_object_or_404(Owners, owner=self.request.user)
        queryset = Event.objects.all()

        page = self.request.GET.get('page', 1)

        paginator = Paginator(queryset, 3)






        try:
            saloons = paginator.page(page)
        except PageNotAnInteger:
            saloons = paginator.page(1)
        except EmptyPage:
            saloons = paginator.page(paginator.num_pages)



        return saloons




@method_decorator([login_required, operator_required], name='dispatch')
class SaloonEditView(TemplateView):

    template_name = 'collabo_events/operators/saloonedit.html'