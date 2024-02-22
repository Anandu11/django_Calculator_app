"""Calculator URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from operation.views import Hai
from operation.views import hello
from operation.views import name 

from operation.views import Second
from operation.views import Subtraction
from operation.views import PrimeView
from operation.views import Format
from operation.views import registrationview
from operation.views import BookView
from operation.views import EmpView
from operation.views import StudentView
from operation.views import PersonView



urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/',Hai.as_view()),
    path('good/',hello.as_view()),
    path('today/',name.as_view()),
    path('war/',Second.as_view()),
    path('mearn/',Subtraction.as_view()),
    path('some/',PrimeView.as_view()),
    path('hey/',Format.as_view()),
    path('ray/',registrationview.as_view()),
    path('form/',BookView.as_view()),
    path('emp/',EmpView.as_view()),
    path('stud/',StudentView.as_view()),
    path('meta/',PersonView.as_view()),

]
