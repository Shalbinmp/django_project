from django.conf.urls import url
from payment import  views
urlpatterns=[
    url('payment/(?P<idd>\w+)',views.payment),
    # url('view_payment/',views.view_payment),
    url('view_pay/',views.view_pay),

]