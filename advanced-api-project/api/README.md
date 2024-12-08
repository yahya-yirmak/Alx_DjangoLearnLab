## API Endpoints for Book Model

- `GET /books/` - Retrieve a list of books (Public)
- `GET /books/<int:pk>/` - Retrieve a single book by ID (Public)
- `POST /books/create/` - Create a new book (Authenticated users only)
- `PUT /books/<int:pk>/update/` - Update an existing book (Authenticated users only)
- `DELETE /books/<int:pk>/delete/` - Delete a book (Authenticated users only)

### Authentication
- Endpoints marked as "Authenticated users only" require a valid token.


## API Query Features
### Filtering
- Filter by title (case-insensitive): `?title__icontains=<value>`
- Filter by author: `?author=<value>`
- Filter by publication year:
  - Exact: `?publication_year=<value>`
  - Greater than or equal to: `?publication_year__gte=<value>`
  - Less than or equal to: `?publication_year__lte=<value>`

### Searching
- Search by title or author: `?search=<value>`

### Ordering
- Order by title: `?ordering=title`
- Order by publication year (descending): `?ordering=-publication_year`
