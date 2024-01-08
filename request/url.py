from django.conf.urls import url
from request import views
urlpatterns=[
    url('manage_request/',views.manage_request),
    url('view_request/',views.view_request),
    url('accept/(?P<idd>\w+)',views.accept),
    url('post_req/(?P<idd>\w+)',views.post_request),
    url('decline/(?P<idd>\w+)',views.decline),
    url('pay/(?P<idd>\w+)',views.pay),
]