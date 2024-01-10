from django.http import HttpRequest, HttpResponse
from django.shortcuts import render



def login_view(request: HttpRequest) -> HttpResponse:
    return render(request, "accounts/login.html")
