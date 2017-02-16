#Goal
#Ask the player if they pick rock paper or scissors
#Have the computer chose its move
#Compare the choices and decide who wins
#Print the results

#Subgoals
#Let the player play again
#Keep a record of the score e.g. (Player: 3 / Computer: 6)



from random import randint

turn = 0
userScore = 0
compScore = 0


compInput = randint(1,3)

def outcome(userInput, compInput):
	userInput = int(userInput)
	#print "comp inputs = %s" % compInput
	global userScore
	global compScore

	if userInput == 1 and compInput == 3:
		print "you win!"
		userScore += 1
	elif compInput == 1 and userInput == 3:
		print "you lose!"
		compScore +=1
	elif userInput == 2 and compInput == 1:
		print "you win!"
		userScore += 1
	elif compInput == 2 and userInput == 1:
		print "you lose!"
		compScore += 1
	elif userInput == 3 and compInput == 2:
		print "you win!"
		userScore += 1
	elif compInput == 3 and userInput == 2:
		print "you lose!"
		compScore += 1
	elif userInput == compInput:
		print "draw!"


for turn in range(3):

	turn +=1
	userInput = raw_input("1 for rock, 2 for paper, 3 for scissors. What is your choice?       ")

	while True:
	
		if int(userInput) < 4:
			print "accepted"
			outcome(userInput, compInput)
			print
			print "Turn %s" % turn
			print "Player : %s / Computer : %s" % (userScore, compScore)
			print "***"
			print
			print
			break
		else:
			userInput = raw_input ("Invalid entry - enter a number from 1 to 3:       ")
		


if turn == 3:
	print
	print "--------------------"
	print "Game Over!"
	print "Player : %s / Computer : %s" % (userScore, compScore)





