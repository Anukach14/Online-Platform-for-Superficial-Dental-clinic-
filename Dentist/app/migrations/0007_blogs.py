# Generated by Django 4.1.7 on 2023-03-16 21:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_appointment_age_appointment_appointmenttime'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blogs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('authname', models.CharField(max_length=50)),
                ('img', models.ImageField(blank=True, null=True, upload_to='pics')),
                ('timeStamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
