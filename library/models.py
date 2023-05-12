from django.db import models

from courses.models import Course
from student_profile.models import StudentProfile


# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    course = models.ForeignKey(
        Course,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.title


class BookInstance(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    book_number = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return f"{self.book.title}({self.book_number})"


class BorrowRecord(models.Model):
    book_instance = models.ForeignKey(BookInstance, on_delete=models.CASCADE)
    student = models.ForeignKey(StudentProfile, on_delete=models.CASCADE)
    borrow_date = models.DateField(auto_now_add=True)
    return_date = models.DateField(blank=True, null=True)

    class Meta:
        unique_together = ("book_instance", "student")

    def __str__(self):
        return f"{self.book_instance.book.title} - {self.student.full_name}"


class ReturnRecord(models.Model):
    borrow_record = models.OneToOneField(BorrowRecord, on_delete=models.CASCADE)
    return_date = models.DateField(auto_now_add=True)

    def save(self, *args, **kwargs):
        self.borrow_record.return_date = self.return_date
        self.borrow_record.save()

        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.borrow_record.book_instance.book.title} - {self.borrow_record.student.full_name}"
