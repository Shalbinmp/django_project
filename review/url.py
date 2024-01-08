from django.conf.urls import url
from review import views
urlpatterns=[
    url('review/',views.review),
    url('view_revi/',views.view_revi),
    url('teacher_vw/',views.teacher_vw_review),

]
