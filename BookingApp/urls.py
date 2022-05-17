from . import views
from django.urls import path


urlpatterns = [
    path('booking/', views.ReservationView, name='booking'),
    path('booking/delete/<str:pk>/', views.ReservationDeleteView, name='reservation_delete'),
]
