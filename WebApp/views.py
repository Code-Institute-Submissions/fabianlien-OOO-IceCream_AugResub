from django.shortcuts import render
from django.views import View
from .models import *


class MainPage(View):
    '''
    Renders the homepage and provides requests
    for all CMS-related template content.
    '''
    def get(self, request):
        about = About.objects.get(id=1)
        pdf_menu = MenuPDF.objects.get(id=1)
        flavour_list = Flavour.objects.order_by(
            'display_flavour',
            'order_ranking',
            'name'
            )
        nybrogatan23_framed_image = Nybro23Image.objects.get(order_ranking=1)
        contact_list = Contact.objects.order_by('order_ranking', 'name')
        return render(request, 'index.html', {
            'about': about,
            'flavour_list': flavour_list,
            'pdf_menu': pdf_menu,
            'contacts': contact_list,
            'nybrogatan23_framed': nybrogatan23_framed_image
            })


class Nybrogatan23(View):
    '''
    Renders the Nybrogatan23 page and provides requests
    for all CMS-related template content.
    '''
    def get(self, request):
        pdf_menu = MenuPDF.objects.get(id=1)
        text_content = Nybro23Text.objects.get(id=1)
        image_list = Nybro23Image.objects.order_by('order_ranking', 'name')
        contact_list = Contact.objects.order_by('order_ranking', 'name')
        return render(request, 'nybrogatan23.html', {
            'pdf_menu': pdf_menu,
            'text_content': text_content,
            'images': image_list,
            'contacts': contact_list
        })
