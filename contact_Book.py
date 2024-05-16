from contact import Contact
class ContactBook:
    def __init__(self):
        self.contact=[]
    def add_contact(self,contact):
        self.contact.append(contact)
        
    def display_all_contact(self):
        for contact in self.contact:
            contact.display_contact()
            print("------------------")

    def search_contact(self,name):
        for contact in self.contact:
            if contact.name.lower()==name.lower():
                return contact
        else:
            return None       

