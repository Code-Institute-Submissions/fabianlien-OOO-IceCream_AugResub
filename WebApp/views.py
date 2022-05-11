from django.shortcuts import render, get_list_or_404
from django.views import generic, View
from .models import Flavour, About


# Create your views here.
class MainPage(View):

    def get(self, request, *args, **kwargs):
        about = About.objects.get(id=1)
        flavour_list = Flavour.objects.order_by('category', 'name')
        return render(request, 'index.html', {
            "about": about,
            "flavour_list": flavour_list
            })
