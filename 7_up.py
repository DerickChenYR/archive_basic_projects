#rule of the game - multiples of 7, numbers containing 7 - all up
#python 2


#core
def seven_up(num):

	if num %7 ==0 or any(i in str(num) for i in ('7')):
		print ("Up!")
	else:
		print (num)
	

#seven_up(num)

#seven_up(17)
#seven_up(21)
#seven_up(3)





#userInput
userInput = input("Enter Number:    ")
if userInput.isdigit():
	print ("...Accepted")
	seven_up(int(userInput))
else:
	print ("Only numbers are accepted.")



#problem: cannot enter another number witout rebuilding. Loop?