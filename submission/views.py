from django.core.files.storage import FileSystemStorage
from django.http import HttpResponseRedirect
from django.shortcuts import render
from submission.models import Submission
import datetime

# create your views here

def submit(request,idd):
    ss=request.session["u_id"]
    if request.method == 'POST':
        obj = Submission()
        # obj.file = request.POST.get('Subject')
        myfile = request.FILES['Subject']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        obj.file = myfile.name
        obj.date = datetime.datetime.today()
        obj.student_id = ss
        obj.assignment_id = idd
        obj.save()
        return HttpResponseRedirect('/assignment/view_assignment_student/')
    return  render(request,'submission/submit_student.html')

def submission(request):
    obj = Submission.objects.all()
    context = {
        'a': obj
    }
    return render(request,'submission/view_assignment_submission_teacher.html',context)
