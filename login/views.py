from django.http import HttpResponseRedirect
from django.shortcuts import render
from login.models import Login

# Create your views here.

def login(request):
    if request.method == 'POST':
        uname = request.POST.get("username")
        passw = request.POST.get("pass")
        obj = Login.objects.filter(user_name=uname, password=passw)
        tp = ""
        for ob in obj:
            tp = ob.type
            uid = ob.u_id
            if tp == "admin":
                request.session["u_id"] = uid
                return HttpResponseRedirect('/temp/admin/')
            elif tp == "student":
                request.session["u_id"] = uid
                return HttpResponseRedirect('/temp/student/')
            elif tp == "teacher":
                request.session["u_id"] = uid
                return HttpResponseRedirect('/temp/teacher/')

        else:

            objlist = "username or password incorrect....please try again....!"
            context = {
                'msg':objlist
            }
            return render(request,'login/login.html',context)
    return render(request,'login/login.html')
