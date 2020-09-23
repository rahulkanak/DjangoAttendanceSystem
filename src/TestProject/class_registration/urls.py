from django.urls import path
from . import views as class_reg_view

app_name = 'classreg'
urlpatterns = [
    path('addclass/', class_reg_view.add_class, name='add-class'),
    path('deleteclass/', class_reg_view.delete_class, name='delete-class'),
    path('viewclass/', class_reg_view.view_class, name='view-class'),
    path('addstudent/', class_reg_view.add_student, name='add-student'),
    path('deletestudent/', class_reg_view.delete_student, name='delete-student'),
    path('viewstudent/', class_reg_view.view_student, name='view-student'),
    path('updatestudent/<int:id>/', class_reg_view.add_student, name='update-student'),
    path('updateclass/<int:id>/', class_reg_view.add_class, name='update-class'),
    path('addcomment/<int:id>/', class_reg_view.add_comment, name='add-comment'),
    path('addcommentajax/', class_reg_view.add_comment_ajax, name='add-comment-ajax'),
    path('addfees/<int:id>/', class_reg_view.add_fees, name='add-fees'),
    path('addfeesajax/', class_reg_view.add_fees_ajax, name='add-fees-ajax'),
]