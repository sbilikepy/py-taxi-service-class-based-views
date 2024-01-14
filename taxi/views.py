from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views import generic
from taxi.models import Driver, Car, Manufacturer


def index(request):
    """View function for the home page of the site."""

    num_visits = request.session.get("num_visits", 0)
    request.session["num_visits"] = num_visits + 1

    context = {
        "num_drivers": Driver.objects.count(),
        "num_cars": Car.objects.count(),
        "num_manufacturers": Manufacturer.objects.count(),
        "num_visits": request.session["num_visits"],
    }

    return render(request, "taxi/index.html", context=context)


def test_session_view(request: HttpRequest) -> HttpResponse:
    # request.session["book"] = "test session book" #dict
    return HttpResponse(
        "<h1>Session</h1>" f"<h4>Session data: {request.session['book']}</h4>"
    )


class ManufacturerListView(generic.ListView):
    model = Manufacturer
    queryset = Manufacturer.objects.all()
    paginate_by = 5
    template_name = "taxi/manufacturer_list.html"


class CarListView(generic.ListView):
    model = Car
    queryset = Car.objects.select_related("manufacturer")
    paginate_by = 5
    template_name = "taxi/car_list.html"


class CarDetailView(generic.DetailView):
    model = Car


class DriverListView(generic.ListView):
    model = Driver
    paginate_by = 5
    template_name = "taxi/driver_list.html"


class DriverDetailView(generic.DetailView):
    model = Driver
    queryset = Driver.objects.prefetch_related("cars__manufacturer")
