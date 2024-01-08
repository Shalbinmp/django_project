from django.conf.urls import url
from study_material import views
urlpatterns=[
 url('study_material/',views.study_material),
    url('view_study_mate/',views.view_study_mate),
    url('view_teacher/',views.view_teacher),
]