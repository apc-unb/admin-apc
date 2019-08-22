from django.shortcuts import render
import requests
import json

data = {}
# Create your views here.

def index(request):
    return render(request, 'index.html', {})