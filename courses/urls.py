from django.urls import path

from .views import (
    CourseDetailView,
    CourseSessionListView,
    StudentEnrollmentListView,
    StudentEnrollmentDetailView,
    CourseSessionDetailView,
    CourseListView,
)


urlpatterns = [
    path("courses/", CourseListView.as_view(), name="courses"),
    path("course/<pk>/", CourseDetailView.as_view(), name="course"),
    path("sessions/", CourseSessionListView.as_view(), name="sessions"),
    path("session/<pk>/", CourseSessionDetailView.as_view(), name="session"),
    path("enrollments/", StudentEnrollmentListView.as_view(), name="enrollments"),
    path("enrollment/<pk>/", StudentEnrollmentDetailView.as_view(), name="enrollment"),
]
