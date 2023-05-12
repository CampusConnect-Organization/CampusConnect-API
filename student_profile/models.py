from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()

GENDER_CHOICES = (
    ("male", "Male"),
    ("female", "Female"),
    ("other", "Other"),
)


class StudentProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)
    gender = models.CharField(choices=GENDER_CHOICES, max_length=20)
    date_of_birth = models.DateField()
    address = models.CharField(max_length=100)
    academics = models.TextField()
    is_verified = models.BooleanField(default=False)
    symbol_number = models.CharField(null=True, max_length=50, blank=True)

    def __str__(self) -> str:
        return f"{self.full_name}'s Profile"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.user.type = "student"
        self.user.save()

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self) -> str:
        return self.full_name
