def sum_num(num):
	nums = range(0,num)
	i = 0
	total = 0
	while i < len(nums):
		total = total + nums[i]
		i = i + 1
	return total

#print sum_num(4)

def sum_nums2(num):
	i = 0
	total = 0
	if num < 0 :
		nums = range(num, 0)
		while i < len(nums):
			total = total + nums[i]
			i = i + 1
	else:
		nums = range(0, num)
		while i < len(nums):
			total = total + nums[i]
			i = i + 1
	return total

print sum_nums2(-3)