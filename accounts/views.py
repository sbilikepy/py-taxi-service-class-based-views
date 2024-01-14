from django.contrib.auth import login, authenticate, logout
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse


def login_view(request: HttpRequest) -> HttpResponse:
    if request.method == "GET":
        return render(request, template_name="accounts/login.html")
    elif request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(username=username, password=password)
        print(username, password, user)
        if user:
            login(request, user)
            print(f"{user} logged in")
            return HttpResponseRedirect(reverse("taxi:index"))
        return HttpResponse("POST")
    return HttpResponse("404")


def logout_view(request: HttpRequest) -> HttpResponse:
    logout(request)
    return render(request, "accounts/logged_out.html")
