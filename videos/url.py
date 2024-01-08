from django.conf.urls import url
from videos import views
urlpatterns=[
    url('video/',views.video),
    url('view_techer/',views.view_teacher),
    url('view_videos/',views.view_videos),
]