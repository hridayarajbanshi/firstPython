from django.shortcuts import render

# Create your views here.
def index(req):
    return render(req, "appIndex.html")
def studentList(req):
        
    return render(req, "studentList.html")