from django.shortcuts import render
import requests
import json

data = {}
# Create your views here.
def index(request):
    return render(request, 'index.html', {})

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
    return render(request, 'choose_students.html', data)

def students(request):
    
    s = requests.Session()
    r = s.get('http://127.0.0.1:8080/students/' + data["ClassID"])
    data["students"] = r.json()
    r = s.get('http://127.0.0.1:8080/classes')
    data["classes"] = r.json()

    return render(request, 'students.html', data)

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

def classes(request):
    
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
    return render(request, 'choose_news.html', data)

def news(request):
    
    s = requests.Session()
    r = s.get('http://127.0.0.1:8080/news/' + data["ClassID"])
    data["news"] = r.json()
    r = s.get('http://127.0.0.1:8080/classes')
    data["classes"] = r.json()
    return render(request, 'news.html', data)

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

def exams(request):
    
    s = requests.Session()
    r = s.get('http://127.0.0.1:8080/classes')
    data["classes"] = r.json()
    r = s.get('http://127.0.0.1:8080/exams')
    data["exams"] = r.json()
    r = s.get('http://127.0.0.1:8080/tasks')
    data["tasks"] = r.json()
    return render(request, 'exams.html', data)

def create_exam(request):
    if request.method == 'POST':
        new_exam = {}
        new_exam["classid"] = request.POST.get("ClassID")
        new_exam["title"] = request.POST.get("title")
        
        requests.post('http://127.0.0.1:8080/exams', data="[" + json.dumps(new_exam) + "]")
    return exams(request)

def update_exam(request):
    if request.method == 'POST':
        update_exam = {}
        update_exam["ID"] = request.POST.get("ID")

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