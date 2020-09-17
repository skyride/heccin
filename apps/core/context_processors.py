from django.conf import settings
from django.http.request import HttpRequest


def ga_code(request: HttpRequest):
    return {"GA_CODE": settings.GA_CODE}
