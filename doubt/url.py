from django.conf.urls import url
from doubt import views
urlpatterns=[
    url('doubt/',views.doubt),
    # url('view_doubt/',views.view_doubt),
  url('view_dou/',views.view_dou),
  url('doubt_reply/(?P<idd>\w+)',views.doubt_reply),
    url('doubt_replys/',views.doubt_replys),
]
