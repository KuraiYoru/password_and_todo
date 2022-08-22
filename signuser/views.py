from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate
from .forms import MyUserCreationForm


# from django.contrib.auth.decorators import login_required


def signupuser(request):
    if request.method == 'GET':
        return render(request, 'signuser/signuser.html', {'form': MyUserCreationForm()})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('/mytodos')
            except IntegrityError:
                return render(request, 'signuser/signuser.html', {'form': MyUserCreationForm(),
                                                                'error': 'That username has already been taken. Please choose a new username'})
        else:
            return render(request, 'signuser/signuser.html',
                          {'form': MyUserCreationForm(), 'error': 'Passwords did not match'})




def logoutuser(request):
    if request.method == 'POST':
        logout(request)
        return redirect('/home')


def loginuser(request):
    if request.method == 'GET':
        return render(request, 'signuser/login.html', {'form': AuthenticationForm()})
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'signuser/login.html',
                          {'form': AuthenticationForm(), 'error': 'Username and password did not match'})
        else:
            login(request, user)
            return redirect('/home')
