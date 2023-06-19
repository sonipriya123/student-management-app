from django.shortcuts import render,redirect
from .models import simsdata

def sims(request):
    data=simsdata.objects.all()
    return render(request,'sims.html',{'data':data})
def display(request):
    if request.method=='GET':
        return render(request,'display.html')
    else:
        simsdata(
        firstname=request.POST['fname'],
        lastname=request.POST['lname'],
        mobile=request.POST['mobile'],
        email=request.POST['email'],
        ).save()
        return redirect('sims')
def update(request,id):
    data=simsdata.objects.get(id=id)
    if request.method=='GET':
        return render(request,'update.html',{'abcd':data})
    else:
        data.firstname=request.POST['fname']
        data.lastname=request.POST['lname']
        data.mobile=request.POST['mobile']
        data.email=request.POST['email']
        data.save()
        return redirect('sims')
def delete(request,id):
    data=simsdata.objects.get(id=id)
    data.delete()
    return redirect('sims')
