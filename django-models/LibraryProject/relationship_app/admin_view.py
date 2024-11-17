from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test

# Access Control: Only 'Admin' users can access
def is_admin(user):
    return user.role == 'Admin'

@user_passes_test(is_admin)
def admin_view(request):
    return render(request, 'admin_view.html')


