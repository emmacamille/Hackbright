def prime_or_no(num):
	#num = raw_input("Enter an interger:")
	for i in range(2, num):
		if num % i == 0:
			return False
	return True


input_number = int(raw_input("Enter an interger:"))

if prime_or_no(input_number):
	print "True, %i is a prime number!" %(input_number)
else: print "False, %i is not a prime number!" %(input_number)