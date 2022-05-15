from django.shortcuts import render
from .forms import ReservationForm
from .models import Reservation
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required(login_url='login')
def ReservationView(request):

    form = ReservationForm(request.POST or None)
    if form.is_valid():
        form.save()

    return render(request, 'booking.html', {
        'form': form
    })
