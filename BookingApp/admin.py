from django.contrib import admin
from .models import Reservation, ReservationAvail


# Register your models here.
@admin.register(Reservation)
class AdminReservation(admin.ModelAdmin):

    list_filter = ('date_and_time', 'name', 'created_on')
    search_fields = ['name', 'phone_number', 'email', 'created_on']
    list_display = ('name', 'party_size', 'date_and_time', 'created_on')


admin.site.register(ReservationAvail)