from django.db import models


# Create your models here.

    
class Appointment(models.Model):
    name = models.CharField(max_length=50)  # Added a name field
    email = models.EmailField(max_length=50)
    age = models.PositiveBigIntegerField(null=True, blank=True)
    phoneNumber = models.CharField(max_length=15, null=True, blank=True)
    appointmentdate = models.DateField(max_length=10)
    appointmentTime = models.TimeField(null=True, blank=True)

    def __str__(self):
        return self.name + " - Your Appointment is Confirmed"
class Blogs(models.Model): 
    title=models.CharField(max_length=100)
    description=models.TextField()
    authname=models.CharField(max_length=50) 
    img=models.ImageField(upload_to='pics',blank=True,null=True)
    timeStamp=models.DateTimeField(auto_now_add=True)  
    
    
    def __str__(self):
        return f'Uploaded by {self.authname} ' 
    
class Contact(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField(max_length=50)
    phoneNumber = models.CharField(max_length=15, null=True, blank=True)
    description=models.CharField(max_length=100,null=True, blank=True)
    
        