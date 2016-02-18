def count_letters(full_name):
	print full_name
	letter_count = {}
	full_name = full_name.upper()
	for letter in full_name:
		if (letter not in letter_count):
			letter_count[letter] = 1
		else:
			letter_count[letter] += 1
	return letter_count

print count_letters(raw_input("What is your name?"))
