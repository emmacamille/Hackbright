def convert_to_seconds(hour, minute, second):
	hour = ((hour * 60) * 60)
	minute = (minute * 60)
	total_seconds = hour + minute + second
	return total_seconds

print convert_to_seconds(1, 1, 55)

def convert_to_inches(feet, inches):
	feet = (feet * 12)
	total_inches = feet + inches
	return total_inches

print convert_to_inches(1, 1)