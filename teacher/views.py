from django.shortcuts import render

from login.models import Login
from teacher.models import Teacher


# Create your views here.

def teacher(request):
    obj = Teacher.objects.all()
    context = {
        'a': obj
    }
    return render(request,'teacher/search_teacher.html',context)

def techer_reg(request):
    if request.method =='POST':
        obj = Teacher()
        obj.teacher_name = request.POST.get('Tname')
        obj.qualification = request.POST.get('Qualifications')
        obj.phone = request.POST.get('Tphone')
        obj.age = request.POST.get('Tage')
        obj.status = 'pending'
        obj.password = request.POST.get('Tpassword')
        obj.address = request.POST.get('address')
        obj.email = request.POST.get('Temail')
        obj.gender = request.POST.get('Gender')
        obj.course = request.POST.get('subject')
        obj.save()

        obb = Login()
        obb.user_name = obj.teacher_name
        obb.password = request.POST.get('Tpassword')
        obb.type = "teacher"
        obb.u_id = obj.teacher_id
        obb.save()
    return render(request,'teacher/teacher_registration.html')

def view_manage(request):
    obj = Teacher.objects.all()
    context = {
        'b': obj
    }
    return render(request,'teacher/view_manage_teacher_admin.html',context)

def Approve(request,idd):
    obj =Teacher.objects.get(teacher_id=idd)
    obj.status="Approve"
    obj.save()
    return view_manage(request)

def Decline(request,idd):
    obj =Teacher.objects.get(teacher_id=idd)
    obj.status="Decline"
    obj.save()
    return view_manage(request)