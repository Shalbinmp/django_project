from django.shortcuts import render
from assignment.models import Assignment
import datetime
# Create your views here.

def assignment(request):
    ss=request.session["u_id"]
    if request.method == 'POST':
        obj = Assignment()
        obj.assignment = request.POST.get('assignment_topic')
        obj.subject = request.POST.get('Subject')
        obj.date = datetime.datetime.today()
        obj.teacher_id = ss
        obj.submission_date = request.POST.get('submission_date')
        obj.save()
    return render(request,'assignment/assignment.html')


def assignment_admin(request):
    obj = Assignment.objects.all()
    context = {
        'a': obj
    }
    return render(request,'assignment/view_assignment_admin.html',context)


def assignment_student(request):
    obj = Assignment.objects.all()
    context = {
        'b': obj
    }
    return render(request,'assignment/view_assignment_student.html',context)

