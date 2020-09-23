from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from .forms import StudentForm, SubjectForm, CommentsForm, FeesForm
from django.contrib import messages
from .models import Student, Subject
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
import sys


@login_required
def add_student(request,id=0):
    if request.method == 'GET':
        if id == 0:
            form = StudentForm()
        else:
            student = Student.objects.get(pk=id)
            form = StudentForm(instance=student)
            return render(request, 'class_registration/add_student.html', {'form': form})
    else:
        if id == 0:
            form = StudentForm(request.POST)
        else:
            student = Student.objects.get(pk=id)
            form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            student_name = f'{form.cleaned_data.get("first_name")} {form.cleaned_data.get("last_name")}'
            if id == 0:
                messages.success(request, f'{student_name} Added Successfully')
            else:
                messages.success(request, f'{student_name} Updated Successfully')
            return redirect('classreg:view-student')
    return render(request, 'class_registration/add_student.html', {'form':form})


@login_required
@csrf_exempt
def delete_student(request):
    student_id = request.POST.get('student_id')
    try:
        student = get_object_or_404(Student, pk=student_id)
        student.delete()
        return HttpResponse("OK")
    except:
        return HttpResponse("ERR")


@login_required
def view_student(request):
    obj = Student.objects.all()
    context = {
        'student_list': obj
    }
    return render(request, 'class_registration/view_student.html', context)


@login_required
def add_class(request, id=0):
    if request.method == 'GET':
        if id == 0:
            form = SubjectForm()
        else:
            subject = Subject.objects.get(pk=id)
            form = SubjectForm(instance=subject)
            return render(request, 'class_registration/add_class.html', {'form': form})
    else:
        if id == 0:
            form = SubjectForm(request.POST)
        else:
            subject = Subject.objects.get(pk=id)
            form = SubjectForm(request.POST, instance=subject)
        if form.is_valid():
            form.save()
            name = form.cleaned_data.get('class_name')
            if id == 0:
                messages.success(request, f'{name} Created Successfully')
            else:
                messages.success(request, f'{name} Updated Successfully')
            return redirect('classreg:view-class')
    return render(request, 'class_registration/add_class.html', {'form':form})


@login_required
def view_class(request):
    subject = Subject.objects.all()
    context = {
        'class_list': subject
    }
    return render(request, 'class_registration/view_class.html', context)


@login_required
@csrf_exempt
def delete_class(request):
    subject_id = request.POST.get('subject_id')
    try:
        subject = get_object_or_404(Subject, pk=subject_id)
        subject.delete()
        return HttpResponse("OK")
    except:
        return HttpResponse("ERR")


@login_required
def add_comment(request, id):
    student = get_object_or_404(Student, pk=id)
    comments = student.comments.all()
    if request.method == 'POST':
        form = CommentsForm(request.POST)
        context = {
            'form': form,
            'comments': comments
        }
        if form.is_valid():
            comment = form.save(commit=False)
            comment.student = student
            comment.save()
            return redirect('classreg:view-student')
    else:
        form = CommentsForm()
        context = {
            'form': form,
            'comments': comments
        }
    return render(request, 'class_registration/add_comment.html', context)


@login_required
@csrf_exempt
def add_comment_ajax(request):
    student_id = request.POST.get('student_id')
    return HttpResponse("OK")


@login_required
def add_fees(request, id):
    student = get_object_or_404(Student, pk=id)
    fees = student.fees.all()
    if request.method == 'POST':
        form = FeesForm(request.POST)
        context = {
            'form': form,
            'fees': fees
        }
        if form.is_valid():
            comment = form.save(commit=False)
            comment.student = student
            comment.save()
            return redirect('classreg:view-student')
    else:
        form = FeesForm()
        context = {
            'form': form,
            'fees': fees
        }
    return render(request, 'class_registration/add_fee.html', context)


@login_required
@csrf_exempt
def add_fees_ajax(request):
    student_id = request.POST.get('student_id')
    return HttpResponse("OK")

