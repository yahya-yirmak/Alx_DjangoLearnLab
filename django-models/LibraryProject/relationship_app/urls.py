from django.urls import path
from .views import list_books
from .views import LibraryDetailView
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView
from .views import SignUpView

urlpatterns = [
    path('books/', list_books, name='list_books'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
    path('login/', LoginView.as_view(template='login.html'), name='login'),
    path('logout/', LogoutView.as_view(template='logout.html'), name='logout'),
    path('register/', SignUpView.as_view(), name='register')
]
