from django.db import models
from student_profile.models import StudentProfile
from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model

User = get_user_model()

SEMESTER_CHOICES = (
    ("1st", "1st"),
    ("2nd", "2nd"),
    ("3rd", "3rd"),
    ("4th", "4th"),
    ("5th", "5th"),
    ("6th", "6th"),
    ("7th", "7th"),
    ("8th", "8th"),
)


# Create your models here.
class Course(models.Model):
    title = models.CharField(max_length=100)
    course_code = models.CharField(max_length=100)
    description = models.TextField()
    semester = models.CharField(max_length=20, choices=SEMESTER_CHOICES)

    def __str__(self):
        return self.title


class InstructorProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.user.type = "instructor"
        self.user.save()

    def __str__(self):
        return self.full_name


class CourseSession(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    start = models.DateField()
    end = models.DateField()
    instructor = models.ForeignKey(
        InstructorProfile, on_delete=models.SET_NULL, null=True
    )

    def __str__(self):
        return f"{self.course.title}({self.start}-{self.end})"


class CourseEnrollment(models.Model):
    student = models.ForeignKey(StudentProfile, on_delete=models.CASCADE)
    course_session = models.ForeignKey(CourseSession, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.student.full_name} - {self.course_session.course.title}"

    class Meta:
        unique_together = ("student", "course_session")
