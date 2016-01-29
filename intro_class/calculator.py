def add_num(num1, num2):
	total = num1 + num2
	return total

def subtract_num(num1, num2):
	difference = num1 - num2
	return difference

def multiply_num(num1,num2):
	total_mult = num1 * num2
	return total_mult

def divide_num(num1,num2):
	divided = num1/num2
	return divided

def modulo(num1,num2):
	remainder = num1%num2
	return remainder

def power(num1,num2):
	to_the_power = num1**num2
	return to_the_power

def num_squared(num1):
	squared = num1**2
	return squared

age = add_num(30, 4)
height = subtract_num(78, 2)
weight = multiply_num(6, 24)
iq = divide_num(100, 2)

print "Age: %d, Height: %d, Weight: %d, IQ: %i." %(age, height, weight, iq)
