from django.shortcuts import render
from .models import Options

def agendamento(request):
    options1 = options(request)
    return render(request, 'hair_salon/home.html', options1)

def options(request):
    options1_4 = Options.objects.all()[:4]
    options5_8 = Options.objects.all()[4:8]
    options9_12 = Options.objects.all()[8:12]
    return {'options1_4': options1_4, 'options5_8': options5_8, 'options9_12': options9_12}
