def sum_nums(num):
	total = 0
	for i in range(0, num):
		total = total + i
	return total

print sum_nums(10)

def sum_nums2(num):
	total = 0
	if num < 0:
		