from . import views
from django.urls import path


urlpatterns = [
    path('booking/', views.ReservationView, name='booking')
]
