user = raw_input("Rock-Paper-Scissors?")
user = user.lower()

import random

choices = ["Rock", "Paper", "Scissors"]
computer = random.choice(choices)

if user == computer:
	print "Draw"
elif user == "rock":
	if computer == "scissors":
		print "User Wins"
	else:
		print "Computer Wins"
elif user == "scissors":
	if computer == "paper":
		print "User Wins"
	else:
		print "Computer Wins"
elif user == "paper":
	if computer == "rock":
		print "User Wins"
	else:
		print "Computer Wins"

