# application/user_service.py
from domain.user import User
from application.user_repository import AbstractUserRepository
from typing import List, Optional

class UserService:
    """
    Application Service (Use Case) for User CRUD operations.
    It orchestrates the flow using the Domain Model and Repository interface.
    """
    def __init__(self, user_repo: AbstractUserRepository):
        # Dependency Injection: The Use Case depends on the Abstract Repository
        self._user_repo = user_repo

    def create_user(self, name: str, email: str) -> Optional[str]:
        """Creates a new User entity and persists it."""
        try:
            # 1. Use the Domain Entity to enforce core rules (e.g., validation)
            new_user = User(name, email) 
        except ValueError as e:
            # Handle domain rule violation
            print(f"Error creating user: {e}")
            return None

        # 2. Use the Repository to persist the entity
        self._user_repo.create(new_user)
        print(f"Created user '{name}' with ID: {new_user.id}")
        return new_user.id

    def get_user(self, user_id: str) -> Optional[User]:
        """Retrieves a specific User entity."""
        user = self._user_repo.get_by_id(user_id)
        if not user:
            print(f"Error: User with ID {user_id} not found.")
        return user
        
    def get_all_users(self) -> List[User]:
        """Retrieves all User entities."""
        return self._user_repo.get_all()

    def update_user(self, user_id: str, name: str = None, email: str = None) -> bool:
        """Updates an existing User's details."""
        user = self._user_repo.get_by_id(user_id)
        if not user:
            print(f"Error: User with ID {user_id} not found. Update failed.")
            return False

        if not name and not email:
            print(f"Warning: No valid data provided to update user ID {user_id}.")
            return False

        # 1. Update the Domain Entity
        user.update_details(name, email)
        
        # 2. Persist the changes via the Repository
        self._user_repo.update(user)
        print(f"Updated user ID {user_id}.")
        return True

    def delete_user(self, user_id: str) -> bool:
        """Deletes a User by ID."""
        deleted = self._user_repo.delete(user_id)
        if deleted:
            print(f"Deleted user with ID {user_id}.")
        else:
            print(f"Error: User with ID {user_id} not found. Deletion failed.")
        return deleted