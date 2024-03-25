from django.db import models
from django.contrib.auth.models import User

GENDER_CHOICES = (
   ('Male', 'Male'),
   ('Female', 'Female')
)

class Patient(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    gender = models.CharField(choices=GENDER_CHOICES, max_length=8)
    age=models.PositiveIntegerField()
    address = models.CharField(max_length=40)
    mobile = models.CharField(max_length=20,null=False)
    pos = models.CharField(max_length=10,default="Patient")



SPECIALIST = (
   ('Anemia', 'Anemia'),
   ('Deep vein thrombosis', 'Deep vein thrombosis'),
   ('lymphoma', 'lymphoma'),
   ('Sepsis', 'Sepsis'),
   ('Hemophilia', 'Hemophilia'),
)

class Doctor(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    gender = models.CharField(choices=GENDER_CHOICES, max_length=8)
    mobile = models.CharField(max_length=20,null=False)
    specialist = models.CharField(choices=SPECIALIST, max_length=25)
    pos = models.CharField(max_length=10,default="Doctor")