# def draw_square(num):
# 	for i in range(num):
# 		print ("* " * num)

# print draw_square(8)

def draw_checkerboard():
	for i in range(64):
		if i % 2:
			print "o",
		else:
			print "x",
	

print draw_checkerboard()