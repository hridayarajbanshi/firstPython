from django.urls import path
from .views import *
urlpatterns = [
    path("appIndex/", index),
    path("studentList/", studentList)
]


