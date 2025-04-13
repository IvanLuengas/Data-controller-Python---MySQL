from database import engine, base, session, sessionActive, user

def view_user():
    print("Listening all users...")
    try:
        users = sessionActive.query(user).all()
        if users:
            for u in users:
                print(f"ID: {u.id}, Name: {u.name}, Age: {u.age}")
        else:
            print("No users found in th database.")
    except Exception as e:
        print("Error retrieving users:", e)

def add_user():
    name = input("Enter the new usr's name: ")
    age = int(input("Enter the new user's age: "))
    new_user = user(name=name, age=age)
    sessionActive.add(new_user)
    try:
        sessionActive.commit()
        print("Adding a new user...")
    except Exception as e:
        sessionActive.rollback()
        print("❌ Error adding user:", e)

def delete_user():
    print("Dalating a user...")
    user_id_to_delete = int(input("Enter the ID of the user to delete: "))
    try:
        user_to_delete = sessionActive.query(user).filter(user.id == user_id_to_delete).first()
        if user_to_delete:
            sessionActive.delete(user_to_delete)
            sessionActive.commit()
            print(f"✅ User with ID {user_id_to_delete} deleted successfully.")
        else:
            print(f"❌ User with ID {user_id_to_delete} not found.")
    except Exception as e:
        sessionActive.rollback()
        print("❌ Error deleting user:", e)

def update_user():
    print("Updating user information...")
    user_id_to_update = int(input("Enter the ID of the user to update: "))
    try:
        user_to_update = sessionActive.query(user).filter(user.id == user_id_to_update).first()
        if user_to_update:
            new_name = input(f"Enter the new name for user ID {user_id_to_update} (leave blank to keep '{user_to_update.name}'): ")
            new_age = input(f"Enter the new age for user ID {user_id_to_update} (leave to blank to keep '{user_to_update.age}'): ")

            if new_name:
                user_to_update.name = new_name
            if new_age:
                user_to_update.age = int(new_age)
            
            sessionActive.commit()
            print(f"✅ User with ID {user_id_to_update} updated successfully.")
        else:
            print(f"❌ User with ID {user_id_to_update} not found.")
    except Exception as e:
        sessionActive.rollback()
        print("❌ Error updating user:", e)

if __name__ == "__main__":
    print("This file contains action finctions and is not maint to be run directly.")