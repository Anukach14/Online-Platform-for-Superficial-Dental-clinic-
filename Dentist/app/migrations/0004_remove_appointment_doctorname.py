# Generated by Django 4.1.7 on 2023-03-16 18:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_delete_doctor'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appointment',
            name='doctorname',
        ),
    ]
