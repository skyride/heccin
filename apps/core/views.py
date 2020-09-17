from django.http import Http404
from django.http.request import HttpRequest
from django.shortcuts import render

from .utils import get_name_from_host


FLAG_STYLE_MAP = {
    "pride": "pride-rainbow",
    "nb": "pride-nb",
    "lesbian": "pride-lesbian-v2"
}


def name_view(request: HttpRequest, flag: str = "pride"):
    # Check the flag is valid
    if flag not in FLAG_STYLE_MAP:
        raise Http404("We don't know that flag :(")

    name = get_name_from_host(request.get_host())    
    state = "gay" if flag in ["pride", "lesbian"] else "valid"

    return render(
        request,
        "core/name.html",
        context={
            "name": name,
            "state": state,
            "style": FLAG_STYLE_MAP[flag]})
