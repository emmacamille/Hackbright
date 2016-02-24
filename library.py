def fizz_buzz():
	nums = range(1, 101)
	i = 0
	while i < len(nums):
		if nums[i] % 3 == 0 and nums[i] % 5 != 0:
			print "Fizz"
		elif nums[i] %5 == 0 and nums[i] %3 != 0:
			print "Buzz"
		elif nums[i] %15 == 0:
			print "FizzBuzz"
		else:
			print nums[i]
		i = i + 1

