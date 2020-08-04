from tkinter import *
import random

root = Tk()
root.geometry("500x375")
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
    return a[choice]


# convert number to choice
def conversion_number_to_choice(number):
    a = {0: 'Rock', 1: 'Paper', 2: 'Scissors'}
    return a[number]


# random selection by computer
def random_generation():
    list = ['Rock', 'Paper', 'Scissors']
    selection = random.choice(list)
    computer_selection['text'] = selection
    return selection


# function for play
def play(comp_choice1, user_choice1):
    try:
        global user_score
        global comp_score
        global count
        user = conversion_choice_to_number(user_choice1)
        comp = conversion_choice_to_number(comp_choice1)
        if user == comp:
            textArea2.delete(1.0, END)
            textArea2.insert(END, "This round is TIE")

        elif (user - comp) % 3 == 1:
            user_score += 1
            your_score['text'] = user_score
            textArea2.delete(1.0, END)
            textArea2.insert(END, "This round is won by user")
        else:
            comp_score += 1
            comp_score1['text'] = comp_score
            textArea2.delete(1.0, END)
            textArea2.insert(END, "This round is won by Computer")
    except Exception:
        textArea2.delete(1.0, END)
        textArea2.insert(END, "ERROR")


# function of rock button
def ROCK():
    global user_choice
    global comp_choice
    user_choice = 'Rock'
    comp_choice = random_generation()
    play(comp_choice, user_choice)


# function of Paper button
def PAPER():
    global user_choice
    global comp_choice
    user_choice = 'Paper'
    comp_choice = random_generation()
    play(comp_choice, user_choice)


# function of rock button
def SCISSORS():
    global user_choice
    global comp_choice
    user_choice = 'Scissors'
    comp_choice = random_generation()
    play(comp_choice, user_choice)


# reset button
def reset():
    global user_score
    global comp_score
    user_score = 0
    comp_score = 0
    comp_score1['text'] = 0
    your_score['text'] = 0
    textArea2.delete(1.0, END)
    computer_selection['text'] = "*******"


# Adding label of the frame
label = Label(newframe, text="Select any one of the following options:", anchor='center', fg="Red")
label.pack()

# adding buttons for rock, paper and scissors
rockButton = Button(newframe, text="ROCK", bg="Light Blue", command=lambda: ROCK())
rockButton.pack(padx=40, pady=10)
paperButton = Button(newframe, text="PAPER", bg="Yellow", command=lambda: PAPER())
paperButton.pack(padx=40, pady=10)
scissorButton = Button(newframe, text="SCISSORS", bg="Light Green", command=lambda: SCISSORS())
scissorButton.pack(padx=40, pady=10)

# adding textArea and inner content
textArea = Text(newframe, bg='peachpuff', height=20, width=50, relief='ridge')
textArea.pack()

# insideTextArea = Label(textArea, text="Enter no. of round you wants to play:", anchor='w', bg='peachpuff')
# insideTextArea.grid(row=0, column=0)
# box = Entry(textArea)
# box.grid(row=0, column=1)

inside_TextArea2 = Label(textArea, text="Computer Selected:", anchor='w', bg='peachpuff')
inside_TextArea2.grid(row=2, column=0)
computer_selection = Label(textArea, text="*******", bg='peachpuff')
computer_selection.grid(row=2, column=1)

inside_TextArea4 = Label(textArea, text="Your's Score:", anchor='w', bg='peachpuff')
inside_TextArea4.grid(row=4, column=0)
your_score = Label(textArea, bg='peachpuff', text='0')
your_score.grid(row=4, column=1)

inside_TextArea6 = Label(textArea, text="Computer's Score:", anchor='w', bg='peachpuff')
inside_TextArea6.grid(row=6, column=0)
comp_score1 = Label(textArea, bg='peachpuff', text='0')
comp_score1.grid(row=6, column=1)

textArea2 = Text(newframe, bg='sandybrown', height=2, width=30, relief='ridge')
textArea2.pack()

resetButton = Button(newframe, text="RESET", bg="Red", command=lambda: reset())
resetButton.pack(padx=40, pady=10)

quitButton = Button(newframe, text="QUIT", bg="Green", command=lambda: newframe.quit())
quitButton.pack(padx=40, pady=10)

root.mainloop()
