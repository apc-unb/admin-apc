from django.shortcuts import render
import requests
import json

# Create your views here.
def index(request):
    return render(request, 'index.html', {})

def students(request):
    data = {}
    # requests to API
    s = requests.Session()
    r = s.get('http://127.0.0.1:8080/students')
    data["students"] = r.json()
    r = s.get('http://127.0.0.1:8080/classes')
    data["classes"] = r.json()

    return render(request, 'students.html', data)

def create_student(request):
    if request.method == "POST":
        new_student = {}
        new_student["firstname"] = request.POST.get("firstname")
        new_student["lastname"] = request.POST.get("lastname")
        new_student["matricula"] = request.POST.get("matricula")
        new_student["ClassID"] = request.POST.get("ClassID")
        requests.post('http://127.0.0.1:8080/students', data="[" + json.dumps(new_student) + "]")
    
    
    return students(request)

def update_student(request):
    if request.method == 'POST':
        update_student = {}
        update_student["ID"] = request.POST.get("ID")
        
        if(request.POST.get("delete") == "on"):
            requests.delete('http://127.0.0.1:8080/students', data="[" + json.dumps(update_student) + "]")  
        
        else: 
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
            if request.POST.get("exams1") != "":
                update_student["grades"].update({"exams" : [
                    float(request.POST.get("exams1")),
                    float(request.POST.get("exams2")),
                    float(request.POST.get("exams3")),
                ]})
            if request.POST.get("projects1") != "":
                update_student["grades"].update({"projects" : [
                    float(request.POST.get("projects1")),
                    float(request.POST.get("projects2")),
                    float(request.POST.get("projects3")),
                ]})
            if request.POST.get("lists1") != "":
                update_student["grades"].update({"lists" : [
                    float(request.POST.get("lists1")),
                    float(request.POST.get("lists2")),
                    float(request.POST.get("lists3")),
                ]})
            
            requests.put('http://127.0.0.1:8080/students', data="[" + json.dumps(update_student) + "]")

    return students(request)

def classes(request):
    data = {}
    s = requests.Session()
    r = s.get('http://127.0.0.1:8080/classes')
    data["classes"] = r.json()
    return render(request, 'classes.html', data)

def create_class(request):
    if request.method == 'POST':
        new_class = {}
        new_class["professorfirstname"] = request.POST.get("professorfirstname")
        new_class["professorlastname"] = request.POST.get("professorlastname")
        new_class["classname"] = request.POST.get("classname")
        new_class["address"] = request.POST.get("address")
        new_class["year"] = int(request.POST.get("year"))
        new_class["season"] = int(request.POST.get("season"))
        
        requests.post('http://127.0.0.1:8080/classes', data="[" + json.dumps(new_class) + "]")

    return classes(request)

def update_class(request):
    if request.method == 'POST':
        update_class = {}
        update_class["ID"] = request.POST.get("ID")

        if(request.POST.get("delete") == "on"):
            requests.delete('http://127.0.0.1:8080/classes', data="[" + json.dumps(update_class) + "]")

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

            requests.put('http://127.0.0.1:8080/classes', data="[" + json.dumps(update_class) + "]")

    return classes(request)

def news(request):
    data = {}
    s = requests.Session()
    r = s.get('http://127.0.0.1:8080/news')
    data["news"] = r.json()
    r = s.get('http://127.0.0.1:8080/classes')
    data["classes"] = r.json()
    return render(request, 'news.html', data)

def create_new(request):
    if request.method == 'POST':
        new_new = {}
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