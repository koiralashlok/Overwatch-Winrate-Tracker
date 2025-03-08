from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("ping_frontend", views.ping_frontend, name="ping_frontend"),
    path("test", views.someView, name="whatdoesthisnamedo"),
]