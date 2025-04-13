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

def update_user():
    print("Updating user information...")

if __name__ == "__main__":
    print("This file contains action finctions and is not maint to be run directly.")