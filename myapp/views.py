from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.conf import settings
from django.core.mail import send_mail
from .models import MailModel
from .forms import MailForm
from django.contrib import messages

def signup(request):
    if request.method == 'POST':
        form = MailForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account Created Successfully..!')
             
               
        username = request.POST["username"]
        password = request.POST["password"]
        email = request.POST["email"]
        
        
        user = MailModel.objects.create_user(
                username = username,
                password = password,
                email = email 
            ) 
        login(request, user)
        
        subject = 'welcome to thoughtwin world'
        message = f'Hi {MailModel.username}, thank you for registering in thoughtwin.'
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [MailModel.email]
        send_mail( subject, message, email_from, recipient_list )
    
    else:
        form = MailForm()      
    return render(request, 'signup.html', {'form':form})


# def signup(request):
#     if request.method == "POST":
#         form = MailForm(request.POST)
        
#         if form.is_valid():
#             form.save()
#             messages.success(request, 'Account Created Successfully..!')
#     else:        
#         form = MailForm()
#     return render(request, 'signup.html',{'form':form})