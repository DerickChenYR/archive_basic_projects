from tkinter import *

test = Tk()

test.title("testing")
test.geometry("200x300")


def hi():
    print ("this is a test yo!")
    
testLabel = Label(test, text="whassup")
testLabel.grid(row = 0)

testButton = Button(test, text="this is button", command=hi)
testButton.grid(row = 1, column=1)

testEntry = Entry(test, width= 10)
testEntry.grid(row=0 , column =1)



test.mainloop()
