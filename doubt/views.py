from django.shortcuts import render
from doubt.models import Doubt
import datetime
from teacher.models import Teacher
# Create your views here.


def doubt(request):
    ss = request.session["u_id"]
    obb=Teacher.objects.all()
    context={
        'a':obb
    }
    if request.method == 'POST':
        obj = Doubt()
        obj.doubt = request.POST.get('doubt')
        obj.date=datetime.datetime.today()
        obj.student_id=ss
        obj.teacher_id=request.POST.get('tn')
        obj.doubt_reply='Pending'
        obj.save()
    return render(request,'doubt/doubt.html',context)

# def view_doubt(request):
#     return render(request,'doubt/view_doubt_and_reply_teacher.html')

def view_dou(request):
    ss = request.session["u_id"]
    obj = Doubt.objects.filter(student_id=ss)
    context = {
        'a': obj
    }
    return render(request,'doubt/view_doubt_and_reply_teacher.html',context)

def doubt_reply(request,idd):
    if request.method == "POST":
        obj = Doubt.objects.get(doubt_id=idd)
        obj.doubt_reply = request.POST.get('d_reply')
        obj.save()
        return view_dou(request)
    return render(request, 'doubt/reply.html')

def doubt_replys(request):
    ss = request.session["u_id"]
    obj = Doubt.objects.filter(teacher_id=ss)
    context = {
        'a': obj
    }
    return render(request,'doubt/teacher.html',context)

