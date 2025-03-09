from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    # int can be: int | str | slug | uuid
    # can use regex too for optional parameters or what not
    path("ping_frontend/<int:id>/", views.ping_frontend, name="ping_frontend"),
    path("test/", views.someView, name="whatdoesthisnamedo"),
    # actual endpoints
    path("get_winrate_data_by_id/<str:id>/", views.get_winrate_data_by_id, name="get_winrate_data_by_id"),
]