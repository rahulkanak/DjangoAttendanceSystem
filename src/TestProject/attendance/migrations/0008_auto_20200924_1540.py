# Generated by Django 3.0.3 on 2020-09-24 21:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0007_auto_20200922_1019'),
    ]

    operations = [
        migrations.RenameField(
            model_name='attendance',
            old_name='attendance',
            new_name='attendance_report',
        ),
    ]
