from django.urls import path
from . import views

app_name = 'seller'
urlpatterns = [
    path('', views.login_seller_view, name='seller_login'),
    path('seller_logout/', views.logout_seller_view, name='seller_logout'),
    path('seller_register/', views.register_seller_view, name='seller_register'),
]
