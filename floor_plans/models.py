# floor_plans/models.py
from django.db import models
from django.contrib.auth.models import AbstractUser
from simple_history.models import HistoricalRecords
from django.utils import timezone

class CustomUser(AbstractUser):
    USER_TYPE_CHOICES = (
        ('admin_level_1', 'Admin Level 1'),
        ('admin_level_2', 'Admin Level 2'),
        ('employee', 'Employee'),
    )
    user_type = models.CharField(max_length=20, choices=USER_TYPE_CHOICES, default='employee')

class LogEntry(models.Model):
    ACTION_CHOICES = (
        ('added', 'Added'),
        ('edited', 'Edited'),
        ('deleted', 'Deleted'),
    )

    user = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True, blank=True, related_name='log_entries')
    timestamp = models.DateTimeField(default=timezone.now)
    action = models.CharField(max_length=20, choices=ACTION_CHOICES)
    model_name = models.CharField(max_length=255)
    object_id = models.PositiveIntegerField()
    object_str = models.CharField(max_length=255)
    changes = models.TextField()

    def __str__(self):
        return f"{self.user} - {self.timestamp} - {self.action} - {self.model_name} {self.object_id}"

    def get_details(self):
        return f"{self.action.capitalize()} {self.model_name} {self.object_id}:\n{self.changes}"

class Floor(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    max_desks = models.PositiveIntegerField(default=0)
    max_rooms = models.PositiveIntegerField(default=0)
    admin_user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True, blank=True)
    timestamp = models.DateTimeField(null=True, blank=True)
    history = HistoricalRecords()

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        # Check if there's a conflict with the latest version
        latest_version = Floor.objects.filter(pk=self.pk).latest('timestamp')

        if latest_version.timestamp and self.timestamp and latest_version.timestamp > self.timestamp:
            # Resolve conflict based on admin hierarchy
            if (
                self.admin_user
                and latest_version.admin_user
                and self.admin_user.user_type == 'admin_level_1'
                and latest_version.admin_user.user_type == 'admin_level_2'
            ):
                # Keep the latest version
                super().save(*args, **kwargs)
            elif (
                self.admin_user
                and latest_version.admin_user
                and self.admin_user.user_type == 'admin_level_2'
                and latest_version.admin_user.user_type == 'admin_level_1'
            ):
                # Keep the current version
                return
            else:
                # Handle conflict resolution based on your specific logic
                # This is a simplified example; adjust as per your needs
                pass
        else:
            super().save(*args, **kwargs)

class Meeting_Room(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    capacity = models.PositiveIntegerField(default=0)
    floor = models.ForeignKey(Floor, on_delete=models.CASCADE)
    projector_available = models.BooleanField(default=False)
    video_conferencing = models.BooleanField(default=False)
    whiteboard_available = models.BooleanField(default=False)
    telepresence_facilities = models.BooleanField(default=False)
    # Add more properties as needed

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        # Check if adding a meeting room exceeds the maximum limit for the floor
        current_meeting_rooms = self.floor.meeting_room_set.count()
        if current_meeting_rooms >= self.floor.max_rooms:
            raise ValueError("Exceeded the maximum limit of meeting rooms for this floor.")
        
        super().save(*args, **kwargs)

class Desk(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    floor = models.ForeignKey(Floor, on_delete=models.CASCADE)
    is_standing = models.BooleanField(default=False)
    has_microphone = models.BooleanField(default=False)
    has_outlet = models.BooleanField(default=True)
    has_ethernet_port = models.BooleanField(default=True)
    ergonomic_chair = models.BooleanField(default=False)
    dual_monitor_support = models.BooleanField(default=False)
    # Add more properties as needed

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        # Check if adding a desk exceeds the maximum limit for the floor
        current_desks = self.floor.desk_set.count()
        if current_desks >= self.floor.max_desks:
            raise ValueError("Exceeded the maximum limit of desks for this floor.")
        
        super().save(*args, **kwargs)


class Booking(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    room = models.ForeignKey(Meeting_Room, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    def __str__(self):
        return f"{self.user.username} - {self.room.name} - {self.start_time} to {self.end_time}"
