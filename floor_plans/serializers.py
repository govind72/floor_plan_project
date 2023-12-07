from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Booking
from .models import Meeting_Room

class MeetingRoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meeting_Room
        fields = '__all__'

class MeetingRoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meeting_Room
        fields = ['id', 'name', 'description', 'capacity', 'floor', 'projector_available', 'video_conferencing', 'whiteboard_available', 'telepresence_facilities']


CustomUser = get_user_model()
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'username', 'email')

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password')  # Add other fields as needed
        extra_kwargs = {'password': {'write_only': True}}


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = CustomUser.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ['id', 'user', 'room', 'start_time', 'end_time']
