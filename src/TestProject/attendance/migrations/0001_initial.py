# Generated by Django 3.0.3 on 2020-09-16 17:09

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('class_registration', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attendance_date', models.DateField(blank=True, default=datetime.datetime.now)),
                ('status', models.CharField(choices=[('P', 'Present'), ('A', 'Absent'), ('T', 'Tardy')], default='P', max_length=1)),
                ('entry_date', models.DateTimeField(default=datetime.datetime.now)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='class_registration.Student')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='class_registration.Subject')),
            ],
        ),
    ]
