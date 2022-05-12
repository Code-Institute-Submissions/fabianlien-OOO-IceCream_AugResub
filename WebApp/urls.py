from . import views
from django.urls import path

urlpatterns = [
    path('', views.MainPage.as_view(), name='home'),
    path('nybrogatan23/', views.Nybrogatan23.as_view(), name='nybrogatan23')
]
