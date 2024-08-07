
from django.contrib import admin
from django.urls import path
from .views import indexView, loginPage, registerPage
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', indexView), 
    path("login/", loginPage),
    path('register/', registerPage)

]

