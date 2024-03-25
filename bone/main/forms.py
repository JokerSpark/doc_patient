from django import forms
from django.contrib.auth.models import User
from . import models


#PATIENT FORM
class PatientUserForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['first_name','last_name','username','password']
        widgets = {
        'password': forms.PasswordInput()
        }

class PatientForm(forms.ModelForm):
    
    class Meta:
        model=models.Patient
        fields=['gender','age','address','mobile']
        






#DOCTOR FORM
class DoctorUserForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['first_name','last_name','username','password']
        widgets = {
        'password': forms.PasswordInput()
        }

class DoctorForm(forms.ModelForm):
    
    class Meta:
        model=models.Doctor
        fields=['gender','mobile','specialist']
        