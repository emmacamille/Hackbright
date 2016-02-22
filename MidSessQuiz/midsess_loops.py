# def draw_square(num):
# 	for i in range(num):
# 		print ("* " * num)

# print draw_square(8)

def draw_checkerboard():
	counter = 1

	for i in range(1, 65):
		if (counter % 2 != 0) : # odd rows start with "x"
			#print (i % 2),
			if (i % 2 == 0):
				print "o",
			else:
				print "x",
			#print (i % 8),
			if (i % 8 == 0):
				print "\n"
				counter += 1

		else: # row starts with "o"
			#print (i % 2),
			if (i % 2 == 0):
				print "x",
			else:
				print "o",
			#print (i % 8),
			if (i % 8 == 0):
				print "\n"
				counter += 1
	

print draw_checkerboard()