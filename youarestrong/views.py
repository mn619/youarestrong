from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import auth
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm

def about(request):
    return render(request, 'about.html')

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            # login the user
            user = form.get_user()
            login(request, user)

            return redirect('app:home')
    else:
        if request.user.is_authenticated:
            return redirect('app:home')

    return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/app')

def signup(request):
    print(request.POST)

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            print("okokokok\n")
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)

            user.first_name = request.POST['firstname']
            user.last_name = request.POST['lastname']
            user.email = request.POST['username']

            user.save()

            login(request, user)
        else:
            print("notokokok")

        return redirect('/app')
    else:
        form = UserCreationForm()
        return render(request, 'signup.html', {'form': form})