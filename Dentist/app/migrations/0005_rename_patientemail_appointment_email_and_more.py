# Generated by Django 4.1.7 on 2023-03-16 19:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_remove_appointment_doctorname'),
    ]

    operations = [
        migrations.RenameField(
            model_name='appointment',
            old_name='patientemail',
            new_name='email',
        ),
        migrations.RenameField(
            model_name='appointment',
            old_name='patientname',
            new_name='name',
        ),
    ]
