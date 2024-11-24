from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import permission_required
from django.http import HttpResponse
from .models import Document
from .models import Book
from .forms import SearchForm

# Create your views here.


def book_list(request):
    books = Book.objects.all()  # Retrieve all books
    return render(request, 'bookshelf/book_list.html', {'books': books})


@permission_required('app_name.can_view', raise_exception=True)
def view_document(request, doc_id):
    document = get_object_or_404(Document, id=doc_id)
    return render(request, 'document_detail.html', {'document': document})

@permission_required('app_name.can_create', raise_exception=True)
def create_document(request):
    if request.method == "POST":
        # Save document logic here
        return HttpResponse("Document created.")
    return render(request, 'create_document.html')

@permission_required('app_name.can_edit', raise_exception=True)
def edit_document(request, doc_id):
    document = get_object_or_404(Document, id=doc_id)
    if request.method == "POST":
        # Update document logic here
        return HttpResponse("Document updated.")
    return render(request, 'edit_document.html', {'document': document})

@permission_required('app_name.can_delete', raise_exception=True)
def delete_document(request, doc_id):
    document = get_object_or_404(Document, id=doc_id)
    document.delete()
    return HttpResponse("Document deleted.")

def search_books(request):
    form = SearchForm(request.GET or None)
    books = []
    if form.is_valid():
        search_query = form.cleaned_data['query']
        books = Book.objects.filter(title__icontains=search_query)
    return render(request, 'bookshelf/book_list.html', {'books': books, 'form': form})

def example_view(request):
    response = HttpResponse("Example content")
    response['Content-Security-Policy'] = "default-src 'self';"
    return response


