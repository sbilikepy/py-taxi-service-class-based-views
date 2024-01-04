from django.urls import path

from .views import *

urlpatterns = [
    path("", index, name="index"),
    path("manufacturers/", ManufacturerListView.as_view(), name="manufacturers-list"),
    path("cars/", CarListView.as_view(), name="cars-list"),
    #cars/pk/ - car detail view;
    path("drivers/", DriverListView.as_view(), name="drivers-list"),
    #drivers/pk/ - driver detail view.
    #https://mate.academy/learn/django/django-class-based-generic-views?section=video&videoId=3131
]

app_name = "taxi"
