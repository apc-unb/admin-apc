from django.shortcuts import render
import requests
import json

data = {}
# Create your views here.

def choose_news(request):
    
    s = requests.Session()
    r = s.get('http://127.0.0.1:8080/classes')
    data["classes"] = r.json()
    r = s.get('http://127.0.0.1:8080/news')
    data["news"] = r.json()
    data["years"] = []
    data["seasons"] = []
    data["classnames"] = []
    for classe in data["classes"]:
        if classe["year"] not in data["years"]:
            data["years"].append(classe["year"])

        if classe["season"] not in data["seasons"]:
            data["seasons"].append(classe["season"])

        if classe["classname"] not in data["classnames"]:
            data["classnames"].append(classe["classname"])
    
    year = request.POST.get("year")
    if request.method == 'POST' and year != None :
        key = 0
        season = request.POST.get("season")
        classname = request.POST.get("classname")
        for classe in data["classes"]:
            if (int(year) == classe["year"]):
                if (int(season) == classe["season"]):
                    if classname == classe["classname"]:
                        key = classe["ID"]
        data["ClassID"] = key
        return news(request)
    return render(request, 'news/choose_news.html', data)

def news(request):
    
    s = requests.Session()
    r = s.get('http://127.0.0.1:8080/news/' + data["ClassID"])
    data["news"] = r.json()
    r = s.get('http://127.0.0.1:8080/classes')
    data["classes"] = r.json()
    return render(request, 'news/news.html', data)

def create_new(request):
    if request.method == 'POST':
        new_new = {}
        data["ClassID"] = request.POST.get("ClassID")
        new_new["classid"] = request.POST.get("ClassID")
        new_new["title"] = request.POST.get("title")
        new_new["description"] = request.POST.get("description")
        new_new["tags"] = str(request.POST.get("tags")).split("#")
        
        requests.post('http://127.0.0.1:8080/news', data="[" + json.dumps(new_new) + "]")
    return news(request)

def update_new(request):
    if request.method == 'POST':
        update_new = {}
        update_new["ID"] = request.POST.get("ID")
        data["ClassID"] = request.POST.get("ClassID")

        if(request.POST.get("delete") == "on"):
            requests.delete('http://127.0.0.1:8080/news', data="[" + json.dumps(update_new) + "]")
        
        else:
            if request.POST.get("ClassID") != "":
                update_new["classid"] = request.POST.get("ClassID")
            if request.POST.get("title") != "":
                update_new["title"] = request.POST.get("title")
            if request.POST.get("description") != "":
                update_new["description"] = request.POST.get("description")
            if request.POST.get("tags") != "":
                update_new["tags"] = str(request.POST.get("tags")).split("#")
            requests.put('http://127.0.0.1:8080/news', data="[" + json.dumps(update_new) + "]")

    return news(request)
