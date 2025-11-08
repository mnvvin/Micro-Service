import uuid

USERS = {}

def create_user(name, email):
    """Creates a new user and adds them to the USERS dictionary."""
    if not name or not email:
        print("Error: Name and email are required.")
        return None

    # Generate a unique ID for the new user
    user_id = str(uuid.uuid4())
    user_data = {
        "name": name,
        "email": email
    }
    USERS[user_id] = user_data
    print(f"Created user '{name}' with ID: {user_id}")
    return user_id

def get_user(user_id=None):
    
    if user_id:
        user = USERS.get(user_id)
        if user:
            # Combine ID with user data for a complete view
            return {"id": user_id, **user}
        else:
            print(f"Error: User with ID {user_id} not found.")
            return None
    else:
        # Get all users and include their IDs
        all_users = [{"id": uid, **data} for uid, data in USERS.items()]
        return all_users

def update_user(user_id, name=None, email=None):
    """Updates the name or email of an existing user."""
    if user_id not in USERS:
        print(f"Error: User with ID {user_id} not found. Update failed.")
        return False

    user_data = USERS[user_id]
    updated = False

    if name:
        user_data['name'] = name
        updated = True
    if email:
        user_data['email'] = email
        updated = True

    if updated:
        print(f"Updated user ID {user_id}.")
        return True
    else:
        print(f"Warning: No valid data provided to update user ID {user_id}.")
        return False

def delete_user(user_id):
    """Deletes a user by ID."""
    if user_id in USERS:
        del USERS[user_id]
        print(f"Deleted user with ID {user_id}.")
        return True
    else:
        print(f"Error: User with ID {user_id} not found. Deletion failed.")
        return False

if __name__ == "__main__":
        
    print("\n1. CREATE two users:")
    # CREATE Operation
    manav_id = create_user("Manav Vinayak", "manivin123@gmail.com")
    rohan_id = create_user("Rohan Sir", "rohan123@gmail.com")

    print("\n2. READ all users:")
    # READ All Operation
    print(get_user())

    print("\n3. UPDATE Manav's email:")
    # UPDATE Operation
    update_user(manav_id, email="manavvinayak41@gmail.com")

    print("\n4. READ Manav specifically:")
    # READ Specific Operation
    print(get_user(manav_id))

    print("\n5. DELETE Rohan:")
    # DELETE Operation
    delete_user(rohan_id)

    print("\n6. READ all users after deletion (only Manav remains):")
    # Final READ All Operation
    print(get_user())
    