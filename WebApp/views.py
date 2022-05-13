from django.shortcuts import render
from django.views import generic, View
from .models import Flavour, About, MenuPDF, Contact


# Create your views here.
class MainPage(View):

    def get(self, request):
        about = About.objects.get(id=1)
        pdf_menu = MenuPDF.objects.get(id=1)
        flavour_list = Flavour.objects.order_by(
            'display_flavour',
            'order_ranking',
            'name'
            )
        contact_list = Contact.objects.order_by('order_ranking', 'name')
        return render(request, 'index.html', {
            'about': about,
            'flavour_list': flavour_list,
            'pdf_menu': pdf_menu,
            'contacts': contact_list
            })


class Nybrogatan23(View):

    def get(self, request):
        pdf_menu = MenuPDF.objects.get(id=1)
        return render(request, 'nybrogatan23.html', {
            'pdf_menu': pdf_menu,
        })
