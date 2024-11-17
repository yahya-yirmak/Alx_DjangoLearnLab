from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test

# Access Control: Only 'Member' users can access
def is_member(user):
    return user.role == 'Member'

@user_passes_test(is_member)
def member_view(request):
    return render(request, 'member_view.html')
