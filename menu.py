from option import view_user, add_user, delete_user, update_user
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def display_menu(title, options):
    print(f"\n{title}\n{'=' * len(title)}")
    for i, option in enumerate(options):
        print(f"{i + 1}. {option}")
    print("0. Exit")

def get_user_choice(max_option):
    while True:
        try:
            choise = int(input("Enter your choise: "))
            if 0 <= choise <= max_option:
                return choise
            else:
                print("Invalid choice. Please enter a number from the menu.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def perform_action(choice, options):
    clear_screen()
    if choice == 0:
        print("Exiting...")
        return True
    elif 1<= choice <= len(options):
        selected_option = options[choice - 1]
        print(f"You selected:  {selected_option}")
        if selected_option == "View Users":
            view_user()
        elif selected_option == "Add User":
            add_user()
        elif selected_option == "Delete User":
            delete_user()
        elif selected_option == "Update User":
            update_user()
        input("\nPress Enter to return to the main menu...")
        return False
    return False

def main_menu():
    menu_title = "User Management System"
    menu_options = ["View Users", "Add User", "Delete User", "Update User"]

    while True:
        clear_screen()
        display_menu(menu_title, menu_options)
        choice = get_user_choice(len(menu_options))
        if perform_action(choice, menu_options):
            break

if __name__ == "__main__":
    main_menu()