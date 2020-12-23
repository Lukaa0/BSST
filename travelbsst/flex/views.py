from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
# Create your views here.
def home_view(*args, **kwargs):
    return HttpResponse("<h1>error 404</h1>")