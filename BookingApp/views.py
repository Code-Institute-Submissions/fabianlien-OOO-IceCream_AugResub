from django.shortcuts import render, redirect
from .forms import ReservationForm
from .models import Reservation
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages


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
        messages.success(
            request, 'Your request has been registered, the restaurant will email you to confirm!')

    return render(request, 'booking.html', {
        'form': form
    })


@login_required(login_url='login')
def ReservationDeleteView(request, pk):
    reservation = Reservation.objects.get(pk=pk)
    reservation.delete()
    messages.success(
        request, 'Your reservation has been deleted!')
    return redirect('profile')