from django.shortcuts import render,redirect
from .models import Registration,StaffTb
from .forms import RegistrationForm,ProfileForm,StaffForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.db.models import Q

# Create your views here.

def Register(request):
    if request.method=="POST":
        UserRegitser=RegistrationForm(request.POST,request.FILES)
        if UserRegitser.is_valid():
            rtb=Registration()
            rtb.Date=UserRegitser.cleaned_data['Date']
            rtb.CustomerName=UserRegitser.cleaned_data['CustomerName']
            rtb.AnyDeskId = UserRegitser.cleaned_data['AnyDeskId']
            rtb.ApplicationDetails = UserRegitser.cleaned_data['ApplicationDetails']
            rtb.Requirements = UserRegitser.cleaned_data['Requirements']
            rtb.Status = UserRegitser.cleaned_data['Status']
            rtb.CompletionDate = UserRegitser.cleaned_data['CompletionDate']
            rtb.Staff = UserRegitser.cleaned_data['Staff']
            rtb.save()

            messages.success(request, "Your Registration is Succesfull")
            return redirect('/')
        else:
            print(UserRegitser.errors)
            return render(request, 'Registration.html', {'data': UserRegitser})
    else:
        UserRegitser = RegistrationForm()
        user = Registration.objects.all().order_by('-id')
        us = StaffTb.objects.all()


    return render(request, 'Registration.html', {'data': UserRegitser,'user':user,'us':us})

def Delete(request,id):
    user=Registration.objects.filter(id=id)
    user.delete()
    return redirect('/')

def Profile(request,id):
    user=Registration.objects.get(id=id)
    form=ProfileForm(request.POST or None,request.FILES or None,instance=user)
    if form.is_valid():
        form.save()
        messages.success(request,'Updated sucessfully...')
        return  redirect('/')
    return  render(request,'Profile.html',{'form':form,'user':user})

def Staff(request):
    if request.method=="POST":
        userStaff = StaffForm(request.POST,request.FILES)
        if userStaff.is_valid():
            stf=StaffTb()
            stf.Name=userStaff.cleaned_data['Name']
            stf.DateOfBirth=userStaff.cleaned_data['DateOfBirth']
            stf.Address=userStaff.cleaned_data['Address']
            stf.save()
            messages.success(request,'stored sucessfully...')
            return ('/')
        else:
            print(userStaff.errors)
            return  render(request,'staff.html',{'data':userStaff})
    else:
        userStaff=StaffForm()
        return  render(request,'staff.html',{'data':userStaff})




