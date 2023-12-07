# Generated by Django 3.1.4 on 2023-12-06 23:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('floor_plans', '0006_auto_20231207_0417'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChangeHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('change_type', models.CharField(choices=[('Add', 'Add'), ('Update', 'Update'), ('Delete', 'Delete')], max_length=20)),
                ('desk', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='floor_plans.desk')),
                ('floor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='floor_plans.floor')),
                ('meeting_room', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='floor_plans.meeting_room')),
            ],
        ),
    ]