# Generated by Django 4.2 on 2025-06-04 06:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="FitnessClass",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100)),
                ("date_time", models.DateTimeField()),
                ("instructor", models.CharField(max_length=100)),
                ("total_slots", models.PositiveIntegerField()),
                ("available_slots", models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name="User",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("username", models.CharField(max_length=100)),
                ("email", models.EmailField(max_length=100, unique=True)),
                ("phone", models.CharField(max_length=15)),
                ("password", models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="Booking",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("client_name", models.CharField(max_length=100)),
                ("client_email", models.EmailField(max_length=254)),
                ("booked_at", models.DateTimeField(auto_now_add=True)),
                (
                    "fitness_class",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="bookings",
                        to="user_fitapp.fitnessclass",
                    ),
                ),
            ],
        ),
    ]
