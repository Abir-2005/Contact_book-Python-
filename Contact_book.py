''' Contact Information: Store name, phone number, email, and address for each contact.

Add Contact: Allow users to add new contacts with their details.

View Contact List: Display a list of all saved contacts with names and phone numbers.
Search Contact: Implement a search function to find contacts by name or phone number.

Update Contact: Enable users to update contact details.
Delete Contact: Provide an option to delete a contact.

User Interface: Design a user-friendly interface for easy interaction.'''
contacts = {}

def add_contact():
    """Adds a new contact to the contacts dictionary."""
    name = input("Enter name: ")
    phone = input("Enter phone number: ")

    # Check if the contact name already exists
    if name in contacts:
        print("This contact already exists.")
    else:
        # Add the new contact to the dictionary
        contacts[name] = phone
        print("Contact added successfully.")

def delete_contact():
    """Deletes an existing contact from the dictionary."""
    name = input("Enter name: ")

    # Check if the contact exists before deleting
    if name in contacts:
        del contacts[name]
        print("Contact deleted successfully.")
    else:
        print("This contact does not exist.")

def update_contact():
    """Updates the phone number of an existing contact."""
    name = input("Enter name: ")
    
    # Check if the contact exists before updating
    if name in contacts:
        new_phone = input("Enter the new phone number: ")
        contacts[name] = new_phone
        print("Contact updated successfully.")
    else:
        print("This contact does not exist.")

def search_contact():
    """Searches for a contact by name in a case-insensitive manner."""
    search_term = input("Enter name to search: ").lower()
    found = False
    
    # Iterate through contact names to find a match
    for contact_name in contacts.keys():
        if search_term in contact_name.lower():
            print(f"Contact Found: {contact_name}")
            print(f"Phone number: {contacts[contact_name]}")
            found = True
            break
    
    if not found:
        print("Contact not found.")

def display_contacts():
    """Displays all contacts in the dictionary."""
    if not contacts:
        print("There are no contacts.")
    else:
        print("\nContacts List:")
        for name, phone in contacts.items():
            print(f"Name: {name}, Phone: {phone}")

while True:
    print("\nContact Book Menu:")
    print("1. Add Contact")
    print("2. Delete Contact")
    print("3. Update Contact")
    print("4. Search Contact")
    print("5. Display Contacts")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ")

    if choice == '1':
        add_contact()
    elif choice == '2':
        delete_contact()
    elif choice == '3':
        update_contact()
    elif choice == '4':
        search_contact()
    elif choice == '5':
        display_contacts()
    elif choice == '6':
        print("Exiting Contact Book. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 6.")
