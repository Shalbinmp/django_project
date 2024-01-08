from django.shortcuts import render
from student.models import  Student
from login.models import Login


# Create your views here.

def student(request):
    if request.method == 'POST':
        obj = Student()
        obj.password = request.POST.get('Password')
        obj.address = request.POST.get('address')
        obj.course = request.POST.get('Course')
        obj.email = request.POST.get('semail')
        obj.student_name = request.POST.get('Sname')
        obj.gender = request.POST.get('Gender')
        obj.phone = request.POST.get('sphone')
        obj.save()

        obb=Login()
        obb.user_name=obj.student_name
        obb.password=request.POST.get('Password')
        obb.type="student"
        obb.u_id=obj.student_id
        obb.save()
    return render(request,'student/student_registration.html')

def view_block(request):
    obj = Student.objects.all()
    context = {
        'a': obj
    }
    return render(request,'student/view_block_student_admin.html',context)

def block(request,idd):
    obj =Student.objects.get(student_id=idd)
    obj.status= "blocked"
    obj.save()
    return view_block(request)