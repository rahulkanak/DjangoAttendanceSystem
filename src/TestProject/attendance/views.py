from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from class_registration.models import Student, Subject
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from crispy_forms.helper import FormHelper, Layout
import json, sys
from .models import Attendance, AttendanceReport


class MyFormSetHelper(FormHelper):
    def __init__(self, *args, **kwargs):
        super(MyFormSetHelper, self).__init__(*args, **kwargs)
        self.layout = Layout(
            'field1',
            'field2',
            'field3'
        )
        self.template = 'bootstrap/table_inline_formset.html'


@csrf_exempt
def get_attendance_set(request):
    subject_id = request.POST.get('subject')
    # print(subject_id)
    subject = Subject.objects.filter(pk=subject_id)
    students = subject[0].student.all()
    print(students.count())
    # student_data = serialize('python', student)
    student_data = []
    for student in students:
        stud_dict = {"id": student.id, "name":student.first_name+" "+student.last_name}
        student_data.append(stud_dict)

    return JsonResponse(json.dumps(student_data), content_type='application/json', safe=False)


@login_required
def subject_for_attendance(request):
    subjects = Subject.objects.all()
    context = {'subjects': subjects}
    return render(request, 'attendance/subject_attendance.html', context)


@csrf_exempt
def save_attendance_set(request):
    attendance_data = request.body
    attendance_data = json.loads(attendance_data)
    # print(attendance_data)
    subject_id = attendance_data[0].get('subject_id')
    subject_model = Subject.objects.get(pk=subject_id)
    attendance_date = attendance_data[0].get('date')
    comments = attendance_data[0].get('comments')
    attendance_report = AttendanceReport(subject=subject_model, comments = comments, attendance_date=attendance_date)
    attendance_report.save()
    try:
        for data in attendance_data:
            student_id = data.get('student_id')
            student_model = Student.objects.get(pk=student_id)
            status = data.get('status')
            attendance = Attendance(attendance=attendance_report, student=student_model, status=status)
            attendance.save()
    except:
        return HttpResponse("ERR")
    return HttpResponse("OK")


@csrf_exempt
def get_saved_attendance(request):
    attendance_date = request.POST.get('attendance_date')
    subject_id = request.POST.get('subject_id')
    # print(subject_id+" - "+attendance_date)
    subject_obj = Subject.objects.get(pk=subject_id)
    attendance = AttendanceReport.objects.filter(subject=subject_obj, attendance_date=attendance_date)
    # print(attendance)
    if attendance:
        comment = attendance[0].comments
        attendance_report = Attendance.objects.filter(attendance=attendance[0])
        # print(attendance_report.count())
        # student_data = serialize('python', student)
        attendance_data = []
        for report in attendance_report:
            stud_dict = {"comment": comment, "status": report.status, "student_id": report.student.id}
            attendance_data.append(stud_dict)
        # print(attendance_data)
        return JsonResponse(json.dumps(attendance_data), content_type='application/json', safe=False)
    else:
        return HttpResponse("ERR")


@csrf_exempt
def save_comment(request):
    subject_id = request.POST.get('subject_id')
    subject_model = Subject.objects.get(pk=subject_id)
    attendance_date = request.POST.get('attendance_date')
    comments = request.POST.get('comments')
    try:
        attendance_report = AttendanceReport.objects.get(subject=subject_model, attendance_date=attendance_date)
        # print(comments)
        # print(attendance_report)
        attendance_report.comments = comments
        attendance_report.save(update_fields=['comments'])
        return HttpResponse("OK")
    except:
        print("Unexpected error:", sys.exc_info()[0])
        return HttpResponse("ERR")


