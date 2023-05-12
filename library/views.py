from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from library.models import Book, BookInstance
from core.response import CustomResponse

from library.serializers import BookInstanceSerializer, BookSerializer


class BookListView(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = BookSerializer

    def get(self, request):
        books = Book.objects.all()

        serializer = self.serializer_class(instance=books, many=True)
        return CustomResponse.success(
            data=serializer.data,
            message="Books fetched successfully!",
        )


class BookDetailView(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = BookSerializer

    def get(self, request, pk: int):
        book = Book.objects.filter(id=pk).first()
        if not book:
            return CustomResponse.error(
                message=f"Book with ID {pk} doesn't exist!",
            )
        serializer = self.serializer_class(instance=book)
        return CustomResponse.success(
            data=serializer.data, message="Book fetched successfully!"
        )


class BookInstanceListView(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = BookInstanceSerializer

    def get(self, request, pk: int):
        book_instances = BookInstance.objects.filter(book__id=pk).all()
        if not book_instances:
            return CustomResponse.error(
                message=f"Book with ID {pk} doesn't have any instances"
            )
        serializer = self.serializer_class(instance=book_instances, many=True)

        return CustomResponse.success(
            data=serializer.data,
            message=f"Book instances of book with ID {pk} fetched successfully!",
        )
