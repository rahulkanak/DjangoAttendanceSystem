from django import forms
from .models import Student, Subject, StudentComments, StudentFees


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'


class SubjectForm(forms.ModelForm):
    student = forms.ModelMultipleChoiceField(required=False, widget=forms.SelectMultiple,
                                             queryset=Student.objects.all()
                                             )

    class Meta:
        model = Subject
        fields = '__all__'


class CommentsForm(forms.ModelForm):
    class Meta:
        model = StudentComments
        fields = [
            'comment'
        ]


class FeesForm(forms.ModelForm):
    fees = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Fees'}))

    class Meta:
        model = StudentFees
        fields = [
            'fees'
        ]
