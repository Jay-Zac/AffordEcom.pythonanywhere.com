from django.urls import path
from . import views

app_name = 'item'
urlpatterns = [
    path('', views.item_view, name='items'),
    path('new/', views.new_view, name='new'),
    path('<int:pk>/', views.detail_view, name='detail'),
    path('<int:pk>/delete/', views.delete_view, name='delete'),
    path('<int:pk>/edit/', views.edit_view, name='edit'),
]
