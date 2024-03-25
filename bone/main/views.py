from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from django.contrib.auth.models import Group
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,login,logout
from main import forms
# Create your views here.


def main(request):
    return render(request,'main.html')

#PATIENT VIEW
def patient_signup_view(request):
    userForm=forms.PatientUserForm()
    patientForm=forms.PatientForm()
    mydict={'userForm':userForm,'patientForm':patientForm}
    if request.method=='POST':
        userForm=forms.PatientUserForm(request.POST)
        patientForm=forms.PatientForm(request.POST)
        if userForm.is_valid() and patientForm.is_valid():
            user=userForm.save()
            user.set_password(user.password)
            user.save()
            patient=patientForm.save(commit=False)
            patient.user=user
            patient.save()
            my_patient_group = Group.objects.get_or_create(name='PATIENT')
            my_patient_group[0].user_set.add(user)
        return HttpResponseRedirect('/plog')
  
    return render(request,'patientsignup.html',context=mydict)

def patient_login_view(request):
    if request.method=='POST':
        form = AuthenticationForm(request,data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username,password=password)
            if user is not None :
                login(request,user) 
                return redirect('/pdash')
            else:
                return redirect('/plog')
        else:
            return redirect('/plog')  
    form = AuthenticationForm()
    context = {'form':form}
    return render(request,'patientlogin.html',context)


def pat_dashboard(request):
    return render(request,'patient_dhashboard.html')



#DOCTOR VIEW
def doctor_signup_view(request):
    userForm=forms.DoctorUserForm()
    DoctorForm=forms.DoctorForm()
    mydict={'userForm':userForm,'DoctorForm':DoctorForm}
    if request.method=='POST':
        userForm=forms.DoctorUserForm(request.POST)
        DoctorForm=forms.DoctorForm(request.POST)
        if userForm.is_valid() and DoctorForm.is_valid():
            user=userForm.save()
            user.set_password(user.password)
            user.save()
            Doctor=DoctorForm.save(commit=False)
            Doctor.user=user
            Doctor.save()
            my_Doctor_group = Group.objects.get_or_create(name='DOCTOR')
            my_Doctor_group[0].user_set.add(user)
        return HttpResponseRedirect('/dlog')
  
    return render(request,'doctorsignup.html',context=mydict)




def doctor_login_view(request):
    if request.method=='POST':
        form = AuthenticationForm(request,data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username,password=password)
            if user is not None :
                login(request,user) 
                return redirect('/ddash')
            else:
                return redirect('/dlog')
        else:
            return redirect('/dlog')  
    form = AuthenticationForm()
    context = {'form':form}
    return render(request,'doctorlogin.html',context)

def doc_dashboard(request):
    return render(request,'doctor_dhashboard.html')







def logout_req(request):
    logout(request)
    return redirect('/')
