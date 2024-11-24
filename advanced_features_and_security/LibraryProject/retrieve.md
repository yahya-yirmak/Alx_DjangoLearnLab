
### Retrieving a Book Instance

**Command**:
```python
book = Book.objects.get(id=book.id)
book.title, book.author, book.publication_year
