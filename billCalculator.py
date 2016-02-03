# This is a comment and it not read by the interpreter
# These are useful for describing difficult code or adding reminders.
# TODO - fix this code :D
# (Part 1): Instead of using the hard coded ".18",
# Ask the user to input the percentage of tip they want to give. 
# Save the input to a variable. 
# Use the variable to calculate the tip.
# (Part 2): Fix any bugs and make it work!




def bill_total():
	bill = float(raw_input("How much was your bill?"))
	tip_percent = float(raw_input("What percentage of the bill would you like to tip?"))
	tip_total = bill * (tip_percent/100)
	total_bill = bill + tip_total
	print "The tip is %.2f and the total bill is %.2f." % (tip_total, total_bill)

def bill_split():
	bill = float(raw_input("How much was your bill?"))
	tip_percent = float(raw_input("What percentage of the bill would you like to tip?"))
	tip_total = bill * (tip_percent/100)
	total_bill = bill + tip_total
	number_paying = int(raw_input("How many people are in your party?"))
	total_bill_split = total_bill / number_paying
	print "Each peron will pay %.2f." %(total_bill_split)

print "Menu"
print "1- Bill Total"
print "2 - Bill Split"

choice = raw_input("Type '1' or '2' to select menu item.")

if choice == "1":
	bill_total()
else:
	bill_split()

