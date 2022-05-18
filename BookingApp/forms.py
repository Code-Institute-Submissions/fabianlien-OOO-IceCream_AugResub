from django import forms
from .models import Reservation


class DateInput(forms.DateInput):
    input_type = 'date'


class TimeInput(forms.TimeInput):
    input_type = 'time'


class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        widgets = {
            'date': DateInput(),
            'time': TimeInput()
            }
        fields = [
            'name',
            'party_size',
            'date',
            'time',
            'email',
            'phone_number',
            'message'
        ]


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ('message',)
