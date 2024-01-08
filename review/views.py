from django.shortcuts import render
from review.models import Review
import datetime
from teacher.models import Teacher
# Create your views here.

def review(request):
    ss = request.session["u_id"]
    obb=Teacher.objects.all()
    context={
        'd':obb
    }
    if request.method == 'POST':
        obj = Review()
        obj.review = request.POST.get('review')
        obj.date = datetime.datetime.today()
        obj.student_id = ss
        obj.teacher_id = request.POST.get('tn')
        obj.save()
    return render(request,'review/review.html',context)

def view_revi(request):
    obj = Review.objects.all()
    context = {
        'a': obj
    }
    return render(request,'review/view_reviews_admin.html',context)

def teacher_vw_review(request):
    ss = request.session["u_id"]
    obj = Review.objects.filter(teacher_id=ss)
    context = {
        'a': obj
    }
    return render(request,'review/teacher_vw_review.html',context)