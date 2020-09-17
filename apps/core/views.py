from django.http.request import HttpRequest
from django.conf import settings
from django.shortcuts import render


def name_view(request: HttpRequest):
    suffix = settings.DOMAIN_SUFFIX
    subdomain = request.get_host().split(":")[0].replace(suffix, "")

    return render(
        request,
        "core/name.html",
        context={
            "name": subdomain.title(),
            "state": "gay",
            "style": "pride-rainbow"})
