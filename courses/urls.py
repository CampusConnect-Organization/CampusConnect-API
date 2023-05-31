from django.urls import path

from .views import (
    CourseDetailView,
    CourseEnrollmentDetailView,
    CourseEnrollmentListView,
    CourseSessionListView,
    StudentCoursesListView,
    StudentCourseDetailView,
    CourseSessionDetailView,
    CourseListView,
    CourseSemesterView,
)


urlpatterns = [
    path("courses/", CourseListView.as_view(), name="courses"),
    path("course/<pk>/", CourseDetailView.as_view(), name="course"),
    path("semester/<semester>/", CourseSemesterView.as_view(), name="course-semester"),
    path("sessions/", CourseSessionListView.as_view(), name="sessions"),
    path("session/<pk>/", CourseSessionDetailView.as_view(), name="session"),
    path("student-courses/", StudentCoursesListView.as_view(), name="student-courses"),
    path(
        "student-course/<pk>/", StudentCourseDetailView.as_view(), name="student-course"
    ),
    path("enrollments/", CourseEnrollmentListView.as_view(), name="enrollments"),
    path("enrollment/<pk>/", CourseEnrollmentDetailView.as_view(), name="enrollment"),
]
