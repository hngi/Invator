from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User, auth
from .models import Profile
from django.http import HttpResponse
from django.http import JsonResponse
# Create your views here.
def register_u(request):
    if request.method == "POST":
        full_name = request.POST['full_name']
        email = request.POST['email']
        job_type = request.POST['job_type']
        username = request.POST['username']
        password = request.POST['password']
        if User.objects.filter(username=username).exists():
            return JsonResponse("<p class='alert alert-danger' style='text-align:center'>Username already exists<p>", safe=False)
        elif User.objects.filter(email=email).exists():
            return JsonResponse("<p class='alert alert-danger' style='text-align:center'>E-mail already in use<p>", safe=False)
        else:
            user = User.objects.create_user(username=username, password=password, email=email, first_name=full_name)
            user.save()
            userp = User.objects.get(email=email)
            userp.profile.job_type = job_type
            userp.save()

            return JsonResponse("<p class='alert alert-success' style='text-align:center'>Registration successful<p>", safe=False)

def register(request):
    if request.method == "POST":
        full_name = request.POST['full_name']
        email = request.POST['email']
        job_type = request.POST['job_type']
        username = request.POST['username']
        password = request.POST['password']
        if User.objects.filter(username=username).exists():
            return JsonResponse("<p class='alert alert-danger' style='text-align:center'>Username already exists<p>", safe=False)
        elif User.objects.filter(email=email).exists():
            return JsonResponse("<p class='alert alert-danger' style='text-align:center'>E-mail already in use<p>", safe=False)
        else:
            user = User.objects.create_user(username=username, password=password, email=email, first_name=full_name)
            user.save()
            userp = User.objects.get(email=email)
            userp.profile.job_type = job_type
            userp.save()

            return JsonResponse("<p class='alert alert-success' style='text-align:center'>Registration successful<p>", safe=False)
    return render(request, "registration/signup.html")

def login(request):
    r_user = request.user
    if r_user.is_authenticated:
        return redirect("/dashboard")
    else:
        if request.method == "POST":
            password = request.POST['password']
            email = request.POST['email']

            try:
                c_user = User.objects.get(email=email)
                username = c_user.username
                user = auth.authenticate(username=username,password=password)
                if user is not None:
                    auth.login(request, user)
                    return JsonResponse("<p class='alert alert-success' style='text-align:center'>Login successful<p><script>window.location.href = '../dashboard';</script>", safe=False)
                    return redirect("/dashboard")
                else:
                    return JsonResponse("<p class='alert alert-danger' style='text-align:center'>User credentials not found<p>", safe=False)
            except:
                return JsonResponse("<p class='alert alert-danger' style='text-align:center'>Email address does not exist<p>", safe=False)
        return render(request, "registration/login.html")

def dashboard(request):
    r_user = request.user
    if r_user.is_authenticated:
        return render(request, "registration/dashboard.html")
    return redirect("/login")

def logout(request):
    auth.logout(request)
    return redirect("/dashboard")