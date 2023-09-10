from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import *


# Create your views here.
def index(request):
    return render(request, "index.html")


def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            messages.success(
                request, f"Hi {username}, your account was created successfully!"
            )

            return redirect("users:index")
    else:
        form = UserRegisterForm()

    return render(request, "register.html", {"form": form})


def login(request):
    return render(request, "login.html")


def profile(request):
    if request.method == "POST":
        form = AccountChangeForm(request.user, data=request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            messages.success(
                request, f"Hi {username}, your account was updated successfully!"
            )

            return redirect("users:index")
    else:
        form = AccountChangeForm(request.user)
    open_form = True
    return render(request, "profile.html", {"form": form})


def changeUsernamePassword(request):
    if request.method == "POST":
        form = AccountChangeForm(request.user, data=request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            messages.success(
                request, f"Hi {username}, your account was updated successfully!"
            )

            return redirect("users:index")
    else:
        form = AccountChangeForm(request.user)
    open_form = True
    return render(request, "updateAccount.html", {"open_form": open_form, "form": form})


def changeFirstLastName(request):
    if request.method == 'POST':
        form = UserInfoChangeForm(data=request.POST)
        if form.is_valid():
            form.save()
            firstname = form.cleaned_data.get("first_name")
            lastname = form.cleaned_data.get("last_name")
            messages.success(
                request, f"Hi {firstname} {lastname}, your account was updated successfully!"
            )

    else:
        form = UserInfoChangeForm(request.user)
    open_form = True
    return render(request, "updateAccount.html", {"form": form})
