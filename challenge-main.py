

alphabet = list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ") #create list of letters

encrypt_dict = {} #create empty dict to put letters and values

value = 0

for i in alphabet: #for every letter, set value to number
	value += 1
	encrypt_dict[i] = value

print encrypt_dict	


def encryption(message):
	#message = ("Secret Message")
	message_list = list(message)
	encrypted_mess = []
	for i in message_list:
		encrypted_mess.append(encrypt_dict[i])
	return message_list
	#goal: return message as numbers from encrypt_dict
print encryption("Secret Message")

