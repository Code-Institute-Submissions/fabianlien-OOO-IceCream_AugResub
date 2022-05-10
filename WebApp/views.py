from django.shortcuts import render
from django.views import generic, View
from .models import Flavour


# Create your views here.
class Main(generic.ListView):
    model = Flavour
    queryset = Flavour.objects.order_by('category', 'name')
    template_name = 'index.html'
