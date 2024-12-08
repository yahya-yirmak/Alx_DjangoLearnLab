## API Endpoints for Book Model

- `GET /books/` - Retrieve a list of books (Public)
- `GET /books/<int:pk>/` - Retrieve a single book by ID (Public)
- `POST /books/create/` - Create a new book (Authenticated users only)
- `PUT /books/<int:pk>/update/` - Update an existing book (Authenticated users only)
- `DELETE /books/<int:pk>/delete/` - Delete a book (Authenticated users only)

### Authentication
- Endpoints marked as "Authenticated users only" require a valid token.
