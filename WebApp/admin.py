from django.contrib import admin
from .models import About, Flavour, MenuPDF, Contact, Nybro23Text
from django_summernote.admin import SummernoteModelAdmin


# Register your models here.
@admin.register(Flavour)
class AdminFlavour(admin.ModelAdmin):

    list_filter = ('order_ranking', 'category', 'name', 'allergens')
    list_display = ('name', 'order_ranking', 'category', 'display_flavour')
    actions = ['toggle_display']

    def toggle_display(self, request, queryset):
        for query in queryset:
            if query.display_flavour == 0:
                query.display_flavour = 1
            else:
                query.display_flavour = 0
            query.save()


@admin.register(Contact)
class AdminContact(admin.ModelAdmin):

    list_display = ('name', 'order_ranking', 'email', 'phone_number')


@admin.register(Nybro23Text)
class AdminUpdate(SummernoteModelAdmin):

    summernote_fields = ('content')


admin.site.register(About)
admin.site.register(MenuPDF)
