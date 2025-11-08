# application/user_repository.py
from abc import ABC, abstractmethod
from domain.user import User
from typing import List, Optional

class AbstractUserRepository(ABC):
    """
    Interface (Port) for accessing user persistence.
    The Use Case layer depends on this abstraction.
    """
    @abstractmethod
    def create(self, user: User) -> None:
        pass

    @abstractmethod
    def get_by_id(self, user_id: str) -> Optional[User]:
        pass

    @abstractmethod
    def get_all(self) -> List[User]:
        pass

    @abstractmethod
    def update(self, user: User) -> None:
        pass

    @abstractmethod
    def delete(self, user_id: str) -> bool:
        pass