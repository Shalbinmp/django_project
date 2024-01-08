"""find_my_tutor URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.conf.urls import url,include
from login import views

import assignment
import complaints
import doubt
import login
import payment
import request
import review
import student
import study_material
import teacher
import submission
import videos
urlpatterns = [
    path('admin/', admin.site.urls),
    url('complaints/',include('complaints.url')),
    url('doubt/',include('doubt.url')),
    url('login/',include('login.url')),
    url('payment/',include('payment.url')),
    url('request/', include('request.url')),
    url('review/', include('review.url')),
    url('student/', include('student.url')),
    url('study_material/', include('study_material.url')),
    url('teacher/', include('teacher.url')),
    url('submission/', include('submission.url')),
    url('videos/', include('videos.url')),
    url('assignment/',include('assignment.url')),
    url('temp/',include('temp.url')),
    url('$',views.login)
]
