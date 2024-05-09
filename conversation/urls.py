from django.urls import path
from. import views

app_name = 'conversation'
urlpatterns = [
    path('', views.inbox_view, name='inbox'),
    path('<int:pk>/', views.detail_view, name='detail'),
    path('new/<int:item_pk>/', views.new_conversation_view, name='new'),
]