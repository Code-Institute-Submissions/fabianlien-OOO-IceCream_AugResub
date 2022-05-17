from django import forms
from BookingApp.models import Reservation


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ('message',)
