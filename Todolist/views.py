from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def home(request):
    return HttpResponse("Welcome to the Todolist app!")

#contact and aboutus
