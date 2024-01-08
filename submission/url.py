from django.conf.urls import url
from submission import views
urlpatterns=[
 url('submission/',views.submission),
 url('submit/(?P<idd>\w+)',views.submit),
]