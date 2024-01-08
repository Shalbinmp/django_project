from django.shortcuts import render
from complaints.models import Complaints
import datetime
from teacher.models import Teacher
# Create your views here.


def complaints(request):
    ss = request.session["u_id"]
    obb=Teacher.objects.all()
    context={
        's':obb
    }
    if request.method == 'POST':
        obj = Complaints()
        obj.complaints = request.POST.get('Complaint')
        obj.reply = 'pending'
        obj.date=datetime.datetime.today()
        obj.teacher_id = request.POST.get('tn')
        obj.student_id = ss
        obj.subject = request.POST.get('subject')
        obj.save()
    return render(request,'complaints/complaints.html',context)

# def view_complaints(request):
#     return render(request,'complaints/view_complaints and post _reply.html')

def view_comp_studnt(request):
    obj = Complaints.objects.all()
    context = {
        'a': obj
    }
    return render(request,'complaints/view_complaints and post _reply.html',context)

def reply(request,idd):
    if request.method=="POST":
        obj = Complaints.objects.get(complaint_id=idd)
        obj.reply = request.POST.get('reply')
        obj.save()
        return view_comp_studnt(request)
    return render(request,'complaints/reply.html')


def st_vw_reply(request):
    ss = request.session["u_id"]
    obj = Complaints.objects.filter(student_id=ss)
    context = {
        'a': obj
    }
    return render(request,'complaints/student_vw_reply.html',context)

def teacher_vw(request):
    ss = request.session["u_id"]
    obj = Complaints.objects.filter(teacher_id=ss)
    context = {
        'a': obj
    }
    return render(request,'complaints/teacher_view.html',context)