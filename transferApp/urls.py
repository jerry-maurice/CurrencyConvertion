from django.urls import path
from . import views

urlpatterns = [
    # ex: /transfer/dashboard
    path('dashboard/', views.dashboard, name='dashboard'),
    # ex: /transfer/transfer
    path('transfer/', views.transfer, name='transfer'),
    # ex: /transfer/profile
    path('profile/', views.profile, name='profile'),
    ]
