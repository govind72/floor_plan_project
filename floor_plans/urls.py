# urls.py
from django.urls import path
from .views import RegisterView, LoginView,BookingCreateView,BookingListView,MeetingRoomListView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('bookings/', BookingListView.as_view(), name='booking-list'),
    path('bookings/create/', BookingCreateView.as_view(), name='booking-create'),
    path('meeting-rooms/', MeetingRoomListView.as_view(), name='meeting-room-list'),

]
