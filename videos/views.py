from django.core.files.storage import FileSystemStorage
from django.shortcuts import render
from videos.models import Videos
import datetime

# Create your views here.

def video(request):
    ss=request.session["u_id"]
    if request.method == 'POST':
        obj = Videos()
        obj.teacher_id = ss
        obj.subject = request.POST.get('Subject')
        obj.date = datetime.datetime.today()
        obj.type = request.POST.get('Type')
        # obj.video = request.POST.get('file')
        myfile = request.FILES['file']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        obj.file = myfile.name
        obj.save()
    return render(request,'videos/video.html')

def view_teacher(request):
    obj=Videos.objects.all()
    context={
        'a':obj
    }
    return render(request,'videos/view_teacher_added_videos.html',context)

def view_videos(request):
    obj=Videos.objects.all()
    context={
        'b':obj
    }
    return render(request,'videos/view_videos_student.html',context)