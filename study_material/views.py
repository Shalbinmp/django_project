from django.core.files.storage import FileSystemStorage
from django.shortcuts import render
from study_material.models import StudyMaterial
import datetime
# Create your views here

def study_material(request):
    ss=request.session["u_id"]
    if request.method == 'POST':
        obj = StudyMaterial()
        # obj.study_material = request.POST.get('file')
        myfile=request.FILES['std']
        fs=FileSystemStorage()
        filename=fs.save(myfile.name,myfile)
        obj.study_material=myfile.name
        obj.date = datetime.datetime.today()
        obj.subject = request.POST.get('Subject')
        obj.teacher_id = ss
        obj.type = request.POST.get('Type')
        obj.save()
    return render(request,'study_material/study_material.html')

def view_study_mate(request):
    obj = StudyMaterial.objects.all()
    context = {
        'a': obj
    }
    return render(request,'study_material/view_study_material_student.html',context)

def view_teacher(request):
    obj = StudyMaterial.objects.all()
    context = {
        'b': obj
    }
    return render(request,'study_material/view_teacher_added_study material.html',context)