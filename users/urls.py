
from django.urls import path
from .views import AddBook, AddLibrary, CheckIn, RegisterView, ReturnBook
from .views import LoginView

urlpatterns = [
    path('register',RegisterView.as_view()),
    path('login',LoginView.as_view()),
    path('add-library',AddLibrary.as_view()),
    path('library-list',AddLibrary.as_view()),
    path('add-book',AddBook.as_view()),
    path('book-list',AddBook.as_view()),
    path('check-in',CheckIn.as_view()),
     path('check-out',ReturnBook.as_view())
]