from django.urls import path

from library.views import BookDetailView, BookInstanceListView, BookListView


urlpatterns = [
    path("books/", BookListView.as_view(), name="books"),
    path("book/<pk>/", BookDetailView.as_view(), name="book"),
    path("book-instances/<pk>/", BookInstanceListView.as_view(), name="book-instances"),
]
