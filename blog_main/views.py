from django.http import HttpResponse
from django.shortcuts import render,redirect
from blogs.models import Category , Blog
from assignment.models import About
from .forms import RegistrationForm , CustomAuthenticationForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import auth


def home(request):
    featured_post = Blog.objects.filter(is_featured=True , status = 'Published').order_by('updated_at')
    posts = Blog.objects.filter(is_featured=False , status = 'Published')
    
    # Fetch about Us
    try:
        about = About.objects.get()
    except:
        about = None

    context = {  
        'featured_post' : featured_post,
        'posts':posts,
        'about' : about
    }
    return render(request , 'home.html' , context)


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request,
                'Registration successful! Redirecting to login page...'
            )
            return redirect('register')
    else:
        form = RegistrationForm()
    
    context = {
        'form' : form
    }
    return render(request , 'register.html' , context)


def login(request):
    if request.method == "POST":
        form = CustomAuthenticationForm(request , request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = auth.authenticate(username=username , password=password)
            if user is not None:
                auth.login(request , user)
                messages.success(request, "Login successful!")
                return redirect('login')
            else:
                messages.error(request, "Invalid username or password")
    else:
        form = CustomAuthenticationForm()
    context = {
        'form' : form
    }
    return render(request , 'login.html' , context)


def logout(request):
    auth.logout(request)
    messages.success(request, "You have been logged out successfully.")
    return redirect('home')