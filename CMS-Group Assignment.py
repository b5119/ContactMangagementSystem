class Contact:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

class ContactList:
    def __init__(self):
        self.contacts = {}

    def add_contact(self, contact):
        self.contacts[contact.name] = contact

    def get_contact(self, name):
        return self.contacts.get(name)

    def update_contact(self, name, new_phone, new_email):
        contact = self.get_contact(name)
        if contact:
            contact.phone = new_phone
            contact.email = new_email
            return True
        return False

    def delete_contact(self, name):
        if name in self.contacts:
            del self.contacts[name]
            return True
        return False

    def generate_report(self):
        if self.contacts:
            print("Contact List:")
            for contact in self.contacts.values():
                print(f"Name: {contact.name}, Phone: {contact.phone}, Email: {contact.email}")
        else:
            print("Contact list is empty.")

class HistoryStack:
    def __init__(self):
        self.stack = []

    def push_operation(self, operation):
        self.stack.append(operation)

    def pop_operation(self):
        if self.stack:
            return self.stack.pop()
        else:
            return None

class ContactManager:
    def __init__(self):
        self.contact_list = ContactList()
        self.history = HistoryStack()

    def add_contact(self, name, phone, email):
        contact = Contact(name, phone, email)
        self.contact_list.add_contact(contact)
        self.history.push_operation(f"Added contact: {name}")
        print("Contact added successfully.")

    def update_contact(self, name, new_phone, new_email):
        if self.contact_list.update_contact(name, new_phone, new_email):
            self.history.push_operation(f"Updated contact: {name}")
            print("Contact updated successfully.")
        else:
            print("Contact not found.")

    def delete_contact(self, name):
        if self.contact_list.delete_contact(name):
            self.history.push_operation(f"Deleted contact: {name}")
            print("Contact deleted successfully.")
        else:
            print("Contact not found.")

    def generate_report(self):
        self.contact_list.generate_report()

# Sample usage:
contact_manager = ContactManager()

while True:
    print("\n1. Add Contact\n2. Update Contact\n3. Delete Contact\n4. Generate Report\n5. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter name: ")
        phone = input("Enter phone: ")
        email = input("Enter email: ")
        contact_manager.add_contact(name, phone, email)
    elif choice == "2":
        name = input("Enter name of contact to update: ")
        new_phone = input("Enter new phone: ")
        new_email = input("Enter new email: ")
        contact_manager.update_contact(name, new_phone, new_email)
    elif choice == "3":
        name = input("Enter name of contact to delete: ")
        contact_manager.delete_contact(name)
    elif choice == "4":
        contact_manager.generate_report()
    elif choice == "5":
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please try again.")
    
    input("Press Enter to continue...")  # Wait for user input before returning to main menu
