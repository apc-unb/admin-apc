from django.shortcuts import render
import requests
import json

# Create your views here.
def index(request):
    return render(request, 'index.html', {})

def students(request):
    
    # requests to API
    s = requests.Session()
    r = s.get('http://127.0.0.1:8080/students')
    data = {}
    data["students"] = r.json()
    r = s.get('http://127.0.0.1:8080/classes')
    data["classes"] = r.json()

    return render(request, 'students.html', data)

def create_student(request):
    # requests to API
    s = requests.Session()
    r = s.get('http://127.0.0.1:8080/students')
    data = {}
    data["students"] = r.json()
    r = s.get('http://127.0.0.1:8080/classes')
    data["classes"] = r.json()

    # create student
    if request.method == "POST":
        new_student = {}
        new_student["firstname"] = request.POST.get("firstname")
        new_student["lastname"] = request.POST.get("lastname")
        new_student["matricula"] = request.POST.get("matricula")
        new_student["ClassID"] = request.POST.get("ClassID")
        requests.post('http://127.0.0.1:8080/students', "[" + json.dumps(new_student) + "]")
    
    
    return students(request)

def update_student(request):
    # requests to API
    s = requests.Session()
    r = s.get('http://127.0.0.1:8080/students')
    data = {}
    data["students"] = r.json()
    r = s.get('http://127.0.0.1:8080/classes')
    data["classes"] = r.json()

    # update student
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
            
            requests.put('http://127.0.0.1:8080/students', json.dumps(update_student))

    return students(request)

