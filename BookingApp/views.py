from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import ProfileForm, ReservationForm
from .models import Reservation


class Profile(View):

    def get(self, request):
        user = User.objects.get(username=request.user.username)
        user_reservations = Reservation.objects.filter(user=user)
        return render(request, 'profile.html', {
            'user': user,
            'reservations': user_reservations,
            'form': ProfileForm,
        })

    def post(self, request, pk):
        user = User.objects.get(username=request.user.username)
        user_reservations = Reservation.objects.filter(user=user).order_by('date_and_time')
        user_reservation = Reservation.objects.get(pk=pk)
        profile_form = ProfileForm(request.POST)
        if profile_form.is_valid():
            user_reservation.message = request.POST['message']
            user_reservation.save()
            messages.success(
                request, 'Your message has been updated!')
        else:
            profile_form = ProfileForm()

        return render(request, 'profile.html', {
            'user': user,
            'reservations': user_reservations,
            'form': ProfileForm,
        })


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
            request, 'Your request has been registered, the restaurant will contact you and confirm your reservation!')

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
