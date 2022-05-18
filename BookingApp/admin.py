from django.contrib import admin
from .models import Reservation


@admin.register(Reservation)
class AdminReservation(admin.ModelAdmin):

    list_filter = ('date_and_time', 'reservation_status', 'name', 'created_on')
    search_fields = ['name', 'phone_number', 'email', 'created_on']
    list_display = (
        'reservation_status',
        'name',
        'party_size',
        'date_and_time',
        'created_on'
        )
    actions = ['toggle_reservation_status']

    def toggle_reservation_status(self, request, queryset):
        for query in queryset:
            if query.reservation_status == 0:
                query.reservation_status = 1
            else:
                query.reservation_status = 0
            query.save()
