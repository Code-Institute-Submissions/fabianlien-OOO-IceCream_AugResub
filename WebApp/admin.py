from django.contrib import admin
from .models import About, Flavour, MenuPDF, Contact


# Register your models here.
@admin.register(Flavour)
class AdminContent(admin.ModelAdmin):

    list_filter = ('order_ranking', 'category', 'name', 'allergens')
    list_display = ('name', 'order_ranking', 'category', 'display_flavour')
    actions = ['toggle_display']



admin.site.register(About)
admin.site.register(MenuPDF)
admin.site.register(Contact)

