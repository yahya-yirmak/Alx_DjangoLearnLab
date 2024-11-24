from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test

# Access Control: Only 'Librarian' users can access
def is_librarian(user):
    return user.role == 'Librarian'

@user_passes_test(is_librarian)
def librarian_view(request):
    return render(request, 'librarian_view.html')
