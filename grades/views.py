from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from core.response import CustomResponse
from courses.models import CourseEnrollment
from grades.models import Exam, GradeRecord

from grades.serializers import GradeRecordSerializer, ExamSerializer


class ExamListView(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ExamSerializer

    def get(self, request):
        course_enrollments = CourseEnrollment.objects.filter(
            student=request.user.studentprofile
        )

        exams = Exam.objects.filter(
            course_session__in=course_enrollments.values("course_session")
        )

        serializer = self.serializer_class(instance=exams, many=True)

        return CustomResponse.success(
            data=serializer.data, message="Exams fetched successfully!"
        )


class GradeListView(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = GradeRecordSerializer

    def get(self, request):
        grades = GradeRecord.objects.filter(student__user=request.user).all()
        serializer = self.serializer_class(instance=grades, many=True)
        return CustomResponse.success(
            data=serializer.data, message="Grades fetched successfully!"
        )


class GradeDetailView(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = GradeRecordSerializer

    def get(self, request, pk: int):
        grade = GradeRecord.objects.filter(student__user=request.user, id=pk).first()
        if not grade:
            return CustomResponse.error(
                message=f"Grade record with ID {pk} doesn't exist!", status_code=404
            )
        serializer = self.serializer_class(instance=grade)

        return CustomResponse.success(
            data=serializer.data,
            message="Grade record fetched successfully!",
        )
