shoppinglist = ["apples", "coco", "wine"]

item = raw_input("What would you like to add to your list?")

if item in shoppinglist:
	print "Already on list! Duh!"

else:
	shoppinglist.append(item)
	shoppinglist.sort()
	print shoppinglist

shoppinglist[2] = item





