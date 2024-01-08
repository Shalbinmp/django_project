from django.conf.urls import url
from temp import views

urlpatterns=[
    url('home/',views.home),
    url('Admin/',views.admin),
    url('student/',views.student),
    url('teacher/',views.teacher),


    
]