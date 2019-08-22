from django.shortcuts import render
import requests
import json

data = {}
# Create your views here.

def choose_students(request):
    
    s = requests.Session()
    r = s.get('http://127.0.0.1:8080/classes')
    data["classes"] = r.json()
    r = s.get('http://127.0.0.1:8080/students')
    data["students"] = r.json()
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
        return students(request)
    return render(request, 'students/choose_students.html', data)

def students(request):
    
    s = requests.Session()
    r = s.get('http://127.0.0.1:8080/students/' + data["ClassID"])
    data["students"] = r.json()
    r = s.get('http://127.0.0.1:8080/classes')
    data["classes"] = r.json()

    return render(request, 'students/students.html', data)

def create_student(request):
    if request.method == "POST":
        new_student = {}
        data["ClassID"] = request.POST.get("ClassID")
        new_student["firstname"] = request.POST.get("firstname")
        new_student["lastname"] = request.POST.get("lastname")
        new_student["matricula"] = request.POST.get("matricula")
        new_student["ClassID"] = request.POST.get("ClassID")
        requests.post('http://127.0.0.1:8080/students', data="[" + json.dumps(new_student) + "]")
    
    
    return students(request)

def update_student(request):
    if request.method == 'POST':
        update_student = {}
        data["ClassID"] = request.POST.get("ClassID")
        if(request.POST.get("delete") == "on"):
            update_student["ID"] = request.POST.get("ID")
            requests.delete('http://127.0.0.1:8080/students', data="[" + json.dumps(update_student) + "]")  
        
        else:
            update_student["StudentID"] = request.POST.get("ID")
            update_student["ClassID"] = request.POST.get("ClassID")
            if request.POST.get("firstname") != "":
                update_student["firstname"] = request.POST.get("firstname")
            if request.POST.get("lastname") != "":
                update_student["lastname"] = request.POST.get("lastname")
            if request.POST.get("matricula") != "":
                update_student["matricula"] = request.POST.get("matricula")
            if request.POST.get("codeforces") != "" or request.POST.get("uri") != "":
                update_student["handles"] = {}
            if request.POST.get("codeforces") != "":
                update_student["handles"].update({"codeforces" : request.POST.get("codeforces")})
            if request.POST.get("uri") != "":
                update_student["handles"].update({"uri" : request.POST.get("uri")})
            update_student["grades"] = {}
            if request.POST.get("exams") != "":
                l = request.POST.getlist("exams")
                l = [float(i) for i in l]
                update_student["grades"].update({"exams" :  l })
            if request.POST.get("projects") != "":
                l = request.POST.getlist("projects")
                l = [float(i) for i in l]
                update_student["grades"].update({"projects" : l })
            if request.POST.get("lists") != "":
                l = request.POST.getlist("lists")
                l = [float(i) for i in l]
                update_student["grades"].update({"lists" : l })

            print(update_student)
            requests.put('http://127.0.0.1:8080/admin/student', data=json.dumps(update_student))

    return students(request)