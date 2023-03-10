from django.db import models

# Create your models here.
class Doctor(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=16)
    specialization = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name
    
class Appointment(models.Model):
    doctorname = models.CharField(max_length=50)
    patientname = models.CharField(max_length=50)
    patientemail = models.EmailField(max_length=50)
    appointmentdate = models.DateField(max_length=10)
    symptoms = models.CharField(max_length=100)
    status = models.BooleanField()
    
    def __str__(self):
        return self.patientname+"you have appointment with" +self.doctorname  