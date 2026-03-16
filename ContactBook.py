import json
import os

# File where contacts will be permanently stored
DATA_FILE = "contacts.json"


# -----------------------------
# Load contacts from JSON file
# -----------------------------
def load_contacts():
    """
    Reads contacts from contacts.json.
    If the file does not exist yet, return an empty list.
    """
    if not os.path.exists(DATA_FILE):
        return []

    with open(DATA_FILE, "r") as file:
        try:
            return json.load(file)
        except json.JSONDecodeError:
            # If JSON is empty or corrupted, return empty list
            return []


# -----------------------------
# Save contacts to JSON file
# -----------------------------
def save_contacts(contacts):
    """
    Writes the contact list to contacts.json so
    the data persists after the program closes.
    """
    with open(DATA_FILE, "w") as file:
        json.dump(contacts, file, indent=4)


# -----------------------------
# Validate name input
# -----------------------------
def valid_name(name):
    """
    Ensures the name contains only letters and spaces.
    """
    return name.replace(" ", "").isalpha()


# -----------------------------
# Validate phone number input
# -----------------------------
def valid_phone(phone):
    """
    Ensures the phone number contains only digits.
    """
    return phone.isdigit()


# -----------------------------
# Add a new contact
# -----------------------------
def add_contact(contacts):
    """
    Prompts user for contact information and saves it.
    """

    name = input("Enter name: ")

    # Validate name
    if not valid_name(name):
        print("Error: Name must contain only letters.")
        return

    phone = input("Enter phone number: ")

    # Validate phone number
    if not valid_phone(phone):
        print("Error: Phone number must contain digits only.")
        return

    address = input("Enter address: ")
    email = input("Enter email: ")

    # Create contact dictionary
    contact = {
        "name": name,
        "phone": phone,
        "address": address,
        "email": email
    }

    contacts.append(contact)
    save_contacts(contacts)

    print("Contact added successfully!")


# -----------------------------
# View all contacts
# -----------------------------
def view_contacts(contacts):
    """
    Displays all contacts stored in the system.
    """

    if not contacts:
        print("No contacts found.")
        return

    print("\nContact List")
    print("------------")

    for contact in contacts:
        print(f"Name: {contact['name']}")
        print(f"Phone: {contact['phone']}")
        print(f"Address: {contact['address']}")
        print(f"Email: {contact['email']}")
        print("-------------------")


# -----------------------------
# Search for a contact by name
# -----------------------------
def search_contact(contacts):
    """
    Finds and displays a contact by name.
    """

    name = input("Enter name to search: ").lower()

    for contact in contacts:
        if contact["name"].lower() == name:
            print("\nContact Found")
            print(f"Name: {contact['name']}")
            print(f"Phone: {contact['phone']}")
            print(f"Address: {contact['address']}")
            print(f"Email: {contact['email']}")
            return

    print("Contact not found.")


# -----------------------------
# Delete contact by name
# -----------------------------
def delete_contact(contacts):
    """
    Removes a contact from the list by name.
    """

    name = input("Enter name of contact to delete: ").lower()

    for contact in contacts:
        if contact["name"].lower() == name:
            contacts.remove(contact)
            save_contacts(contacts)
            print("Contact deleted.")
            return

    print("Contact not found.")


# -----------------------------
# Display menu
# -----------------------------
def show_menu():
    """
    Prints the application menu.
    """
    print("\nContact Book")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5. Exit")


# -----------------------------
# Main program loop
# -----------------------------
def main():

    # Load existing contacts from JSON file
    contacts = load_contacts()

    while True:

        show_menu()

        choice = input("Select an option: ")

        if choice == "1":
            add_contact(contacts)

        elif choice == "2":
            view_contacts(contacts)

        elif choice == "3":
            search_contact(contacts)

        elif choice == "4":
            delete_contact(contacts)

        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print("Invalid option. Please choose again.")


# Run the program
if __name__ == "__main__":
    main()