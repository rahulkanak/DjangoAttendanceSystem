# Generated by Django 3.0.3 on 2020-09-17 01:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('class_registration', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subject',
            name='student',
            field=models.ManyToManyField(related_name='student', to='class_registration.Student'),
        ),
    ]
