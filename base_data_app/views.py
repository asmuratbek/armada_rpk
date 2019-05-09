from django.shortcuts import render

# Create your views here.
from base_data_app.models import Services


def index(request):
    services = Services.objects.all()
    return render(request, 'index.html', locals())


def service(request, id):
    service = Services.objects.get(id=id)
    return render(request, 'service.html', locals())
