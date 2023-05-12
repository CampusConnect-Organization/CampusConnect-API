from django.contrib import admin
from .models import StudentProfile
from django.contrib import messages
from courses.models import InstructorProfile


class StudentProfileAdmin(admin.ModelAdmin):
    list_display = (
        "full_name",
        "phone",
        "gender",
        "date_of_birth",
        "address",
        "academics",
        "is_verified",
    )
    list_filter = ("is_verified",)
    search_fields = (
        "user__username",
        "user__email",
        "first_name",
        "last_name",
        "phone",
        "address",
        "academics",
    )

    def save_model(self, request, obj, form, change):
        if InstructorProfile.objects.filter(user=obj.user).exists():
            messages.error(
                request, "An instructor profile already exists for this user."
            )
            return
        super().save_model(request, obj, form, change)


admin.site.register(StudentProfile, StudentProfileAdmin)
