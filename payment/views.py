from django.shortcuts import render
from payment.models import Payment
import datetime
from teacher.models import Teacher

# Create your views here.
def payment(request,idd):
    ss = request.session["u_id"]
    if request.method == 'POST':
        obj = Payment()
        obj.payment = request.POST.get('payment')
        obj.status = 'paid'
        obj.date = datetime.datetime.today()
        obj.teacher_id = idd
        obj.student_id = ss
        obj.save()
        obb=Teacher.objects.get(teacher_id=idd)
        obb.status="Paid"
        obb.save()
    return render(request,'payment/payment.html')
# def view_payment(request):
#     return render(request,'payment/view_payment_teacher.html')

def view_pay(request):
    ss = request.session["u_id"]
    obj = Payment.objects.filter(teacher_id=ss)
    context = {
        'a': obj
    }
    return render(request,'payment/view_payment_teacher.html',context)