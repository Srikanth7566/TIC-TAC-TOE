from tkinter import *
import random


def winner():
    for row in range(3):
        if buttons[row][0]['text'] == buttons[row][1]['text'] == buttons[row][2]['text'] != '':
            buttons[row][0].config(bg='green')
            buttons[row][1].config(bg='green')
            buttons[row][2].config(bg='green')
            return True

    for column in range(3):
        if buttons[0][column]['text'] == buttons[1][column]['text'] == buttons[2][column]['text'] != '':
            buttons[0][column].config(bg='green')
            buttons[1][column].config(bg='green')
            buttons[2][column].config(bg='green')
            return True

    if buttons[0][0]['text'] == buttons[1][1]['text'] == buttons[2][2]['text'] != '':
        buttons[0][0].config(bg='green')
        buttons[1][1].config(bg='green')
        buttons[2][2].config(bg='green')
        return True
    elif buttons[0][2]['text'] == buttons[1][1]['text'] == buttons[2][0]['text'] != '':
        buttons[0][2].config(bg='green')
        buttons[1][1].config(bg='green')
        buttons[2][0].config(bg='green')
        return True
    elif empty() is False:
        for row in range(3):
            for column in range(3):
                buttons[row][column].config(bg='red')
        return "Tie"
    else:
        return False


def next_turn(row, column,):
    global player
    if buttons[row][column]["text"] == "" and winner() is False:

        if player == players[0]:
            buttons[row][column]['text'] = player
            if winner() is False:
                player = players[1]
                label.config(text=(players[1] + "-turn"))
            elif winner() is True:
                label.config(text=(players[0] + "-wins"))
            elif winner() == "Tie":
                label.config(text=("Tie!"))
        else:
            buttons[row][column]['text'] = player
            if winner() is False:
                player = players[0]
                label.config(text=(players[0] + "-turn"))
            elif winner() is True:
                label.config(text=(players[1] + "-wins"))
            elif winner() == "Tie":
                label.config(text="Tie!")


def empty():
    spaces = 9
    for row in range(3):
        for column in range(3):
            if buttons[row][column]['text'] != "":
                spaces -= 1
    if spaces == 0:
        return False
    else:
        return True


def restart():
    global player

    player = random.choice(players)
    label.config(text=player + '-turn')
    for i in range(3):
        for j in range(3):
            buttons[i][j].config(text="", bg="#F0F0F0")


window = Tk()
window.title("Tic-Tac-Toe")
players = ['x', 'o']
player = random.choice(players)
buttons = [[0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]]
label = Label(text=player + "-turn", font=('consolas', 40))
label.pack(side="top")
reset_button = Button(text="restart", font=('consolas', 20), command=restart)
reset_button.pack(side="top")

frame = Frame(window)
frame.pack()

for row in range(3):
    for column in range(3):
        buttons[row][column] = Button(frame, text="", font=('consolas', 40), width=5, height=2,
                               command=lambda row=row, column=column: next_turn(row, column))
        buttons[row][column].grid(row=row, column=column)

window.mainloop()





