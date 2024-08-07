
from django.shortcuts import HttpResponse, render
def indexView(req):

    data = { 
        "name": "Harry",
        "age": 24, 
        "hobbies": ["coding", "reading", "gaming"],
        "is_male": True
    
    }
    return render(req, "index.html", data)

def loginPage(req):
   return render(req, "login.html")
def registerPage(req):
    return render(req, "register.html")

# Add more views here
