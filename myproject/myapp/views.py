from django.shortcuts import render, redirect
from django.http import HttpResponse 
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Feature


def index(request):
    print(request)

    features = Feature.objects.all()

    return render(request,'index.html' , {'features':features} )

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2 :
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email Already Used')
                return redirect ('register')
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'Username Already Used')
                return redirect ('register')
            else : 
                user = User.objects.create_user(username=username, email= email, password=password)
                user.save
                return redirect('login')
        else:
            messages.info(request, 'Password Not The Same')
            return redirect('register')
    else:
        return render(request, 'register.html')  #here if the user only hits the blank submit button or sends a blank response the this will only render the register page with blank response. 

def counter(request):
    text = request.POST['text']
    amount_of_words = len(text.split())
    return render(request , 'counter.html' , {'amount': amount_of_words})

























# Create your views here.
# You can create your own urls here 
# you can pass your functions to urls.py and then include them to the urls.py of the main project .
# Heres you can view your web application out put on manage.py by running it.