from django.db import models


# Create your models here.
class Attendance(models.Model):
    course_session = models.ForeignKey(
        "courses.CourseSession", on_delete=models.CASCADE
    )
    student = models.ForeignKey(
        "student_profile.StudentProfile", on_delete=models.CASCADE
    )
    attendance_count = models.IntegerField(default=0)
    last_updated = models.DateField(auto_now=True)
