import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
import copy

board = [[0,0,0],[0,0,0],[0,0,0],[0,0,0]] #Create 4 by 4 Board for board and reset button
buttons = [[0,0,0],[0,0,0],[0,0,0],[0,0,0]] #Create corresponding buttons for each box
current_player = 'X'
player_x_score = 0
player_y_score = 0

def reset_close_screen(root,screen):
    reset_board(root)
    screen.destroy()

def display_tie_screen(root):
    tie_screen = tk.Tk()
    tie_screen.title("Tie Screen")
    screen_width, screen_height = tie_screen.winfo_screenwidth(), tie_screen.winfo_screenheight()
    tie_screen.geometry('%dx%d+%d+%d' % (600, 600, (screen_width/2) - (600/2), (screen_height/2) - (600/2)))
    tie_screen.resizable(False,False) 

    background_photo = ImageTk.PhotoImage(master=tie_screen, image=Image.open("images/tie.png"))
    background_label = tk.Label(tie_screen, image=background_photo)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

    tie_label = tk.Label(tie_screen, text="It's a tie! \U0001F454", font=("Arial", 20, 'bold'), bg = "white")
    tie_label.place(relx=0.2, rely=0.5, anchor="center")
    close_button = tk.Button(tie_screen, text="Close", height = 2, width = 10, bg = "#C9E4FF", relief = SOLID, borderwidth=1, command=lambda: reset_close_screen(root, tie_screen))
    close_button.place(relx=0.8, rely=.5, anchor="center")

    tie_screen.mainloop()

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
    close_button = tk.Button(victory_screen, text="Close", height = 2, width = 10, bg = "#F08080", relief = SOLID, borderwidth=1, command=lambda: reset_close_screen(root, victory_screen))
    close_button.place(relx=0.5, rely=.95, anchor="s")

    victory_screen.mainloop()

def update_x_score():
    global player_x_score
    player_x_score = player_x_score + 1
    playerx_label.config(text="Player ✕: " + str(player_x_score))

def update_y_score():
    global player_y_score
    player_y_score = player_y_score + 1
    playery_label.config(text="Player 〇: " + str(player_y_score))

def check_win_or_draw(root):
    global board
    global player_x_score
    global player_y_score
    if board[0][0] == board[0][1] == board[0][2] and board[0][0] != 0:
        if (board[0][0] == 'X'):
            update_x_score()
        else:
            update_y_score()
        display_victory_screen(board[0][0],root)
        return True
    elif board[1][0] == board[1][1] == board[1][2] and board[1][0] != 0:
        if (board[1][0] == 'X'):
            update_x_score()
        else:
            update_y_score()
        display_victory_screen(board[1][0],root)
        return True
    elif board[2][0] == board[2][1] == board[2][2] and board[2][0] != 0:
        if (board[2][0] == 'X'):
            update_x_score()
        else:
            update_y_score()
        display_victory_screen(board[2][0],root)
        return True
    elif board[0][0] == board[1][0] == board[2][0] and board[0][0] != 0:
        if (board[0][0] == 'X'):
            update_x_score()
        else:
            update_y_score()
        display_victory_screen(board[0][0],root)
        return True
    elif board[0][1] == board[1][1] == board[2][1] and board[0][1] != 0:
        if (board[0][1] == 'X'):
            update_x_score()
        else:
            update_y_score()
        display_victory_screen(board[0][1],root)
        return True
    elif board[0][2] == board[1][2] == board[2][2] and board[0][2] != 0:
        if (board[0][2] == 'X'):
            update_x_score()
        else:
            update_y_score()
        display_victory_screen(board[0][2],root)
        return True
    elif board[0][0] == board[1][1] == board[2][2] and board[0][0] != 0:
        if (board[0][0] == 'X'):
            update_x_score()
        else:
            update_y_score()
        display_victory_screen(board[0][0],root)
        return True
    elif board[0][2] == board[1][1] == board[2][0] and board[0][2] != 0:
        if (board[0][2] == 'X'):
            update_x_score()
        else:
            update_y_score()
        display_victory_screen(board[0][2],root)
        return True
    elif 0 not in board[0] and 0 not in board[1] and 0 not in board[2]:
        display_tie_screen(root)
        return True
    return False

def minimax_check_win(curr_board):
    if curr_board[0][0] == curr_board[0][1] == curr_board[0][2] and curr_board[0][0] != 0:
        return curr_board[0][0]
    elif curr_board[1][0] == curr_board[1][1] == curr_board[1][2] and curr_board[1][0] != 0:
        return curr_board[1][0]
    elif curr_board[2][0] == curr_board[2][1] == curr_board[2][2] and curr_board[2][0] != 0:
        return curr_board[2][0]
    elif curr_board[0][0] == curr_board[1][0] == curr_board[2][0] and curr_board[0][0] != 0:
        return curr_board[0][0]
    elif curr_board[0][1] == curr_board[1][1] == curr_board[2][1] and curr_board[0][1] != 0:
        return curr_board[0][1]
    elif curr_board[0][2] == curr_board[1][2] == curr_board[2][2] and curr_board[0][2] != 0:
        return curr_board[0][2]
    elif curr_board[0][0] == curr_board[1][1] == curr_board[2][2] and curr_board[0][0] != 0:
        return curr_board[0][0]
    elif curr_board[0][2] == curr_board[1][1] == curr_board[2][0] and curr_board[0][2] != 0:
        return curr_board[0][2]
    elif 0 not in curr_board[0] and 0 not in curr_board[1] and 0 not in curr_board[2]:
        return "tie"

def minimax_score(curr_board,depth,is_maximizing):
    result = minimax_check_win(curr_board)
    if result == 'X':
        return 1
    elif result == 'O':
        return -1
    elif result == "tie":
        return 0
    if is_maximizing:
        best_score = -100 
        empty_spots = [(row, col) for row in range(3) for col in range(3) if curr_board[row][col] == 0]
        for spots in empty_spots: 
            curr_board[spots[0]][spots[1]] = "X" 
            copy_board = copy.deepcopy(curr_board)
            score = minimax_score(copy_board,depth+1,False) 
            curr_board[spots[0]][spots[1]] = 0 
            best_score = max(best_score,score)
        return best_score
    else:
        best_score = 100 
        empty_spots = [(row, col) for row in range(3) for col in range(3) if curr_board[row][col] == 0]
        for spots in empty_spots: 
            curr_board[spots[0]][spots[1]] = "O" 
            score = minimax_score(curr_board,depth+1,True) 
            curr_board[spots[0]][spots[1]] = 0 
            best_score = min(best_score,score)
        return best_score 

def minimax_move():
    global board
    global buttons
    best_score = 100 #Default low score
    empty_spots = [(row, col) for row in range(3) for col in range(3) if board[row][col] == 0]
    for spots in empty_spots: #For every empty spot
        board[spots[0]][spots[1]] = "O" #Try out the spot 
        copy_board = copy.deepcopy(board)
        score = minimax_score(copy_board,0,True) #Calculate the score with the spot tried out
        board[spots[0]][spots[1]] = 0 #Undo the change
        if score < best_score: #Set best score and best move
            best_score = score
            best_move = spots
    board[best_move[0]][best_move[1]] = "O" 
    buttons[best_move[0]][best_move[1]].configure(text = "〇", font = ("Arial",80))
    #Play the best move with the highest score

def draw(root,i,j):
    global buttons
    global current_player
    global board
    if buttons[i][j]['text'] == '':
        buttons[i][j].configure(text = "✕", font = ("Arial",80))
        board[i][j] = current_player
        if (not check_win_or_draw(root)):
            minimax_move()
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