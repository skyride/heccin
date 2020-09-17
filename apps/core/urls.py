from django.urls import path

from .views import name_view


urlpatterns = [
    path("", name_view),
    path("<str:flag>", name_view)
]
