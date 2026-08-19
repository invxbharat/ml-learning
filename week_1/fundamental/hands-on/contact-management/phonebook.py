class Phonebook:

    def __init__(self):
        self.__contacts = []

    def addContact(self, contact): # dont store duplicate contacts based on name, email, or phone number
        for existing_contact in self.__contacts:
            if (existing_contact.getName() == contact.getName() or
                existing_contact.getEmail() == contact.getEmail() or
                existing_contact.getPhone() == contact.getPhone()):
                print("Contact already exists.")
                return
        self.__contacts.append(contact)

    def removeContact(self, contact):
        if contact in self.__contacts:
            self.__contacts.remove(contact)
        else:
            print("Contact not found.")

    def getContacts(self):
        return self.__contacts

    def displayContacts(self):
        for contact in self.__contacts:
            print(contact)

    def searchContactByNameOrEmailOrPhone(self, query): #contains search functionality for name, email, or phone number # return list of contacts that match the query
        results = []
        for contact in self.__contacts:
           q = query.lower()
           if q in contact.getName().lower() or q in contact.getEmail().lower() or q in contact.getPhone():
                results.append(contact)
        if results:
            return results
        return None

import contact

phonebook = Phonebook()
contact1 = contact.Contact("John Doe", "john.doe@example.com", "123-456-7890")
phonebook.addContact(contact1)
contact2 = contact.Contact("Jane Smith", "jane.smith@example.com", "098-765-4321")
phonebook.addContact(contact2)
contact3 = contact.Contact("Alice Johnson", "alice.johnson@example.com", "555-123-4567")
phonebook.addContact(contact3)
phonebook.addContact(contact3)

phonebook.displayContacts()

phonebook.removeContact(contact2)

phonebook.displayContacts()

contacts = phonebook.searchContactByNameOrEmailOrPhone("Alice")
if contacts:
    print("Contacts found:")
    for contact in contacts:
        print(contact)
else:
    print("No contacts found.")