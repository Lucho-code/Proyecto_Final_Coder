from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView

class Index(TemplateView):
    template_name = "index.html"

class Contacto(TemplateView):
    template_name = "contacto.html"

class AboutUs(TemplateView):
    template_name = 'about_us.html'

#def index(request):
    #return render(request, 'index.html')

#def contacto(request):
    #return render(request, 'contacto.html')

