from . import views
from django.urls import path


urlpatterns = [
    path('booking/', views.ReservationView, name='booking'),
    path('profile/', views.Profile.as_view(), name='profile'),
    path(
        'booking/delete/<str:pk>/',
        views.ReservationDeleteView,
        name='reservation_delete'
        ),
    path(
        'edit_reservation/<str:pk>/',
        views.Profile.as_view(),
        name='edit_reservation'
        )
]
