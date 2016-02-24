text_file_fo = open("testText.txt")
text_file_list = text_file_fo.readlines()
text_file_fo.close()

text_file_list = text_file_list.split("\n")

print text_file_list

count_dict = {}

# text_file_list = text_file_list.upper()

# def count_letters():
# for i in text_file_list:
# 	if (i not in count_dict):
# 		count_dict[i] = 1
# 	else:
# 		count_dict[i] += 1
# 	# return count_dict

# print count_dict