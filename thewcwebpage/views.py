from django.shortcuts import render, redirect
# from django.contrib.auth import authenticate, login, logout
# from django.contrib import messages
# from .forms import RegisterForm, AddRecordForm
# from .models import Record

# Create your views here.
def home(request):
    return render(request, 'home.html')