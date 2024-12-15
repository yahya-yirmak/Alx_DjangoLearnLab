from django.contrib.auth.views import LoginView
from django.urls import path
from . import views


urlpatterns = [
    path('register/', views.SignUpView.as_view(), name='register'),
    path('login/', LoginView.as_view(template_name='login.html'), name='login')
]