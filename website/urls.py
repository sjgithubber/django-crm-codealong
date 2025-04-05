from django.urls import path, include
from . import views 


urlpatterns = [
    # path('', include('views.home'))
    path("", views.home, name='home'), 
    # path("login/", views.login_user ,name='login'),
    path("logout/", views.logout_user, name="logout"),
    path("register/", views.register_user, name="register_user"),
    path("record/<int:pk>", views.record_data, name="record"),
    # path('home', views.home, name='home1')
]