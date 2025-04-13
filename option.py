from database import engine, base, session, sessionActive, user

# Function to retrieve and display all users from the database
def view_user():
    print("Listening all users...") # Typo in original: "Listening" should be "Listing"
    try:
        users = sessionActive.query(user).all() # Query the 'user' table and retrieve all records
        if users:
            for u in users:
                print(f"ID: {u.id}, Name: {u.name}, Age: {u.age}") # Print the details of each user
        else:
            print("No users found in the database.")
    except Exception as e:
        print("Error retrieving users:", e) # Print any error that occurs during retrieval

# Function to add a new user to the database
def add_user():
    name = input("Enter the new user's name: ")
    age = int(input("Enter the new user's age: "))
    new_user = user(name=name, age=age) # Create a new 'user' object
    sessionActive.add(new_user) # Add the new user object to the session
    try:
        sessionActive.commit() # Commit the changes to the database
        print("Adding a new user...")
    except Exception as e:
        sessionActive.rollback() # If an error occurs, rollback the transaction
        print("❌ Error adding user:", e) # Print the error message

# Function to delete a user from the database
def delete_user():
    print("Deleting a user...") # Typo in original: "Dalating" should be "Deleting"
    user_id_to_delete = int(input("Enter the ID of the user to delete: "))
    try:
        user_to_delete = sessionActive.query(user).filter(user.id == user_id_to_delete).first() # Query for the user with the given ID
        if user_to_delete:
            sessionActive.delete(user_to_delete) # Mark the user object for deletion
            sessionActive.commit() # Commit the deletion to the database
            print(f"✅ User with ID {user_id_to_delete} deleted successfully.")
        else:
            print(f"❌ User with ID {user_id_to_delete} not found.")
    except Exception as e:
        sessionActive.rollback() # If an error occurs, rollback the transaction
        print("❌ Error deleting user:", e) # Print the error message

# Function to update the information of an existing user in the database
def update_user():
    print("Updating user information...")
    user_id_to_update = int(input("Enter the ID of the user to update: "))
    try:
        user_to_update = sessionActive.query(user).filter(user.id == user_id_to_update).first() # Query for the user with the given ID
        if user_to_update:
            new_name = input(f"Enter the new name for user ID {user_id_to_update} (leave blank to keep '{user_to_update.name}'): ")
            new_age = input(f"Enter the new age for user ID {user_id_to_update} (leave to blank to keep '{user_to_update.age}'): ") # Typo in original: "leave to blank" should be "leave blank"

            if new_name:
                user_to_update.name = new_name # Update the user's name if a new one is provided
            if new_age:
                user_to_update.age = int(new_age) # Update the user's age if a new one is provided
            
            sessionActive.commit() # Commit the updates to the database
            print(f"✅ User with ID {user_id_to_update} updated successfully.")
        else:
            print(f"❌ User with ID {user_id_to_update} not found.")
    except Exception as e:
        sessionActive.rollback() # If an error occurs, rollback the transaction
        print("❌ Error updating user:", e) # Print the error message

# This block executes only when this script is run directly
if __name__ == "__main__":
    print("This file contains action functions and is not meant to be run directly.") # Corrected typo in original: "finctions" to "functions" and "maint" to "meant"