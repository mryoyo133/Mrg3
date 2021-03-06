from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.http import HttpResponseRedirect
from django.urls import reverse
from api.models import User
# Create your views here.

def index(request):
    # Authenticated users view their inbox
    if request.user.is_authenticated:
        return render(request, "frontend/index.html")

    # Everyone else is prompted to sign in
    else:
        return HttpResponseRedirect(reverse("login-frontend"))

def register(request):
    if request.method == "POST":
        username = request.POST["username"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "frontend/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, username,password)
            user.save()
        except IntegrityError as e:
            print(e)
            return render(request, "frontend/register.html", {
                "message": "Username address already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index-frontend"))
    else:
        return render(request, "frontend/register.html")

def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index-frontend"))
        else:
            return render(request, "frontend/login.html", {
                "message": "Invalid email and/or password."
            })
    else:
        return render(request, "frontend/login.html")

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index-frontend"))
