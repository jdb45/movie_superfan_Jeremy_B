from django.db import transaction

from .models import *
from .forms import UserRegistrationForm

from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import update_session_auth_hash
from django.shortcuts import render, redirect


def register(request):

    if request.method == 'POST':

        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            user = authenticate(
                username=request.POST['username'],
                password=request.POST['password1'])
            login(request, user)
            return redirect('homepage')

        else:
            message = 'Please check the data you entered'
            return render(request, 'registration/register.html',
                          {'form': form, 'message': message})

    else:
        form = UserRegistrationForm()
        return render(request, 'registration/register.html', {'form': form})


def user_profile(request, user_pk):

    user = User.objects.get(pk=user_pk)


    return render(request, 'movie_superfan/users/user_profile.html',
                  {'user': user})
