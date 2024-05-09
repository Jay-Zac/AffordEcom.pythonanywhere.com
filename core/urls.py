from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .forms import LogInForm

urlpatterns = [
    path('', views.index_view, name='index'),
    path('contact/', views.contact_view, name='contact'),
    path('signup/', views.signup_view, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='core_html/login.html', authentication_form=LogInForm),
         name='login'),
    path('logout/', views.logout_user_view, name='logout'),
    path('item/<int:pk>', views.detail_view, name='detail'),
    path('about/', views.about_view, name='about'),
]
