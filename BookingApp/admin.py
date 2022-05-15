from django.contrib import admin
from .models import Reservation


# Register your models here.
@admin.register(Reservation)
class AdminReservation(admin.ModelAdmin):

    list_filter = ('date', 'time', 'name', 'created_on')
    search_fields = ['name', 'phone_number', 'email', 'created_on']
    list_display = ('name', 'time', 'party_size', 'date', 'created_on')
