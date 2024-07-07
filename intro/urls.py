from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('generate_qr/', views.generate_qr, name='generate_qr'),
    path('qr_display/', views.qr_display, name='qr_display'),
]
