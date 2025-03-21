from django.urls import path
from . import views # Import views from the same directory

urlpatterns = [
    path('home/',views.home,name='home'), # When the user goes to the home page, the home function from views.py will be called
]