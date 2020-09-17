from django.http.request import HttpRequest
from django.shortcuts import render


def name_view(request: HttpRequest):
    return render(request, "core/index.html")
