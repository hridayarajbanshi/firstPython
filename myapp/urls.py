from django.urls import path
from .views import *
urlpatterns = [
    path("appIndex/", index),
    path("studentList/", studentList),
    path('create/', studentCreate),
    path('delete/<int:id>/', listDelete),
    path('update/<int:id>/', listUpdate),
     path('doners/', BloodReqView)
]


