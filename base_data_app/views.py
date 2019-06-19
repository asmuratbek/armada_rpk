from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.urls import reverse

from base_data_app.models import Services, Department, FeedBack, AboutUs, Key, Blog


def index(request):
    services = Services.objects.all()
    departments = Department.objects.all()
    return render(request, 'index.html', locals())


def service(request, id):
    service = Services.objects.get(id=id)
    return render(request, 'service.html', locals())


def send_call_back(request):
    name = request.GET.get('name')
    phone = request.GET.get('phone')
    callback = FeedBack()
    callback.name = name
    callback.phone = phone
    callback.save()
    name = 'Моё имя: ' + str(name) + '\n'
    phone = 'Мой номер: ' + str(phone) + '\n'
    send_mail('Заявка с сайта ', name + phone,
              'asnotifications@gmail.com',
              ['armada.kg@gmail.com'])
    return HttpResponseRedirect(reverse('thanks'))


def thanks(request):
    return render(request, 'thanks.html')


def about_company(request):
    object = AboutUs.objects.first()
    return render(request, 'about.html', locals())


def get_project_in_key(request):
    object = Key.objects.first()
    return render(request, 'get_key.html', locals())

def blog_list(request):
    objects = Blog.objects.all()
    return render(request, 'blog.html', locals())
