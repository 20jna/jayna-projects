Description:
My final project is a version of the popular board game, Connect4. In this program, a user
plays against an AI, which tries its best to block any four-of-a-kind moves made by the user
and looks to get four-of-a-kind for itself. This program uses graphics.py to draw the board
and the moves made. It checks to make sure that the moves being made by the user and computer
are valid according to the board and prints the winner in the end, or a tie if it is the case.

Justification of Construction:
Each function is entailed in one class, the ConnectWindow class. The window is first initiated,
using graphics.py to draw a blue rectangle and white circles to visualize the board. The grid
keeps track of the number of moves being made and the number of pieces in each column. The program
uses setMouseHandler() to input the user's moves on the board and checks to see if they are valid
depending on what is already on the board, making sure it stays within the limits of the grid. The computer
adds its piece to where there is three in a row diagonally, horizontally, or vertically, then looks
to put it where there is two in a row. If neither occur, the computer places its piece randomly
on the board using the random module in Python. These actions continue until there is either a 
winner or it is a tie. 

Current Status:
The program runs well when the user puts three in a row and tries to put the forth. The only
setback of this program is that when the user puts two pieces in a row and sets it up where the
fourth piece to win is between those two and one that is a space away, the computer doesn't always
catch that empty spot. This problem is only for when the pieces are aligned horizontally or diagonally, 
not vertically since then it would be impossible to skip a space. The game also doesn't show the last 
move made to win the game, if the user wins, but instead goes right to the print statement of who one.

Instructions:
Once the program is ran, the game is pretty simple. First, you, the user, click anywhere on
the board where you would want your piece to be. The pieces will stack up, as the computer and
you switch off each turn, putting another piece into the board. The goal is to have four
of your pieces align either horizontally, vertically, or diagonally.