
# count letters in file
# not the prettiest, but it works!

text_file_fo = open("one_fish.txt")
text_file_list = text_file_fo.read()
text_file_fo.close()

def letters_to_count(file_for_count):
	count_dict = {}
	file_for_count = file_for_count.replace("\n"," ")
	file_for_count = file_for_count.replace(",", "")
	file_for_count = file_for_count.replace(".", "")
	file_for_count = file_for_count.replace("!", "")
	file_for_count = file_for_count.replace("?", "")
	file_for_count = file_for_count.replace(" ", "")
	file_for_count = file_for_count.replace("\xe2\x80\x99t","")
		# removes all punctionation. Line 12 is apostrophe.
	file_for_count = file_for_count.lower()
	for i in file_for_count:
		if (i not in count_dict):
			count_dict[i] = 1
		else:
			count_dict[i] += 1
	return count_dict

print letters_to_count(text_file_list)

# count words in file

def words_to_count(file_for_count):
	word_count_dict = {}
	file_for_count = file_for_count.replace("\n"," ")
	file_for_count = file_for_count.replace(",", "")
	file_for_count = file_for_count.replace(".", "")
	file_for_count = file_for_count.replace("!", "")
	file_for_count = file_for_count.replace("?", "")
	file_for_count = file_for_count.replace("\xe2\x80\x99t","")
		# removes all punctionation. Line 12 is apostrophe.
	file_for_count = file_for_count.lower()
	file_for_count = file_for_count.split(" ")
	for i in file_for_count:
		if (i not in word_count_dict):
			word_count_dict[i] = 1
		else:
			word_count_dict[i] += 1
	return word_count_dict

print words_to_count(text_file_list)

