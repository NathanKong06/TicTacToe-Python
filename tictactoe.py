import tkinter as tk
from tkinter import *

board = [[0,0,0],[0,0,0],[0,0,0],[0,0,0]] #Create 4 by 4 Board for board and reset button
buttons = [[0,0,0],[0,0,0],[0,0,0],[0,0,0]] #Create corresponding buttons for each box

def draw(root,i,j):
    global buttons
    if i == 0 and j == 0:
        buttons[0][0] = Button(root, text = 'X', height = 5, width = 10, relief = SOLID, borderwidth = 0.5, command = lambda:draw(root,0,0))
        buttons[0][0].grid(row = 0, column = 0, sticky = "nsew", padx = (20,0), pady = (20,0))
    elif i == 0 and j == 1:
        buttons[0][1] = Button(root, text = 'X', height = 5, width = 10, relief = SOLID, borderwidth = 0.5, command = lambda:draw(root,0,1))
        buttons[0][1].grid(row = 0, column = 1, sticky = "nsew", pady = (20,0))
    elif i == 0 and j == 2:
        buttons[0][2] = Button(root, text = 'X', height = 5, width = 10, relief = SOLID, borderwidth = 0.5, command = lambda:draw(root,0,2))
        buttons[0][2].grid(row = 0, column = 2, sticky = "nsew", padx = (0,20), pady = (20,0))
    elif i == 1 and j == 0:
        buttons[1][0] = Button(root, text = 'X', height = 5, width = 10, relief = SOLID, borderwidth = 0.5, command = lambda:draw(root,1,0))
        buttons[1][0].grid(row = 1, column = 0, sticky = "nsew", padx = (20,0))
    elif i == 1 and j == 1:
        buttons[1][1] = Button(root, text = 'X', height = 5, width = 10, relief = SOLID, borderwidth = 0.5, command = lambda:draw(root,1,1))
        buttons[1][1].grid(row = 1, column = 1, sticky = "nsew")
    elif i == 1 and j == 2:
        buttons[1][2] = Button(root, text = 'X', height = 5, width = 10, relief = SOLID, borderwidth = 0.5, command = lambda:draw(root,1,2))
        buttons[1][2].grid(row = 1, column = 2, sticky = "nsew", padx = (0,20))
    elif i == 2 and j == 0:
        buttons[2][0] = Button(root, text = 'X', height = 5, width = 10, relief = SOLID, borderwidth = 0.5, command = lambda:draw(root,2,0))
        buttons[2][0].grid(row = 2, column = 0, sticky = "nsew", padx = (20,0))
    elif i == 2 and j == 1:
        buttons[2][1] = Button(root, text = 'X', height = 5, width = 10, relief = SOLID, borderwidth = 0.5, command = lambda:draw(root,2,1))
        buttons[2][1].grid(row = 2, column = 1, sticky = "nsew")
    elif i == 2 and j == 2:
        buttons[2][2] = Button(root, text = 'X', height = 5, width = 10, relief = SOLID, borderwidth = 0.5, command = lambda:draw(root,2,2))
        buttons[2][2].grid(row = 2, column = 2, sticky = "nsew", padx = (0,20))

def create_button_paddings(root):
    global buttons

    buttons[0][0] = Button(root, text = '', height = 5, width = 10, relief = SOLID, borderwidth = 0.5, command = lambda:draw(root,0,0))
    buttons[0][0].grid(row = 0, column = 0, sticky = "nsew", padx = (20,0), pady = (20,0))

    buttons[0][1] = Button(root, text = '', height = 5, width = 10, relief = SOLID, borderwidth = 0.5, command = lambda:draw(root,0,1))
    buttons[0][1].grid(row = 0, column = 1, sticky = "nsew", pady = (20,0))

    buttons[0][2] = Button(root, text = '', height = 5, width = 10, relief = SOLID, borderwidth = 0.5, command = lambda:draw(root,0,2))
    buttons[0][2].grid(row = 0, column = 2, sticky = "nsew", padx = (0,20), pady = (20,0))

    buttons[1][0] = Button(root, text = '', height = 5, width = 10, relief = SOLID, borderwidth = 0.5, command = lambda:draw(root,1,0))
    buttons[1][0].grid(row = 1, column = 0, sticky = "nsew", padx = (20,0))

    buttons[1][1] = Button(root, text = '', height = 5, width = 10, relief = SOLID, borderwidth = 0.5, command = lambda:draw(root,1,1))
    buttons[1][1].grid(row = 1, column = 1, sticky = "nsew")

    buttons[1][2] = Button(root, text = '', height = 5, width = 10, relief = SOLID, borderwidth = 0.5, command = lambda:draw(root,1,2))
    buttons[1][2].grid(row = 1, column = 2, sticky = "nsew", padx = (0,20))

    buttons[2][0] = Button(root, text = '', height = 5, width = 10, relief = SOLID, borderwidth = 0.5, command = lambda:draw(root,2,0))
    buttons[2][0].grid(row = 2, column = 0, sticky = "nsew", padx = (20,0))

    buttons[2][1] = Button(root, text = '', height = 5, width = 10, relief = SOLID, borderwidth = 0.5, command = lambda:draw(root,2,1))
    buttons[2][1].grid(row = 2, column = 1, sticky = "nsew")

    buttons[2][2] = Button(root, text = '', height = 5, width = 10, relief = SOLID, borderwidth = 0.5, command = lambda:draw(root,2,2))
    buttons[2][2].grid(row = 2, column = 2, sticky = "nsew", padx = (0,20))
    #Paddings to top, right, and left sides

    buttons[3][2] = Button(root, text = 'Reset', height = 3, width = 10, relief = SOLID, borderwidth=0.5, command = lambda:reset_board(root))
    buttons[3][2].grid(row = 3, column = 2, sticky = "ew", pady = 20, padx = (0,10))
    #Reset button

def reset_board(root):
    global board 
    global buttons
    board = [[0,0,0],[0,0,0],[0,0,0],[0,0,0]]
    buttons = [[0,0,0],[0,0,0],[0,0,0],[0,0,0]]
    create_button_paddings(root)

def create_gui():
    root = tk.Tk() #Create Window
    root.title("Tic Tac Toe") #Title
    root.geometry("700x700") #Default Window Size
    root.resizable(True,True) #Resizeable window
    root.minsize(300,300) #Minimum window size

    #Relative weights (Equal in this case) for each row and column
    #Weight is scale for distributing space (default is 0 meaning don't grow if extra space)
    Grid.rowconfigure(root,0,weight = 1)
    Grid.rowconfigure(root,1,weight = 1)
    Grid.rowconfigure(root,2,weight = 1)
    Grid.columnconfigure(root,0,weight = 1)
    Grid.columnconfigure(root,1,weight = 1)
    Grid.columnconfigure(root,2,weight = 1)

    create_button_paddings(root)

    root.mainloop() #Display Window

if __name__ == "__main__":
    create_gui()