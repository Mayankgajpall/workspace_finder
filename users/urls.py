from django.urls import path
from . import views

urlpatterns = [
    path('', views.log_reg, name='login_register_page'),
    path('login/', views.auth_login, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.user_logout, name='logout'),
]