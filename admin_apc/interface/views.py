from django.shortcuts import render
import requests

# Create your views here.
def index(request):
    return render(request, 'index.html', {})

def students(request):
    s = requests.Session()
    r = s.get('http://127.0.0.1:8080/students')
    data = {}
    data["students"] = r.json()
    print(data)

    return render(request, 'students.html', data)