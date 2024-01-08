from django.shortcuts import render
from request.models import Request
import datetime
from teacher.models import Teacher

# Create your views here.

def manage_request(request):
    ss = request.session["u_id"]
    obj = Request.objects.filter(teacher_id=ss)
    context = {
        'a': obj
    }
    return render(request,'request/manage_request_teacher.html',context)

def view_request(request):
    ss = request.session["u_id"]
    obj = Request.objects.filter(status="accept",student_id=ss)
    context = {
        'b': obj
    }
    return render(request,'request/view_request_and_pay_student.html',context)

def accept(request,idd):
    obj = Request.objects.get(request_id=idd)
    obj.status = 'accept'
    obj.save()
    return manage_request(request)

def post_request(request,idd):
    ss = request.session["u_id"]
    obb = Teacher.objects.get(teacher_id=idd)
    context = {
        'a': obb
    }
    if request.method == 'POST':
        obj = Request()
        obj.teacher_id = idd
        obj.request = request.POST.get('request')
        obj.student_id = ss
        obj.date = datetime.datetime.now()
        obj.save()
    return render(request,'request/request.html',context)

def decline(request,idd):
    obj =Request.objects.get(request_id=idd)
    obj.status="decline"
    obj.save()
    return manage_request(request)

def pay(request,idd):
    obj =Request.objects.get(request_id=idd)
    obj.status="pay"
    obj.save()
    return view_request(request)