# Generated by Django 3.0.3 on 2020-09-16 04:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=20)),
                ('parent', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('class_name', models.CharField(max_length=50)),
                ('student', models.ManyToManyField(to='class_registration.Student')),
            ],
        ),
        migrations.CreateModel(
            name='StudentComments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField()),
                ('date_added', models.DateTimeField(auto_now_add=True, verbose_name='Comment Added On')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='class_registration.Student')),
            ],
        ),
    ]
