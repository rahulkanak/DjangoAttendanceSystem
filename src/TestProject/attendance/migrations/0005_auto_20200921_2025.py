# Generated by Django 3.0.3 on 2020-09-22 02:25

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('class_registration', '0002_auto_20200916_1915'),
        ('attendance', '0004_auto_20200921_1828'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='attendance',
            name='attendance_date',
        ),
        migrations.RemoveField(
            model_name='attendance',
            name='comments',
        ),
        migrations.RemoveField(
            model_name='attendance',
            name='subject',
        ),
        migrations.CreateModel(
            name='AttendanceReport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attendance_date', models.DateField(default=datetime.datetime.now)),
                ('entry_date', models.DateField(default=datetime.date.today)),
                ('comments', models.TextField(blank=True)),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='attendance_subject', to='class_registration.Subject')),
            ],
        ),
    ]
