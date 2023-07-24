import tkinter as tk
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk

board = [[0,0,0],[0,0,0],[0,0,0],[0,0,0]] #Create 4 by 4 Board for board and reset button
buttons = [[0,0,0],[0,0,0],[0,0,0],[0,0,0]] #Create corresponding buttons for each box
current_player = 'X'
player_x_score = 0
player_y_score = 0

def reset_close_tie_screen(root,tie_screen):
    reset_board(root)
    tie_screen.destroy()

def display_tie_screen(root):
    tie_screen = tk.Tk()
    tie_screen.title("Tie Screen")
    screen_width, screen_height = tie_screen.winfo_screenwidth(), tie_screen.winfo_screenheight()
    tie_screen.geometry('%dx%d+%d+%d' % (600, 600, (screen_width/2) - (600/2), (screen_height/2) - (600/2)))
    tie_screen.resizable(False,False) 

    background_photo = ImageTk.PhotoImage(master=tie_screen, image=Image.open("images/tie.png"))
    background_label = tk.Label(tie_screen, image=background_photo)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

    winner_label = tk.Label(tie_screen, text="It's a tie! \U0001F454", font=("Arial", 20, 'bold'), bg = "white")
    winner_label.place(relx=0.2, rely=0.5, anchor="center")
    close_button = tk.Button(tie_screen, text="Close", height = 2, width = 10, bg = "#C9E4FF", relief = SOLID, borderwidth=1, command=lambda: reset_close_tie_screen(root, tie_screen))
    close_button.place(relx=0.8, rely=.5, anchor="center")

    tie_screen.mainloop()

def reset_close_victory_screen(root,victory_screen):
    reset_board(root)
    victory_screen.destroy()

def display_victory_screen(winner,root):
    victory_screen = tk.Tk()
    victory_screen.title("Victory Screen")
    screen_width, screen_height = victory_screen.winfo_screenwidth(), victory_screen.winfo_screenheight()
    victory_screen.geometry('%dx%d+%d+%d' % (600, 400, (screen_width/2) - (600/2), (screen_height/2) - (400/2)))
    victory_screen.resizable(False,False) 

    background_photo = ImageTk.PhotoImage(master=victory_screen, image=Image.open("images/confetti.jpg"))
    background_label = tk.Label(victory_screen, image=background_photo)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

    if winner == 'O':
        winner = "〇"
    else:
        winner = "✕"
    winner_label = tk.Label(victory_screen, text="Player {} wins! \U0001F525".format(winner), font=("Arial", 20, 'bold'), bg = "white")
    winner_label.place(relx=0.5, rely=0.7, anchor="center")
    close_button = tk.Button(victory_screen, text="Close", height = 2, width = 10, bg = "#F08080", relief = SOLID, borderwidth=1, command=lambda: reset_close_victory_screen(root, victory_screen))
    close_button.place(relx=0.5, rely=.95, anchor="s")

    victory_screen.mainloop()

def check_win_or_draw(root):
    global board
    global player_x_score
    global player_y_score
    if board[0][0] == board[0][1] == board[0][2] and board[0][0] != 0:
        if (board[0][0] == 'X'):
            player_x_score = player_x_score + 1
            playerx_label.config(text="Player ✕: " + str(player_x_score))
        else:
            player_y_score = player_y_score + 1
            playery_label.config(text="Player 〇: " + str(player_y_score))
        display_victory_screen(board[0][0],root)
    elif board[1][0] == board[1][1] == board[1][2] and board[1][0] != 0:
        if (board[1][0] == 'X'):
            player_x_score = player_x_score + 1
            playerx_label.config(text="Player ✕: " + str(player_x_score))
        else:
            player_y_score = player_y_score + 1
            playery_label.config(text="Player 〇: " + str(player_y_score))
        display_victory_screen(board[1][0],root)
    elif board[2][0] == board[2][1] == board[2][2] and board[2][0] != 0:
        if (board[2][0] == 'X'):
            player_x_score = player_x_score + 1
            playerx_label.config(text="Player ✕: " + str(player_x_score))
        else:
            player_y_score = player_y_score + 1
            playery_label.config(text="Player 〇: " + str(player_y_score))
        display_victory_screen(board[2][0],root)
    elif board[0][0] == board[1][0] == board[2][0] and board[0][0] != 0:
        if (board[0][0] == 'X'):
            player_x_score = player_x_score + 1
            playerx_label.config(text="Player ✕: " + str(player_x_score))
        else:
            player_y_score = player_y_score + 1
            playery_label.config(text="Player 〇: " + str(player_y_score))
        display_victory_screen(board[0][0],root)
    elif board[0][1] == board[1][1] == board[2][1] and board[0][1] != 0:
        if (board[0][1] == 'X'):
            player_x_score = player_x_score + 1
            playerx_label.config(text="Player ✕: " + str(player_x_score))
        else:
            player_y_score = player_y_score + 1
            playery_label.config(text="Player 〇: " + str(player_y_score))
        display_victory_screen(board[0][1],root)
    elif board[0][2] == board[1][2] == board[2][2] and board[0][2] != 0:
        if (board[0][2] == 'X'):
            player_x_score = player_x_score + 1
            playerx_label.config(text="Player ✕: " + str(player_x_score))
        else:
            player_y_score = player_y_score + 1
            playery_label.config(text="Player 〇: " + str(player_y_score))
        display_victory_screen(board[0][2],root)
    elif board[0][0] == board[1][1] == board[2][2] and board[0][0] != 0:
        if (board[0][0] == 'X'):
            player_x_score = player_x_score + 1
            playerx_label.config(text="Player ✕: " + str(player_x_score))
        else:
            player_y_score = player_y_score + 1
            playery_label.config(text="Player 〇: " + str(player_y_score))
        display_victory_screen(board[0][0],root)
    elif board[0][2] == board[1][1] == board[2][0] and board[0][2] != 0:
        if (board[0][2] == 'X'):
            player_x_score = player_x_score + 1
            playerx_label.config(text="Player ✕: " + str(player_x_score))
        else:
            player_y_score = player_y_score + 1
            playery_label.config(text="Player 〇: " + str(player_y_score))
        display_victory_screen(board[0][2],root)
    elif 0 not in board[0] and 0 not in board[1] and 0 not in board[2]:
        display_tie_screen(root)

def draw(root,i,j):
    global buttons
    global current_player
    global board
    if buttons[i][j]['text'] == '':
        if current_player == "X":
            display_object = "✕"
        else:
            display_object = "〇"
        buttons[i][j].configure(text = display_object, font = ("Arial",80))
        board[i][j] = current_player
        if current_player == 'X': #Alternate between X and O
            current_player = 'O'
        else:
            current_player = 'X'
    check_win_or_draw(root)

def create_buttons(root):
    global buttons
    global playerx_label
    global playery_label
    button_color = "#AFEEEE"
    h = 5
    w = 10
    f = ("Arial",80)
    buttons[0][0] = Button(root, text = '', height = h, width = w, font = f, bg = button_color, relief = SUNKEN, borderwidth = 1, command = lambda:draw(root,0,0))
    buttons[0][0].grid(row = 0, column = 0, padx = (20,0), pady = (20,0))

    buttons[0][1] = Button(root, text = '', height = h, width = w, font = f, bg = button_color, relief = SUNKEN, borderwidth = 1, command = lambda:draw(root,0,1))
    buttons[0][1].grid(row = 0, column = 1, sticky = "nsew", pady = (20,0))

    buttons[0][2] = Button(root, text = '', height = h, width = w, font = f, bg = button_color, relief = SUNKEN, borderwidth = 1, command = lambda:draw(root,0,2))
    buttons[0][2].grid(row = 0, column = 2, sticky = "nsew", padx = (0,20), pady = (20,0))

    buttons[1][0] = Button(root, text = '', height = h, width = w, font = f, bg = button_color, relief = SUNKEN, borderwidth = 1, command = lambda:draw(root,1,0))
    buttons[1][0].grid(row = 1, column = 0, sticky = "nsew", padx = (20,0))

    buttons[1][1] = Button(root, text = '', height = h, width = w, font = f, bg = button_color, relief = SUNKEN, borderwidth = 1, command = lambda:draw(root,1,1))
    buttons[1][1].grid(row = 1, column = 1, sticky = "nsew")

    buttons[1][2] = Button(root, text = '', height = h, width = w, font = f, bg = button_color, relief = SUNKEN, borderwidth = 1, command = lambda:draw(root,1,2))
    buttons[1][2].grid(row = 1, column = 2, sticky = "nsew", padx = (0,20))

    buttons[2][0] = Button(root, text = '', height = h, width = w, font = f, bg = button_color, relief = SUNKEN, borderwidth = 1, command = lambda:draw(root,2,0))
    buttons[2][0].grid(row = 2, column = 0, sticky = "nsew", padx = (20,0))

    buttons[2][1] = Button(root, text = '', height = h, width = w, font = f, bg = button_color, relief = SUNKEN, borderwidth = 1, command = lambda:draw(root,2,1))
    buttons[2][1].grid(row = 2, column = 1, sticky = "nsew")

    buttons[2][2] = Button(root, text = '', height = h, width = w, font = f, bg = button_color, relief = SUNKEN, borderwidth = 1, command = lambda:draw(root,2,2))
    buttons[2][2].grid(row = 2, column = 2, sticky = "nsew", padx = (0,20))
    #Paddings to top, right, and left sides

    buttons[3][2] = Button(root, text = 'Reset Board', height = 3, width = 10, relief = SOLID, bg = "#F0FFF0", borderwidth=1, command = lambda:reset_board(root))
    buttons[3][2].grid(row = 3, column = 2, sticky = "ew", pady = 20, padx = (0,10))
    #Reset button

    playerx_label = tk.Label(root, text="Player ✕: " + str(player_x_score), font = ("Arial",20), bg = "#E6E6FA")
    playerx_label.grid(row=3, column=0)

    playery_label = tk.Label(root, text="Player 〇: " + str(player_y_score), font = ("Arial",20), bg = "#E6E6FA" )
    playery_label.grid(row=3, column=1)
    #Player scores

def reset_board(root):
    global board 
    global buttons
    global current_player
    current_player = 'X'
    board = [[0,0,0],[0,0,0],[0,0,0],[0,0,0]]
    buttons = [[0,0,0],[0,0,0],[0,0,0],[0,0,0]]
    create_buttons(root)

def create_gui():
    root = tk.Tk() #Create Window
    root.title("Tic Tac Toe") #Title
    screen_width, screen_height = root.winfo_screenwidth(), root.winfo_screenheight()
    root.geometry('%dx%d+%d+%d' % (700, 700, (screen_width/2) - (700/2), (screen_height/2) - (700/2))) #700 x 700 sized screen (Centered)
    root.resizable(True,True) #Resizeable window
    root.minsize(400,400) #Minimum window size
    root.configure(background='#E6E6FA')

    #Relative weights (Equal in this case) for each row and column
    #Weight is scale for distributing space (default is 0 meaning don't grow if extra space)
    Grid.rowconfigure(root,0,weight = 1)
    Grid.rowconfigure(root,1,weight = 1)
    Grid.rowconfigure(root,2,weight = 1)
    Grid.columnconfigure(root,0,weight = 1)
    Grid.columnconfigure(root,1,weight = 1)
    Grid.columnconfigure(root,2,weight = 1)

    create_buttons(root)

    root.mainloop() #Display Window

if __name__ == "__main__":
    create_gui()