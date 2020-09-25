from django.urls import path
from attendance import views as attn_view

app_name='attendance'
urlpatterns = [
    path('getdata/',attn_view.get_attendance_set, name='add-attendance'),
    path('subjects/',attn_view.subject_for_attendance, name='subject-attendance'),
    path('saveattendance/',attn_view.save_attendance_set, name='save-attendance'),
    path('savecomment/', attn_view.save_comment, name='save-comment'),
    path('getsavedattendance/',attn_view.get_saved_attendance, name='saved-attendance'),
    path('studentview/',attn_view.student_view, name='student-view'),
    path('studentattendance/',attn_view.student_attendance_view, name='student-attendance-view'),
    path('studentattendancedates/', attn_view.student_attendance_dates, name='student-attendance-dates'),
]