from django.urls import path
from . import views

urlpatterns = [
    path('', views.cart_summary_view, name='cart_summary'),
]
