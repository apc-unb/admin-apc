from django.shortcuts import render
import requests
import json

data = {}
NEWS_URL = 'http://127.0.0.1:8080/news'
EXAMS_URL = 'http://127.0.0.1:8080/exams'
TASKS_URL = 'http://127.0.0.1:8080/tasks'
CLASSES_URL = 'http://127.0.0.1:8080/classes'
STUDENTS_URL = 'http://127.0.0.1:8080/students'
# Create your views here.

def index(request):
    return render(request, 'index.html', {})