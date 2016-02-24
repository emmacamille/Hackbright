food_price_tuple = ('sushi', 7.50, 'burrito', 8.20, 'cheeseburger', 6.00, 'hot dog', 3.40, 'fried rice', 9.99)


def tuple_to_dictionary (tuple):
	item_index = 0 # creating a count of 
					# items in list
	food_dictionary = {} #create empty list
	for item in tuple: # loop to count every
						# other item
		if item_index % 2 == 0: #check for key
			food_dictionary[item] = tuple[item_index + 1]
		item_index += 1 # moving to next key
	return food_dictionary

food_dictionary = tuple_to_dictionary(food_price_tuple)
	# calling the function
	
print food_dictionary
print food_dictionary["sushi"]
