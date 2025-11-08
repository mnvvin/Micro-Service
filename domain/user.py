# domain/user.py
import uuid

class User:
    """Represents the core User entity/Domain Model."""
    def __init__(self, name: str, email: str, user_id: str = None):
        if not name or not email:
            # Domain rule: User must have a name and email
            raise ValueError("Name and email are required for a User.")
            
        self.id = user_id if user_id is not None else str(uuid.uuid4())
        self.name = name
        self.email = email

    def update_details(self, name: str = None, email: str = None):
        """Domain logic for updating user details."""
        if name:
            self.name = name
        if email:
            self.email = email

    def __repr__(self):
        return f"User(id='{self.id}', name='{self.name}', email='{self.email}')"