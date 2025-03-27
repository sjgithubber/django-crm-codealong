from django.urls import path, include
from . import views 


urlpatterns = [
    # path('', include('views.home'))
    path("", views.home, name='home'), 
    # path('home', views.home, name='home1')
]