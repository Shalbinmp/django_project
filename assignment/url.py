
from  django.conf.urls import url
from assignment import views
urlpatterns=[
 url('assignment/',views.assignment),
    url('view_assignment_admin/',views.assignment_admin),
    url('view_assignment_student/',views.assignment_student),
]