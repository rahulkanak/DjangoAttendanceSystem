from django.db import models
from django.urls import reverse


class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    parent = models.CharField(max_length=150)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Subject(models.Model):
    class_name = models.CharField(max_length=50)
    student = models.ManyToManyField('Student', related_name='student')

    def __str__(self):
        return f'{self.class_name}'


class StudentComments(models.Model):
    student = models.ForeignKey(Student, related_name="comments", on_delete=models.CASCADE)
    comment = models.TextField()
    date_added = models.DateTimeField(verbose_name="Comment Added On", auto_now_add=True)


class StudentFees(models.Model):
    student = models.ForeignKey(Student, related_name="fees", on_delete=models.CASCADE)
    fees = models.TextField()
    date_added = models.DateTimeField(verbose_name="Fees Added On", auto_now_add=True)
