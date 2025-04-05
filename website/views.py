from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.hashers import check_password
from .forms import SignUpForm
# Create your views here.
# def home(request):
#     return render(request, 'home.html', {})
# django1; passwd123

# In django settings have set the debug=False, have set the allowed_hosts next, to localhost address, 127.0.0.1

def home(request):
    # check if person is logged in
    if request.method == 'POST':
        # username = request.POST.get('username')
        # strip whitespaces
        username = request.POST.get('username', '').strip()
        # username = request.POST.get('username', 'default_value') # default_value is the fallback value...
        # username = request.POST['username'] this returns exception when key not present
        # multivaluedictkeyerror
        passwd = request.POST.get('password')
        print(f"Attempting login for user: {username}")
        
        # authenticate
        user = authenticate(request, username=username, password=passwd)
        if user is not None:
            login(request, user)
            messages.success(request, "You have logged in")
            return redirect('home')
        else:
            messages.success(request, "There was an error logging in, Please Try Again! ")
            return redirect('home')
    else:
        return render(request, 'home.html', {})

# def login_user(request):
#     pass


def logout_user(request):
    logout(request)
    messages.success(request,"You have been logged out!")
    return redirect('home')

def register_user(request):
    if request.method == 'POST':
        # we init the class here
        form = SignUpForm(request.POST)
        # validation for form is checked here?
        if form.is_valid():
            form.save()
            # authenticate and login
            # no email confirmation for now
            # also can't register user something is missing
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password = password)
            login(request, user)
            messages.success(request, "Registration Successful")
            # messages.success(request, "You have been logged in!")
            return redirect('home')
    else:
        form = SignUpForm()
        # passes the form into the register_user.html
        return render(request, 'register_user.html', {'form':form})
        # this return is for GET requests since django.views must always return an Http Response object
    return render(request, 'register_user.html', {'form':form})

# using the imported signup form
