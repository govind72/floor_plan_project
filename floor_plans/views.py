from django.contrib.auth import get_user_model, authenticate
from rest_framework import generics, permissions, response, status
from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import RegisterSerializer, LoginSerializer, UserSerializer ,BookingSerializer
from .models import Booking
from .models import Meeting_Room
from .serializers import MeetingRoomSerializer

CustomUser = get_user_model()


class MeetingRoomListView(generics.ListAPIView):
    queryset = Meeting_Room.objects.all()
    serializer_class = MeetingRoomSerializer
    permission_classes = [permissions.IsAuthenticated]

    
class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny]

class LoginView(generics.GenericAPIView):
    serializer_class = LoginSerializer
    permission_classes = [permissions.AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        # Use your custom user model for authentication
        user = authenticate(
            username=serializer.validated_data['username'],
            password=serializer.validated_data['password']
        )
        
        if not user:
            return response.Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

        refresh = RefreshToken.for_user(user)
        return response.Response({
            'refresh': str(refresh),
            'access': str(refresh.access_token),
            'user': UserSerializer(user, context=self.get_serializer_context()).data
        })



class BookingCreateView(generics.CreateAPIView):
    serializer_class = BookingSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class BookingListView(generics.ListAPIView):
    serializer_class = BookingSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        return Booking.objects.filter(user=self.request.user)


class BookingCreateView(generics.CreateAPIView):
    serializer_class = BookingSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        room = serializer.validated_data['room']
        start_time = serializer.validated_data['start_time']
        end_time = serializer.validated_data['end_time']

        # Check if the room is available for the specified time slot
        if Booking.objects.filter(room=room, start_time__lt=end_time, end_time__gt=start_time).exists():
            raise serializers.ValidationError("The room is not available during the specified time slot.")

        serializer.save(user=self.request.user)
