from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *

def drinks_view(request):
    drinks = Drinks.objects.values("name", "country")
    context = {'drinks':drinks}
    return render(request, 'home.html', context)