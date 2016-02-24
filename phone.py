import contacts

contact_emma = contacts.Contact("Emma", "Schacter")
contact_hillary = contacts.Contact ("Hillary", "Lounsbury")
contact_alfred = contacts.Contact("Alfred", "Hitchcock")



contacts_list = []
contacts_list.append(contact_emma)
contacts_list.append(contact_hillary)
contacts_list.append(contact_alfred)

contact_emma.email_address = "emma@emma.com"
contact_alfred.email_address = "alf@hitch.com"

# for item_contact in contacts_list:
# 	print item_contact.first_name, item_contact.last_name

for item_contact in contacts_list:
	item_contact.send_email("Hello, how are you")