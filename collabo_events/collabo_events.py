from django.shortcuts import redirect, render
from django.views.generic import TemplateView
from ..filters import UserFilter


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

from ..forms import SellerEditForm
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




            #return render(request, 'collabo_events/home.html')

        #return redirect('owners:quiz_change_list')
        else:
            print("not user")
            return redirect('operators:event_list')
    return render(request, 'collabo_events/home.html')



from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect

from collabo_events.forms import SignUpForm

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'collabo_events/owners/createseller.html', {'form': form})