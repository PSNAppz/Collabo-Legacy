
from django.contrib.auth import login, authenticate
from django.http import HttpResponse
from django.shortcuts import render, redirect

from collabo_events.forms import SignUpForm
from .views import *

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            print("SELLER")
            print(form.cleaned_data.get('is_seller'))


            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password,is_seller=True)
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'createseller.html', {'form': form})






