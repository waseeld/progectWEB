from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .models import *

from django.contrib import messages
from .forms import CreateUserForm


def home (request):
    return render(request, 'home/HomePage.html')

def gethelp (request):
    return render(request, 'home/GetHelp.html')

def signin (request):
    return render(request, 'home/signin.html')

def privacypolicy (request):
    return render(request, 'home/PrivacyPolicy.html')

def taxes (request):
    return render(request, 'home/Taxes.html')

def AboutUs (request):
    return render(request, 'home/AboutUs.html')

def contactus (request):
    return render(request, 'home/ContactUs.html')

def selectcar (request):
    return render(request, 'home/SelectCar.html')

def orderpage (request):
    return render(request, 'home/orderpage.html')


def signup (request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            username =form.cleaned_data.get('username')
            messages.success(request, f'Account created !! You are now able to Sign In {username}!')
            return redirect('signin')

    else:
        form = CreateUserForm()

    return render(request, 'home/signup.html',{'form':form})

def location (requst):
    return render(requst, 'home/location.html')

def ourlocation (requst):
    return render(requst, 'home/ourlocation.html')

def style_loc (requst):
    return render(requst, 'home/style_loc.html')

def selectcar (requst):
    return render(requst, 'home/SelectCar.html')

def orderpage (requst):
    return render(requst, 'home/orderpage.html')


def orderform(request):
    if request.method == 'POST':
        name = request.POST.get('first_name')
        l_name = request.POST.get('last_name')
        number = request.POST.get('phone_number')
        id = request.POST.get('id_order')
        order = request.POST.get('order_number')

        var_orderform = order(first_name=name, last_name=l_name, phone_number=number, id_order=id , order_number=order)
        var_orderform.save()
        return render(request, 'home/orderpage.html')
    else:
        return render(request, 'home/orderform.html')

def orderform(request):
        if request.method == 'POST':
            name = request.POST.get('first_name1')
            l_name = request.POST.get('last_name1')
            number = request.POST.get('phone_number1')
            id = request.POST.get('id_order1')
            order = request.POST.get('order_number1')

            var_ConfirmOrder = ConfirmOrder(first_name1=name, last_name1=l_name, phone_number1=number, id_order1=id, order_number1=order)
            var_ConfirmOrder.save()
            return render(request, 'home/HomePage.html')
        else:
            return render(request, 'home/orderform.html')