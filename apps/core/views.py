from django.http.request import HttpRequest
from django.shortcuts import render

from .utils import get_name_from_host


def name_view(request: HttpRequest):
    name = get_name_from_host(request.get_host())

    return render(
        request,
        "core/name.html",
        context={
            "name": name,
            "state": "gay",
            "style": "pride-rainbow"})
