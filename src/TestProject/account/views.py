from django.shortcuts import render, redirect
from .admin import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required


def register(request):
    method = request.method
    if method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            form.save()
            messages.success(request, f'{username}, Your account has been created!')
            return redirect('account:user-login')
    else:
        form = UserCreationForm()
        return render(request, 'account/register.html',{'form': form})


@login_required
def home(request):
    return render(request,'account/home.html',{})


