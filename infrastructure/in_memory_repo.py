# infrastructure/in_memory_repo.py
from application.user_repository import AbstractUserRepository
from domain.user import User
from typing import List, Dict, Optional

class InMemoryUserRepository(AbstractUserRepository):
    """
    Concrete implementation of the UserRepository using an in-memory dictionary.
    This is an Adapter for the Use Case layer.
    """
    def __init__(self):
        # This acts as the "database"
        self._users: Dict[str, User] = {}

    def create(self, user: User) -> None:
        """Stores a new User entity."""
        self._users[user.id] = user

    def get_by_id(self, user_id: str) -> Optional[User]:
        """Retrieves a User entity by ID."""
        # Returns the actual User object (Domain Entity)
        return self._users.get(user_id)

    def get_all(self) -> List[User]:
        """Retrieves all User entities."""
        return list(self._users.values())

    def update(self, user: User) -> None:
        """Saves changes to an existing User entity."""
        if user.id in self._users:
            self._users[user.id] = user
        # Note: If the ID wasn't found here, it would be an infrastructure error

    def delete(self, user_id: str) -> bool:
        """Deletes a User by ID."""
        if user_id in self._users:
            del self._users[user_id]
            return True
        return False