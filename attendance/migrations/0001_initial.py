# Generated by Django 4.2.1 on 2023-07-11 17:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("student_profile", "0001_initial"),
        ("courses", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Attendance",
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
                (
                    "status",
                    models.CharField(
                        choices=[("absent", "Absent"), ("present", "Present")],
                        max_length=20,
                    ),
                ),
                ("date", models.DateTimeField(auto_now_add=True)),
                (
                    "course_session",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="courses.coursesession",
                    ),
                ),
                (
                    "student",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="student_profile.studentprofile",
                    ),
                ),
            ],
        ),
    ]
