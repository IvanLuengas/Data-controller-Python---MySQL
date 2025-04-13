from option import view_user, add_user, delete_user, update_user
import os

# Function to clear the terminal screen
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear') # Checks the operating system to use the correct clear command

# Function to display a menu with a title and options
def display_menu(title, options):
    print(f"\n{title}\n{'=' * len(title)}") # Prints the title with an underline
    for i, option in enumerate(options):
        print(f"{i + 1}. {option}") # Prints each option with a number
    print("0. Exit") # Prints the exit option

# Function to get the user's choice from the menu, ensuring it's within the valid range
def get_user_choice(max_option):
    while True:
        try:
            choise = int(input("Enter your choise: ")) # Prompts the user to enter their choice
            if 0 <= choise <= max_option:
                return choise # Returns the valid choice
            else:
                print("Invalid choice. Please enter a number from the menu.") # Error message for out-of-range input
        except ValueError:
            print("Invalid input. Please enter a number.") # Error message for non-numeric input

# Function to perform the action corresponding to the user's choice
def perform_action(choice, options):
    clear_screen() # Clears the screen before performing the action
    if choice == 0:
        print("Exiting...") # Message when the user chooses to exit
        return True # Indicates that the main loop should break
    elif 1<= choice <= len(options):
        selected_option = options[choice - 1] # Gets the selected option from the list
        print(f"You selected:  {selected_option}") # Confirms the selected option
        if selected_option == "View Users":
            view_user() # Calls the function to view users
        elif selected_option == "Add User":
            add_user() # Calls the function to add a user
        elif selected_option == "Delete User":
            delete_user() # Calls the function to delete a user
        elif selected_option == "Update User":
            update_user() # Calls the function to update a user
        input("\nPress Enter to return to the main menu...") # Pauses the execution until the user presses Enter
        return False # Indicates that the main loop should continue
    return False # Default return if the choice is invalid

# Main function to display the menu and handle user interaction
def main_menu():
    menu_title = "User Management System"
    menu_options = ["View Users", "Add User", "Delete User", "Update User"]

    while True:
        clear_screen() # Clears the screen at the beginning of each menu display
        display_menu(menu_title, menu_options) # Displays the menu
        choice = get_user_choice(len(menu_options)) # Gets the user's choice
        if perform_action(choice, menu_options): # Performs the action based on the choice
            break # Exits the main loop if the user chose to exit

# This block ensures that the main_menu function is called only when this script is executed directly
if __name__ == "__main__":
    main_menu()