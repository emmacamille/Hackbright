class Contact(object):
	def __init__(self, first_name, last_name):
		self.first_name = first_name
		self.last_name = last_name
		self.email_address = ""
		self.mobile_number = ""

	def send_email(self, message):
		print "To %s - %s" %(self.email_address, message)

	 