from django.shortcuts import render
import requests
import json

data = {}
# Create your views here.

def choose_exams(request):
    
    s = requests.Session()
    r = s.get('http://127.0.0.1:8080/classes')
    data["classes"] = r.json()
    r = s.get('http://127.0.0.1:8080/exams')
    data["exams"] = r.json()
    r = s.get('http://127.0.0.1:8080/tasks')
    data["tasks"] = r.json()

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
        return exams(request)
    return render(request, 'exams/choose_exams.html', data)

def exams(request):
    
    s = requests.Session()
    r = s.get('http://127.0.0.1:8080/classes')
    data["classes"] = r.json()
    r = s.get('http://127.0.0.1:8080/exams/' + data["ClassID"])
    data["exams"] = r.json()
    r = s.get('http://127.0.0.1:8080/tasks')
    data["tasks"] = r.json()
    return render(request, 'exams/exams.html', data)

def create_exam(request):
    if request.method == 'POST':
        new_exam = {}
        data["ClassID"] = request.POST.get("ClassID")

        new_exam["classid"] = request.POST.get("ClassID")
        new_exam["title"] = request.POST.get("title")
        
        requests.post('http://127.0.0.1:8080/exams', data="[" + json.dumps(new_exam) + "]")
    return exams(request)

def update_exam(request):
    if request.method == 'POST':
        update_exam = {}
        update_exam["ID"] = request.POST.get("ID")
        data["ClassID"] = request.POST.get("ClassID")

        if(request.POST.get("delete") == "on"):
            requests.delete('http://127.0.0.1:8080/exams', data="[" + json.dumps(update_exam) + "]")
        
        else:
            if request.POST.get("ClassID") != "":
                update_exam["classid"] = request.POST.get("ClassID")
            if request.POST.get("title") != "":
                update_exam["title"] = request.POST.get("title")
            requests.put('http://127.0.0.1:8080/exams', data="[" + json.dumps(update_exam) + "]")
    
    return exams(request)

def create_task(request):
    if request.method == 'POST':
        new_task = {}
        new_task["ExamID"] = request.POST.get("ExamID")
        new_task["title"] = request.POST.get("title")
        new_task["statement"] = request.POST.get("statement")
        new_task["score"] = float(request.POST.get("score"))
        new_task["tags"] = str(request.POST.get("tags")).split("#")
        
        requests.post('http://127.0.0.1:8080/tasks', data="[" + json.dumps(new_task) + "]")
    
    return exams(request)

def update_task(request):
    if request.method == 'POST':
        update_task = {}
        update_task["ID"] = request.POST.get("ID")

        if(request.POST.get("delete") == "on"):
            requests.delete('http://127.0.0.1:8080/tasks', data="[" + json.dumps(update_task) + "]")
        
        else:
            if request.POST.get("ExamID") != "":
                update_task["ExamID"] = request.POST.get("ExamID")
            if request.POST.get("title") != "":
                update_task["title"] = request.POST.get("title")
            if request.POST.get("statement") != "":
                update_task["statement"] = request.POST.get("statement")
            if request.POST.get("score") != "":
                update_task["score"] = float(request.POST.get("score"))
            if request.POST.get("tags") != "":
                update_task["tags"] = str(request.POST.get("tags")).split("#")

            requests.put('http://127.0.0.1:8080/tasks', data="[" + json.dumps(update_task) + "]")

    return exams(request)