from . import views
from django.urls import path


urlpatterns = [
    path('', views.MainPage.as_view(), name='home'),
    path('nybrogatan23/', views.Nybrogatan23.as_view(), name='nybrogatan23'),
    path('profile/', views.Profile.as_view(), name='profile'),
    path('edit_reservation/<str:pk>/', views.Profile.as_view(), name='edit_reservation')
]
