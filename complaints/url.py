from django.conf.urls import url
from complaints import views
urlpatterns=[
   url('complaints/',views.complaints),
    url('view_reply/',views.st_vw_reply),
    url('viw_comp_stdnt/',views.view_comp_studnt),
    url('teacher_vw/',views.teacher_vw),
    url('add_reply/(?P<idd>\w+)',views.reply),

]