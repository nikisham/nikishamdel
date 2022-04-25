from django.shortcuts import render, redirect

from home.forms import ContactUs
from zakaz.models import Zakaz


def zakaz(request):
    product = Zakaz.objects.all()
    return render(request, 'zakaz.html', {"product":product})
