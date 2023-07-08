from rest_framework import serializers

from attendance.models import Attendance


class AttendanceViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendance
        fields = ["course_session", "student_profile", "attendance_count"]
