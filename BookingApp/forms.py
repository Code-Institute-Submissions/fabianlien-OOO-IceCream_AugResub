from django import forms
from .models import Reservation


class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = [
            'name',
            'party_size',
            'date',
            'time',
            'email',
            'phone_number',
            'message'
        ]
