# Generated by Django 3.1.4 on 2023-12-07 00:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('floor_plans', '0009_auto_20231207_0541'),
    ]

    operations = [
        migrations.AddField(
            model_name='desk',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='desk',
            name='dual_monitor_support',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='desk',
            name='ergonomic_chair',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='desk',
            name='has_ethernet_port',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='desk',
            name='has_microphone',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='desk',
            name='has_outlet',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='desk',
            name='is_standing',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='floor',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='floor',
            name='no_of_desks',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='floor',
            name='no_of_meeting_rooms',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='historicalfloor',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='historicalfloor',
            name='no_of_desks',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='historicalfloor',
            name='no_of_meeting_rooms',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='meeting_room',
            name='capacity',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='meeting_room',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='meeting_room',
            name='projector_available',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='meeting_room',
            name='telepresence_facilities',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='meeting_room',
            name='video_conferencing',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='meeting_room',
            name='whiteboard_available',
            field=models.BooleanField(default=False),
        ),
    ]
