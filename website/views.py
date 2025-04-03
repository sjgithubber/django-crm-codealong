from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.
# def home(request):
#     return render(request, 'home.html', {})
# django1; passwd123

# In django settings have set the debug=False, have set the allowed_hosts next, to localhost address, 127.0.0.1

def home(request):
    # check if person is logged in
    if request.method == 'POST':
        username = request.POST.get('username')
        # username = request.POST.get('username', 'default_value') # default_value is the fallback value...
        # username = request.POST['username'] this returns exception when key not present
        # multivaluedictkeyerror
        passwd = request.POST.get('password')
# alternatively can also use
# the problem here is it enforces guest login in case of an error
        # if 'username' in request.POST:
        #     username = request.POST.get('username')
        # else:
        #     username = 'guest'
        # authenticate
        user = authenticate(request, username=username, password=passwd)
        if user is not None:
            login(request, user)
            messages.success(request, "You have logged in")
            return redirect('home')
        else:
            messages.success(request, "There was an error logging in ")
            return redirect('home')
    else:
        return render(request, 'home.html', {})




def login_user(request):
    pass


def logout_user(request):
    pass