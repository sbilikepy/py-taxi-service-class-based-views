from django.urls import path

from .views import *

urlpatterns = [
    path("", index, name="index"),
    path("manufacturers/", ManufacturerListView.as_view(), name="manufacturers_list"),
    path("cars/", CarListView.as_view(), name="cars_list"),
    #cars/pk/ - car detail view;
    path("drivers/", DriverListView.as_view(), name="drivers_list"),
    #drivers/pk/ - driver detail view.

]

app_name = "taxi"
