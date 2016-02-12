

#numbers = "1,2,3,4,5" # creating initial string
#def convert_str_to_int(numbers): # converting strings to integers
#	numbers_list = numbers.split(",") # splitting string
#	print numbers_list
#	integers_list = [] # creating list
#	for i in numbers_list: # loop to make str into int
#		integers_list.append(int(i)) # adding int to list and casting str 
#									#as int
#	return integers_list

#print convert_str_to_int(numbers)

fish = "one fish two fish red fish blue fish"
def fish_to_string(fish):
	fishes = fish.split(" ")
	print fishes

	fish_index = 0
	fishes_id =[]
	for i in fishes:
		if fish_index % 2 == 0:
			fish_id[i] = fishes[fish_index + 1]
		fish_index += 1
	return fish_id

print fish_to_string(fish)
