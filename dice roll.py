#Dice Rolling Game, refresher
#rules - dice generate ranodm number 1-6, able to retsart

from random import randint

i = 0
loglist = []
turn = 0


#generate and print random number. DONE

def roll_dice(turn):

	i = randint(1,6)
	loglist.append(str(i))
	turn += 1
	print ("")
	print ("The number is.... " + str(i))


def log(i,loglist):
		print (" ")
		print ("Previous numbers were: ")
		print (", ".join(loglist))





roll_dice(turn)


#repeat function, DONE

while type(turn) == int :
	

	
		command = input("To start again, enter YES....")
		if command == "YES":

			roll_dice(turn)
			log(i,loglist)
			
			print ("")
			print ("")




