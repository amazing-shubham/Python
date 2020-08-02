from tkinter import *
import random

root = Tk()
root.geometry("500x350")
root.title('Rock Paper Scissors')
# creating new frame
newframe = Frame(root)
newframe.pack()

user_score = 0
comp_score = 0
user_choice = ""
comp_choice = ""


# convert choice to number
def conversion_choice_to_number(choice):
    a = {'Rock': 0, 'Paper': 1, 'Scissors': 2}
    return s[choice]


# convert number to choice
def conversion_number_to_choice(number):
    a = {0: 'Rock', 1: 'Paper', 2: 'Scissors'}
    return s[number]

# random selection by computer
def random_generation():
    list = ['Rock', 'Paper', 'Scissors']
    selection = random.choice(list)
    computerselection['text'] = selection
    return selection

# function for play
def play():


# Adding label of the frame
label = Label(newframe, text="Select any one of the following options:", anchor='center', fg="Red")
label.pack()

# adding buttons for rock, paper and scissors
rockButton = Button(newframe, text="ROCK", bg="Light Blue", command=lambda: random_generation())
rockButton.pack(padx=40, pady=10)
paperButton = Button(newframe, text="PAPER", bg="Yellow", command=lambda: random_generation())
paperButton.pack(padx=40, pady=10)
scissorButton = Button(newframe, text="SCISSORS", bg="Light Green", command=lambda: random_generation())
scissorButton.pack(padx=40, pady=10)

# adding textArea and inner content
textArea = Text(newframe, bg='peachpuff', height=20, width=50, relief='ridge')
textArea.pack()

insideTextArea = Label(textArea, text="Enter no. of round you wants to play:", anchor='w', bg='peachpuff')
insideTextArea.grid(row=0, column=0)
box = Entry(textArea)
box.grid(row=0, column=1)

inside_TextArea2 = Label(textArea, text="Computer Selected:", anchor='w', bg='peachpuff')
inside_TextArea2.grid(row=2, column=0)
computer_selection = Label(textArea, bg='peachpuff')
computer_selection.grid(row=2, column=1)

inside_TextArea4 = Label(textArea, text="Your's Score:", anchor='w', bg='peachpuff')
inside_TextArea4.grid(row=4, column=0)
your_score = Label(textArea, bg='peachpuff', text='0')
your_score.grid(row=4, column=1)

inside_TextArea6 = Label(textArea, text="Computer's Score:", anchor='w', bg='peachpuff')
inside_TextArea6.grid(row=6, column=0)
comp_score = Label(textArea, bg='peachpuff', text='0')
comp_score.grid(row=6, column=1)

textArea2 = Text(newframe, bg='sandybrown', height=2, width=15, relief='ridge')
textArea2.pack()

root.mainloop()
