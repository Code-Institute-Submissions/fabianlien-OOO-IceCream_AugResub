from django.contrib import admin
from .models import About, Flavour, MenuPDF, Contact


# Register your models here.
@admin.register(Flavour)
class AdminContent(admin.ModelAdmin):

    list_filter = ('category', 'name', 'allergens')
    list_display = ('name', 'category', 'allergens')


admin.site.register(About)
admin.site.register(MenuPDF)
admin.site.register(Contact)

