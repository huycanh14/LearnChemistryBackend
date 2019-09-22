from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    response = HttpResponse()
    response.writelines("<h1>Xin chào</h1>")
    return response
