from django.shortcuts import render,redirect
from .models import Customer
# Create your views here.
def index(req):
    return render(req, "appIndex.html")
def studentList(req):
    user = Customer.objects.all()
    data = {
        "users": user,
        
    }
    return render(req, "studentList.html", data)

def listDelete(request, id):
    user = Customer.objects.get(id=id)
    user.delete()
    return redirect("/studentList")

def listUpdate(request, id):
    print(id)
    user = Customer.objects.get(id=id)
    form = CustomerForm(request.POST or None, instance=user)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect("/studentList")
    data = {'form': form}

    return render(request, "listUpdate.html", data)

def studentCreate(request):
    form = CustomerForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect("/studentList")
    data = {'form': form}
    return render(request, "studentCreate.html", data)