# floor_plans/admin.py
from django.contrib import admin
from .models import CustomUser, Floor, Meeting_Room, Desk, LogEntry,Booking

class MeetingRoomInline(admin.TabularInline):
    model = Meeting_Room
    extra = 1  # Number of empty forms to display for adding new meeting rooms

class DeskInline(admin.TabularInline):
    model = Desk
    extra = 1  # Number of empty forms to display for adding new desks

@admin.register(LogEntry)
class LogEntryAdmin(admin.ModelAdmin):
    list_display = ('user', 'timestamp', 'action', 'model_name', 'object_id')

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'user_type')

@admin.register(Floor)
class FloorAdmin(admin.ModelAdmin):
    list_display = ('name',)
    inlines = [MeetingRoomInline, DeskInline]
    search_fields = ['name']

@admin.register(Meeting_Room)
class MeetingRoomAdmin(admin.ModelAdmin):
    list_display = ('name', 'floor')
    search_fields = ['name', 'floor__name']

@admin.register(Desk)
class DeskAdmin(admin.ModelAdmin):
    list_display = ('name', 'floor')
    search_fields = ['name', 'floor__name']

class BookingAdmin(admin.ModelAdmin):
    list_display = ('get_user_username', 'get_room_name', 'start_time', 'end_time')

    def get_user_username(self, obj):
        return obj.user.username

    def get_room_name(self, obj):
        return obj.room.name

    # Add more methods as needed

    # ...

# Register the model with the updated admin class
admin.site.register(Booking, BookingAdmin)