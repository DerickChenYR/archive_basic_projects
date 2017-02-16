from random import randint

from tkinter import *

#turn = 0
userScore = 0
compScore = 0




def outcome(userInput):
	
	#print "comp inputs = %s" % compInput

	global userScore
	global compScore




	if userInput == 1 and compInput == 3:
		print ("you win!")
		userScore += 1
	elif compInput == 1 and userInput == 3:
		print ("you lose!")
		compScore +=1
	elif userInput == 2 and compInput == 1:
		print ("you win!")
		userScore += 1
	elif compInput == 2 and userInput == 1:
		print ("you lose!")
		compScore += 1
	elif userInput == 3 and compInput == 2:
		print ("you win!")
		userScore += 1
	elif compInput == 3 and userInput == 2:
		print ("you lose!")
		compScore += 1
	elif userInput == compInput:
		print ("draw!")




def execute():


	global compInput
	compInput = randint(1,3)

	print("executing")

	print ("user - " , str(userInput))
	print("comp -" , str(compInput))

	outcome(userInput)
	print ("Player : %s / Computer : %s" % (userScore, compScore))
	print()







#	for turn in range(3):
#
#		turn +=1
#		
#		while True:
#		
#			if turn <= 3:
#				outcome(userInput, compInput)
#				print()
#				print ("Turn %s" % turn)
#				print ("Player : %s / Computer : %s" % (userScore, compScore))
#				print ("***")
#				print()
#				print()
#				break
#			else:
#				break
#				print()
#				print ("--------------------")
#				print (")Game Over!")
#				print ("Player : %s / Computer : %s" % (userScore, compScore))
		


def userRock():
	global userInput
	userInput = 1

	print (userInput)
	return userInput

def userPaper():
	global userInput
	userInput = 2

	print (userInput)
	return userInput

def userScissors():
	global userInput
	userInput = 3

	print (userInput)
	return userInput

#def test():
#	print ("test")





#GUI codes
sps = Tk()


sps.title("The SPS Game")
sps.geometry("400x100")

sps_description = Label(sps, text="This is a rock paper scissors game with your computer!")
sps_description.grid(row = 0, columnspan = 3)


#t = StringVar()
#user_turnInput = Entry(sps,textvariable = t)
#user_turnInput.pack()

user_rock = Button(sps, text="Rock", command = userRock, width=10 )
user_rock.grid(row=1, column = 0)

#button pressed
#user_rock.config(relief= SUNKEN)

user_paper = Button(sps, text="Paper", command = userPaper, width=10 )
user_paper.grid(row=1, column = 1)

user_scissors = Button(sps, text="Scissors", command = userScissors, width=10 )
user_scissors.grid(row=1, column = 2)

user_run = Button (sps, text="Run!", command = execute, width = 43 )
user_run.grid(row=2, columnspan= 3)


#stretchable columns, widgets expand out
sps.columnconfigure(0,weight =1)
sps.columnconfigure(1,weight =1)
sps.columnconfigure(2,weight =1)
sps.mainloop()
