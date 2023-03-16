from django.db import models

# Create your models here.

    
class Appointment(models.Model):
    doctorname = models.CharField(max_length=50)
    patientname = models.CharField(max_length=50)
    patientemail = models.EmailField(max_length=50)
    phoneNumber=models.IntegerField
    appointmentdate = models.DateField(max_length=10)
    appointmentTime = models.IntegerField
    
    
    def __str__(self):
        return self.patientname+"you have appointment with" +self.doctorname  