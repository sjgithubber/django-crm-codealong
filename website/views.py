from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.hashers import check_password
from .forms import SignUpForm, AddRecordForm
# this is to make it viewable in page
from .models import Record
# Create your views here.
# def home(request):
#     return render(request, 'home.html', {})
# django1; passwd123

# In django settings have set the debug=False, have set the allowed_hosts next, to localhost address, 127.0.0.1

def home(request):
    # assigns all the objects in class to the variable
    # get all variables in class
    records = Record.objects.all()

    # check to see if logging in
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

        # check if person is logged in
        if user is not None:
            login(request, user)
            messages.success(request, "You have logged in")
            return redirect('home')
        else:
            messages.success(request, "There was an error logging in, Please Try Again! ")
            return redirect('home')
    # this block will give back the home page and records variable as records to manipulate in home.html
    else:
        return render(request, 'home.html', {'records':records})

# def login_user(request):
#     pass


def logout_user(request):
    logout(request)
    messages.success(request,"You have been logged out!")
    return redirect('home')

def register_user(request):
# using the imported signup form
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


def record_data(request, pk):
    if request.user.is_authenticated:
        # look up records
        # get single record using primary key
        db_record = Record.objects.get(id=pk)
        # the dict that we send here allows us to view it in record.html
        return render(request, 'record.html', {'db_record':db_record})
    else:
        messages.success(request, "You must be logged in to view that page!")
        return redirect('home')

def delete_record(request, pk):
    if request.user.is_authenticated:    
        delete_it = Record.objects.get(id=pk)
        delete_it.delete()
        messages.success(request, "The user_record was successfully deleted")
        return redirect('home')
    else:
        messages.info(request, "You are not logged in!")
        return redirect('home')
    

def add_record(request):
    # if request.user.is_authenticated:
        # db_record = Record.objects.get()
        # if request.method == 'POST': return page else return the same page 
    form = AddRecordForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method == "POST":
            if form.is_valid():
                add_record = form.save()
                messages.success(request, "Record added Successfully!")
                return redirect('home')
        return render(request, 'add_record.html', {'form': form})
    else:
        messages.info(request, "You are not logged in!")
        return redirect('home')
