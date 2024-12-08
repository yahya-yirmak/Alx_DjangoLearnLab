## Blog Post Management Features

This project implements full CRUD capabilities for blog posts:
- **ListView**: Displays all posts at `/`.
- **DetailView**: Displays individual post details at `/post/<id>/`.
- **CreateView**: Allows authenticated users to create posts at `/post/new/`.
- **UpdateView**: Allows authors to edit their posts at `/post/<id>/edit/`.
- **DeleteView**: Allows authors to delete their posts at `/post/<id>/delete/`.

### Permissions
- Only authenticated users can create posts.
- Only the author of a post can edit or delete it.

### Testing
- Ensure all forms validate inputs.
- Verify permissions work as intended.
