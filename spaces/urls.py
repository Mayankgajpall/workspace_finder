from django.urls import path
from . import views

urlpatterns = [
    path('', views.search_res, name='search_result'),
    path('<int:pk>/', views.detail, name='detail'),
    path('<int:pk>/book/',views.book, name='book'),
    path('<int:pk>/delete/',views.delete_booking, name='delete'),
    path('booked/',views.booked, name='booked'),
    path('your_bookings/',views.your_bookings,name="your_bookings")
]