from django.shortcuts import render
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages


def home(request):
    # Check to see if user s logged in
    return render(request, 'home.html', {})


def logout_user(requeest):
    pass