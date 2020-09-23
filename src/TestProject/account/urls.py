from django.urls import path
from django.contrib.auth import views as auth_views
from .views import register, home

app_name = "account"
urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='account/login.html'), name="user-login" ),
    path('logout/', auth_views.LogoutView.as_view(template_name='account/logout.html'), name="user-logout"),
    path('register/', register, name='user-register'),
    path('', home, name='user-home'),
]