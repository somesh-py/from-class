from django.shortcuts import render
from .forms import *
from .models import User
from django.http.response import HttpResponseRedirect
# Create your views here.


# def registration(request):
#     fm = User()
#     return render(request, 'index.html', {'from': fm})

# add new item

def add_show(request):
    if request.method=='POST':
        fm=UserRegistration(request.POST)
        if fm.is_valid():
            nm=fm.cleaned_data['name']
            em=fm.cleaned_data['email']
            pw=fm.cleaned_data['password']
            reg=User(name=nm,email=em,password=pw)
            reg.save()
            fm=UserRegistration()

    
    fm=UserRegistration()
    stud=User.objects.all()
    return render(request,'enroll/addandshow.html',{'form':fm,'st':stud})
    
def update_data(request,id):
    if request.method=='POST':
        pi=User.objects.get(pk=id)
        fm=UserRegistration(request.POST,instance=pi)
        if fm.is_valid():
            fm.save()
        p1=User.objects.get(pk=id)
        fm=UserRegistration(instance=p1)
        return render(request,'enroll/updatestudent.html',{'form':fm})
    
    else:
        p1=User.objects.get(pk=id)
        fm=UserRegistration(instance=p1)
        return render(request,'enroll/updatestudent.html',{'form':fm})

def delete_data(request,id):
    if request.method=='POST':
        p1=User.objects.get(pk=id)
        p1.delete()
        return HttpResponseRedirect('/')