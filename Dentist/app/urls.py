from django.urls import path
from app import views
urlpatterns = [
    path('',views.index,name='index'),
    path('Doctors',views.Doctors,name='Doctors'),
    path('Treatments',views.Treatments,name='Treatments'),
    path('Blog',views.Blog,name='Blog'),
    path('About',views.About,name='About'),
    path('Contact',views.Con,name='Con'),
    path('Login',views.handleLogin,name='handleLogin'),
    path('signup',views.handlesignup,name='handlesignup'),
    path('Appointment',views.App,name='App'),
    path('MyAppointments',views.MyAppointments,name='MyAppointments'),
    
]