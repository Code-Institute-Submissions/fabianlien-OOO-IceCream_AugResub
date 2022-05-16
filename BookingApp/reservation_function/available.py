import datetime
from BookingApp.models import *

def check_available(table, date_and_time, end_reservation):
    avail_params[]
    reservations = Reservation.objects.filter(table=table)
    for res in reservations:
        if res.date_and_time > end_reservation