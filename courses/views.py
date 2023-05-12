from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from core.response import CustomResponse

from courses.serializers import (
    CourseEnrollmentListSerializer,
    CourseEnrollmentSerializer,
    CourseSessionSerializer,
    CourseSerializer,
)
from courses.models import CourseEnrollment, CourseSession, Course


class CourseListView(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = CourseSerializer

    def get(self, request):
        courses = Course.objects.all()
        serializer = self.serializer_class(instance=courses, many=True)

        return CustomResponse.success(
            data=serializer.data,
            message="Courses fetched successfully!",
        )


class CourseDetailView(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = CourseSerializer

    def get(self, request, pk: int):
        course = Course.objects.filter(id=pk).first()
        if not course:
            return CustomResponse.error(
                message=f"Course with ID {pk} doesn't exist!",
            )
        serializer = self.serializer_class(instance=course)
        return CustomResponse.success(
            data=serializer.data,
            message="Course fetched successfully!",
        )


class CourseSessionListView(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = CourseSessionSerializer

    def get(self, request):
        course_sessions = CourseSession.objects.all()
        serializer = self.serializer_class(instance=course_sessions, many=True)

        return CustomResponse.success(
            data=serializer.data,
            message="Course sessions fetched succesfully!",
        )


class CourseSessionDetailView(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = CourseSessionSerializer

    def get(self, request, pk: int):
        course_session = CourseSession.objects.filter(id=pk).first()
        if not course_session:
            return CustomResponse.error(
                message=f"Course session with ID {pk} doesn't exist"
            )
        serializer = self.serializer_class(instance=course_session)
        return CustomResponse.success(
            data=serializer.data, message="Course session fetched successfully!"
        )


class StudentEnrollmentListView(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = CourseEnrollmentListSerializer

    def get(self, request: Request):
        enrollments = CourseEnrollment.objects.filter(student__user=request.user).all()
        serializer = self.serializer_class(instance=enrollments)

        return CustomResponse.success(
            data=serializer.data, message="Enrollments fetched successfully!"
        )


class StudentEnrollmentDetailView(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = CourseEnrollmentSerializer

    def get(self, request: Request, pk: int):
        enrollment = CourseEnrollment.objects.filter(
            student__user=request.user, id=pk
        ).first()
        if not enrollment:
            return CustomResponse.error(
                message=f"Enrollment with ID {pk} doesn't exist!", status_code=404
            )
        serializer = self.serializer_class(instance=enrollment)

        return CustomResponse.success(
            data=serializer.data, message="Enrollment fetched successfully!"
        )
