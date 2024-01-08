from django.conf.urls import url
from teacher import views
urlpatterns=[
 url('teacher/',views.teacher),
    url('teacher_reg/',views.techer_reg),
    url('view_manage/',views.view_manage),
    url('Approve/(?P<idd>\w+)', views.Approve),
    url('Decline/(?P<idd>\w+)',views.Decline),

]