food_price_tuple = ('sushi', 7.50, 'burrito', 8.20, 'cheeseburger', 6.00, 'hot dog', 3.40, 'fried rice', 9.99)

food_dictionary = {}

def tuple_to_dictionary (tup):
	food_dictionary[tup[0]] = (tup[1])
	food_dictionary[tup[2]] = (tup[3])
	food_dictionary[tup[4]] = (tup[5])
	food_dictionary[tup[6]] = (tup[7])
	food_dictionary[tup[8]] = (tup[9])
	return food_dictionary


tuple_to_dictionary(food_price_tuple)

print food_dictionary['sushi']
print food_dictionary