from django.conf.urls import url
from student import views
urlpatterns=[
 url('student/',views.student),
 url('view_block/',views.view_block),
 url('block/(?P<idd>\w+)',views.block)
]