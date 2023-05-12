from rest_framework import serializers

from courses.models import Course, CourseEnrollment, CourseSession


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = "__all__"


class CourseSessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseSession
        fields = "__all__"


class CourseEnrollmentSerializer(serializers.ModelSerializer):
    instructor_name = serializers.CharField(
        source="course_session.instructor.full_name"
    )

    course_session_name = serializers.CharField(source="course_session.course.title")
    course_session_id = serializers.IntegerField(source="course_session.id")
    start_date = serializers.DateField(source="course_session.start")
    end_date = serializers.DateField(source="course_session.end")
    semester = serializers.CharField(source="course_session.course.semester")

    class Meta:
        model = CourseEnrollment
        fields = [
            "id",
            "instructor_name",
            "course_session_name",
            "course_session_id",
            "start_date",
            "end_date",
            "semester",
        ]


class CourseEnrollmentListSerializer(serializers.ListSerializer):
    child = CourseEnrollmentSerializer()
