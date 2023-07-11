from django.urls import path

from .views import InstructorProfileView, StudentListView

urlpatterns = [
    path("", InstructorProfileView.as_view(), name="instructor-profile"),
    path("students/", StudentListView.as_view(), name="students"),
]
