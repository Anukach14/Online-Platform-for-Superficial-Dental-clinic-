from django.db import models


# Create your models here.

    
class Appointment(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    age = models.PositiveBigIntegerField(null=True,blank=True)
   
    appointmentdate = models.DateField(max_length=10)
    appointmentTime = models.TimeField(null=True,blank=True)
    
    
    def __str__(self):
        return self.patientname+"you have appointment with" +self.doctorname  