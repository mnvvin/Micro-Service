# main.py
from infrastructure.in_memory_repo import InMemoryUserRepository
from application.user_service import UserService

def run_application():
    """Wires up the dependencies and executes the user flow."""
    
    # 1. Infrastructure/Adapter instantiation
    # This is the concrete database implementation
    user_repo = InMemoryUserRepository()
    
    # 2. Use Case/Application Service instantiation
    # The UserService is given the concrete repository implementation (Dependency Injection)
    user_service = UserService(user_repo)

    print("\n1. CREATE two users:")
    # CREATE Operation
    manav_id = user_service.create_user("Manav Vinayak", "manivin123@gmail.com")
    rohan_id = user_service.create_user("Rohan Sir", "rohan123@gmail.com")

    print("\n2. READ all users:")
    # READ All Operation - The Use Case returns User entities
    print(user_service.get_all_users())

    print("\n3. UPDATE Manav's email:")
    # UPDATE Operation
    user_service.update_user(manav_id, email="manavvinayak41@gmail.com")

    print("\n4. READ Manav specifically:")
    # READ Specific Operation
    print(user_service.get_user(manav_id))

    print("\n5. DELETE Rohan:")
    # DELETE Operation
    user_service.delete_user(rohan_id)

    print("\n6. READ all users after deletion (only Manav remains):")
    # Final READ All Operation
    print(user_service.get_all_users())
    
if __name__ == "__main__":
    run_application()