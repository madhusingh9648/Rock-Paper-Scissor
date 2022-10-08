from tkinter import *
from PIL import Image,ImageTk
from random import randint

 
#main windows
root=Tk()
root.title("Rock Paper Scissor")
root.configure(background="Pink")

#picture
rock_img=ImageTk.PhotoImage(Image.open("userrock.png"))
paper_img=ImageTk.PhotoImage(Image.open("userpaper.png"))
scissor_img=ImageTk.PhotoImage(Image.open("userscissor.png"))
rock_comp_img=ImageTk.PhotoImage(Image.open("rock.png"))
paper_comp_img=ImageTk.PhotoImage(Image.open("Paper.png"))
scissor_comp_img=ImageTk.PhotoImage(Image.open("Scissors.png"))

#insert picture
user_label = Label(root,image=scissor_img,background="Pink")
comp_label = Label(root,image=scissor_comp_img,background="Pink")
comp_label.grid(row=1,column=0)
user_label.grid(row=1,column=4)

#scores
playerScore = Label(root,text=0,font=100,background="Pink",fg="white")
ComputerScore=Label(root,text=0,font=100,background="Pink",fg="white")
ComputerScore.grid(row=1,column=1)
playerScore.grid(row=1,column=3)

#indicators
user_indicator = Label(root,font=50,text="USER",background="Pink",fg="white")
comp_indicator = Label(root,font=50,text="COMPUTER",background="Pink",fg="white")
user_indicator.grid(row=0,column=3)
comp_indicator.grid(row=0,column=1)


#messages 
msg = Label(root,font=50, bg="Pink",fg="white")
msg.grid(row=3,column=2)


#update message  
def updateMessage(x):
    msg['text'] = x

#update user score
def updateUserScore():
    score = int(playerScore["text"])
    score +=1
    playerScore["text"] = str(score)
#update computer score
def updateCompScore():
    score = int(ComputerScore["text"])
    score +=1
    ComputerScore["text"] = str(score)

#check winner
def checkwin(player,Computer):
    if player == Computer:
        updateMessage("Its a tie!!")
    elif player =="rock":
        if Computer == "paper":
            updateMessage("You loose")
            updateCompScore()
        else:
            updateMessage("You Win")
            updateUserScore()
    elif player =="paper":
        if Computer =="scissor":
            updateMessage("You loose")
            updateCompScore()
        else:
            updateMessage("You Win")
            updateUserScore()
    elif player =="scissor":
        if Computer =="rock":
            updateMessage("You loose")
            updateCompScore()
        else:
            updateMessage("You Win")
            updateUserScore()
    else:
        pass




#update choices

choices = ["rock","paper","scissor"]
def updateChoice(x):


#for computer
    compChoice = choices[randint(0,2)]
    if compChoice =="rock":
        comp_label.configure(image=rock_comp_img)
    elif compChoice =="paper":
        comp_label.configure(image=paper_comp_img)
    else:
        comp_label.configure(image=scissor_comp_img)




#for user
    if x=="rock":
        user_label.configure(image=rock_img)
    elif x=="paper":
        user_label.configure(image=paper_img)
    else:
        user_label.configure(image=scissor_img)
    
    checkwin(x,compChoice)

#buttons
rock = Button(root,width=20,height=2,text="ROCK",bg="Green",fg="White",command = lambda:updateChoice("rock")).grid(row=2,column=1)
paper = Button(root,width=20,height=2,text="PAPER",bg="Red",fg="White",command = lambda:updateChoice("paper")).grid(row=2,column=2)
scissor = Button(root,width=20,height=2,text="SCISSOR",bg="Blue",fg="White",command = lambda:updateChoice("scissor")).grid(row=2,column=3)



root.mainloop()
