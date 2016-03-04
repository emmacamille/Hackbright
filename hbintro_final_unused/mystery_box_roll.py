import random
import myster_box


def myster_box_roll(outcomes):

	print "Welcome to the Mystery Box Challenge! Roll the dice to find out what's in your Mystery Box!" 
	yes_no_answer = raw_input("Are you ready to roll? Yes or no?")

	if yes_no_answer == "NO" or yes_no_answer == "no":
		print "Are you that scared of what's in the box? Fine, be that way."
			#end program
	else: 
		print "Here is your shopping list:"
		for food_type in mystery_categories:
			print random.choice()
			# how do you iterate through each of the lists...
		print "Now, get cooking!"