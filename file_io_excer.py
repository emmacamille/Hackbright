emma_favfoods_ = open("emma_fav_foods.txt")
emma_list = emma_favfoods.readlines()
emma_favfoods.close()

hillary_favfoods_fo = open("hillary_fav_foods.txt")
hillary_list = hillary_favfoods.readlines()
hillary_favfoods.close()

print emma_list
print hillary_list

def compare_favs(list1, list2):
	if emma_list[1] == hillary_list[1]:
		print "Our favorite foods are the same!"
	else:
		print "Our favorite foods are different!"
	return fav_compared

print compare_favs(emma_list, hillary_list)
