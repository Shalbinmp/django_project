from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'temp/home.html')

def admin(request):
    return render(request,'temp/Admin.html')

def student(request):
    return render(request,'temp/student.html')

def teacher(requset):
    return render(requset,'temp/teacher.html')

