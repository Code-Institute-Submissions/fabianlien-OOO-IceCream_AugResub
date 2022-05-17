from django.shortcuts import render
from .forms import ReservationForm
from .models import Reservation
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


# Create your views here.
@login_required(login_url='login')
def ReservationView(request):

    form = ReservationForm(request.POST or None)
    if form.is_valid():
        user = User.objects.get(username=request.user.username)
        reservation = form.save(commit=False)
        reservation.user = user
        reservation.save()
        form = ReservationForm()

    return render(request, 'booking.html', {
        'form': form
    })
