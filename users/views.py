#Importing necessary modules and models
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import *

#define a view function for the home page
def home(request):
    return render(request, 'home.html')

#define view function for the login page
def login_page(request):
    #Check if the HTTP request method is POST
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        #Check if the user provided a username that exists
        if not User.objects.filter(username=username).exists():
            #Display an error if not
            messages.error(request, 'Invalid Username')
            return redirect('/login/')
        
        #Authenticate the user with the provided username and password
        user = authenticate(username=username, password=password)

        if user is None:
            #Display an error message if the authentification fails: "Invalid Password"
            messages.error(request, "Invalid Password")
            return redirect('/login')
        else:
            #Log the user in and redirect to the home page when successful
            login(request, user)
            return redirect('/home/')
        
    #Render the login page template (GET request)
    return render(request, 'login.html')

#Define a view function for the registration page
def register_page(request):
    #Check if the HTTP request method is POST (form submission)
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        password = request.POST.get('password')

        #Check if username already exists
        user = User.objects.filter(username=username)

        if user.exists():
        #Display message if the username is taken
            messages.info(request, "Username is taken!")
            return redirect('/register/')

    #Create a new User object with the provided information
        user = User.objects.create_user(
            first_name=first_name,
            last_name=last_name,
            username=username
        )

        #Set the user's password and save the user object
        user.set_password(password)
        user.save()

        #Display a message that indicates a successful account creation
        messages.info(request, "Account was Created Successfully!")
        return redirect('/register/')

    #Render the registration page template (GET request)
    return render(request, 'register.html')