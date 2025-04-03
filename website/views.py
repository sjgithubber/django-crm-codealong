from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.hashers import check_password
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
# alternatively can also use
# the problem here is it enforces guest login in case of an error
        # if 'username' in request.POST:
        #     username = request.POST.get('username')
        # else:
        #     username = 'guest'
        
        
        # debug authentication 1
        # try:
        # this didn't work gave us False
        #     user_exists = User.objects.filter(username=username).exists()
        #     print(f"does username exists in database: {user_exists}")
        # except Exception as e:
        #     print("Error checking user: {e}")

        # check which users exist
        # result is that it does
        # all_users = User.objects.all().values_list('username', flat=True)
        # print(f"All users in system: {list(all_users)}")

        # debug authentication 2
        # Try with hardcoded values
        # this gives me the username
        # test_user = authenticate(request, username="username", password="pass")
        # print(f"Test authentication result: {test_user}")


        # debug authentication 3
        # Get the user object
        # user not found

        # try:
        #     user_obj = User.objects.get(username=username)
        #     print(f"Found user: {user_obj.username}, is_active: {user_obj.is_active}")
            
        #     # Check password directly
        #     pwd_valid = check_password(passwd, user_obj.password)
        #     print(f"Password valid: {pwd_valid}")
            
        #     # Now try authenticate
        #     auth_user = authenticate(request, username=username, password=passwd)
        #     print(f"Authenticate returned: {auth_user}")
            
        # except User.DoesNotExist:
        #     print(f"User {username} not found")

        # debug authentication 4
        # entered_username = request.POST.get('username')
        # from django.contrib.auth.models import User
        # all_users = list(User.objects.all().values_list('username', flat=True))

        # print(f"Entered username: '{entered_username}'")
        # print(f"All usernames: {all_users}")
        # print(f"Exact match check: '{entered_username}' in {all_users}: {entered_username in all_users}")

        # # Check for case insensitive match
        # for db_username in all_users:
        #     # the issue caused was found by the line below, as it gave entered_username as NoneType
        #     # the exact issue was a typo
        #     if db_username.lower() == entered_username.lower():
        #         print(f"Case-insensitive match found: '{db_username}' vs '{entered_username}'")


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