from django import forms
from .models import Attendance


class DateInput(forms.DateInput):
    input_type = 'date'


STATUS_CHOICES= [
    ('P', 'Present'),
    ('A', 'Absent'),
    ('T', 'Tardy'),
    ]


class AttendanceForm(forms.ModelForm):
    class Meta:
        model = Attendance
        fields = ('attendance_date', 'status', 'student', 'subject')
        widgets = {
            'attendance_date': DateInput(),
            'subject': forms.HiddenInput(),
        }

    def __init__(self, *args, **kwargs):
        super(AttendanceForm, self).__init__(*args, **kwargs)
        self.fields['student'].empty_label = None
        # self.fields['subject'].empty_label = 'select'




