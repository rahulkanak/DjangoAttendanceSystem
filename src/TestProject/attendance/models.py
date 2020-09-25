from django.db import models
from datetime import datetime, date
from class_registration.models import Student, Subject


class AttendanceReport(models.Model):
    attendance_date = models.DateField()
    entry_date = models.DateField(default=date.today)
    comments = models.TextField(blank=True)
    subject = models.ForeignKey(Subject, related_name='attendance_subject', on_delete=models.CASCADE)

    def __str__(self):
        return '{0} {1}'.format(self.attendance_date, self.subject.class_name)


class Attendance(models.Model):
    status = models.CharField(max_length=1, choices=(('P', 'Present'), ('A', 'Absent'), ('T', 'Tardy')), default='P')
    entry_date = models.DateField(default=date.today)
    student = models.ForeignKey(Student, related_name='attendance_student', on_delete=models.CASCADE)
    attendance_report = models.ForeignKey(AttendanceReport, related_name='attendance_report', on_delete=models.CASCADE,null=True)

    def __str__(self):
        return '{0} {1}'.format(self.status, self.student.first_name)



