This is the LibraryProject Django application :

# Permissions and Groups Setup

## Custom Permissions

The `Document` model includes the following permissions:
- `can_view`: View document details.
- `can_create`: Create a new document.
- `can_edit`: Edit existing documents.
- `can_delete`: Delete documents.

## Groups

- `Viewers`: Assigned `can_view`.
- `Editors`: Assigned `can_create`, `can_edit`.
- `Admins`: Assigned all permissions.

## Enforcing Permissions

- Permissions are enforced in views using the `@permission_required` decorator.
- Unauthorized users will receive a `PermissionDenied` error if they attempt restricted actions.

## Testing

1. Create test users and assign them to the respective groups.
2. Test actions as different users to verify access control.


