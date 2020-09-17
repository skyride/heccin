from django.urls import path

from .views import name_view, root_view


urlpatterns = [
    path("", root_view),
    path("<str:flag>", name_view)
]
