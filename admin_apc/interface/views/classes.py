from django.shortcuts import render
from .base import CLASSES_URL
import requests
import json

data = {}
# Create your views here.

def choose_classes(request):
    s = requests.Session()
    r = s.get(CLASSES_URL)
    data["classes"] = r.json()
    data["years"] = []
    data["seasons"] = []
    for classe in data["classes"]:
        if classe["year"] not in data["years"]:
            data["years"].append(classe["year"])

        if classe["season"] not in data["seasons"]:
            data["seasons"].append(classe["season"])
    
    year = request.POST.get("year")
    season = request.POST.get("season")

    if request.method == 'POST' and year != '' and season != '':
        data["y"] = int(year)
        data["s"] = int(season)
        return classes(request)
    return render(request, 'classes/choose_classes.html', data)

def classes(request):
    
    s = requests.Session()
    r = s.get(CLASSES_URL)
    data["classes"] = r.json()
    data["choose_classes"] = []
    for classe in data["classes"]:
        if (classe["year"] == data["y"] and classe["season"] == data["s"]):
            data["choose_classes"].append(classe)
    return render(request, 'classes/classes.html', data)

def create_class(request):
    if request.method == 'POST':
        new_class = {}
        new_class["professorfirstname"] = request.POST.get("professorfirstname")
        new_class["professorlastname"] = request.POST.get("professorlastname")
        new_class["classname"] = request.POST.get("classname")
        new_class["address"] = request.POST.get("address")
        new_class["year"] = int(request.POST.get("year"))
        new_class["season"] = int(request.POST.get("season"))
        
        requests.post(CLASSES_URL, data="[" + json.dumps(new_class) + "]")

    return choose_classes(request)

def update_class(request):
    if request.method == 'POST':
        update_class = {}
        update_class["ID"] = request.POST.get("ID")

        if(request.POST.get("delete") == "on"):
            requests.delete(CLASSES_URL, data="[" + json.dumps(update_class) + "]")

        else:
            if request.POST.get("professorfirstname") != "":
                update_class["professorfirstname"] = request.POST.get("professorfirstname")
            if request.POST.get("professorlastname") != "":
                update_class["professorlastname"] = request.POST.get("professorlastname")
            if request.POST.get("classname") != "":
                update_class["classname"] = request.POST.get("classname")
            if request.POST.get("address") != "":
                update_class["address"] = request.POST.get("address")
            if request.POST.get("year") != "":
                update_class["year"] = int(request.POST.get("year"))
            if request.POST.get("season") != "":
                update_class["season"] = int(request.POST.get("season"))

            requests.put(CLASSES_URL, data="[" + json.dumps(update_class) + "]")

    return choose_classes(request)