# Eric Alexander
# CS 111: Spring 2018
# A classy (haha!) version of our TicTacToe game.

import random

# This class acts as a board for our TicTacToe game.
class TTTBoard:
    # Constructor takes no arguments
    def __init__(self):
        self.board = [['-','-','-'],
                      ['-','-','-'],
                      ['-','-','-']]

# Attempts to place <mark> at position (r,c)
# Returns True if successful, False if move was illegal    
    
    def move(self, r, c, mark): 
    	if self.isLegalMove() == True:
    		self.board[r][c] == self.mark
    		return True
    	else:
    		return False
    		    
        '''##Check if legal
        if false return false
        else mark board
        return true
        '''
 
# Checks to see if (r,c) is a legal move given the current state of the board
    
    def isLegalMove(self, r, c):
    	if r >= 0 and r <= 2 and c >=0 and r >= 2:
        	if self.board[r][c] == '-':
            	return True
        	else:
            	return False
        else:
        	return False

# Checks to see who has won (if anyone)
# Returns 'X', 'O', 'Draw', or '' if no one has won yet

	def getWinner(self, board):
#defining the middle space on the tic-tac-toe board
    	middle = board[1][1]
    	winner = ''
#looping through each list in board  
    	for i in range(3):
#checking for winner with three in a row as a row on the board
        	if self.board[i][0] == self.board[i][1] and self.board[i][0] == self.board[i][2]:
            	winner = self.board[i][0]
            	return winner
#checking for winner with three in a row as a column on the board                     
        	elif self.board[0][i] == self.board[1][i] and self.board[0][i] == self.board[2][i]:
            	winner = self.board[0][i]
            	return winner
#checking for winner with three in a row diagonally (top left to bottom right)      
        	elif self.board[0][0] == middle and middle == self.board[2][2]:
            	winner = self.board[0][0]
            	return winner
#checking for winner with three in a row diagonally (top right to bottom left)       
        	elif self.board[2][0] == middle and middle == self.board[0][2]:
            	winner = self.board[2][0]
            	return winner
        
        	else:
#checking for empty spaces to see if no one has won yet        
            	for j in range(3):
                	if self.board[i][j] == '-':
                    	winner = ''
                    	return winner
#returns draw when all spaces are filled and there is no winner                    
            	winner = 'Draw'
    	return winner

# Draws board in its current state
	def drawBoard(self):
        for row in self.board:
            for spot in row:
                print(spot, end='')
            print()
        print()
'''
class TTTNovice:
    def __init__(self, mark, board):
        self.mark = mark
        self.board = board
    def play(self):
        r = random.randint(0, 2)
        c = random.randint(0, 2)
'''    
class TTTUser:
    
    def __init__(self, mark, board):
        userMark = self.mark
        board = self.board   
    
    def play(self):
    	validMove = False
    	while validMove == False:     	
			r = int(input('Row: (0-2) '))
        	c = int(input('Col: (0-2) '))
    		validMove = self.board.move(r, c, self.mark)
    	return self.board
      
# Get user's choice for who goes first and initiate vars
def getMarks():
    while True:
        userChoice = input('Would you like to be X or O? ')
        if userChoice not in ['X','x','O','o']:
            print('Invalid choice.')
        else:
            if userChoice == 'X' or userChoice == 'x':
                return 'X','O'
            else:
                return 'O','X'
    
# Tell the user how the game ended
def printEndGame(winner, userMark):
    if winner != 'Draw':
        print('{} wins!'.format(winner))
        if winner == userMark:
            print('Congratulations!')
        else:
            print('Better luck next time!')
    else:
        print('The game has ended in a draw.')
    
# Main function contains the actual turn-taking functionality
def main():
    while True:
        userMark, compMark = getMarks()
        
        # Instantiate board and players and draw empty board
        board = TTTBoard()
        # board = GraphicalBoard()
        print(userMark)
        print(compMark)
        userPlayer = TTTUser(userMark, board)
        compPlayer = TTTNovice(compMark, board)
        board.drawBoard()
        
        # If user is X, don't let computer go first
        if userMark == 'X':
            compGoes = False
        else:
            compGoes = True
            
        # Alternate between AI's turn and user's turn until game is over
        winner = board.getWinner()
        while winner == '':
            if compGoes:
                compPlayer.play()
            else:
                compGoes = True
            
            # If computer didn't win, user gets to go
            winner = board.getWinner()
            if winner == '':
                userPlayer.play()
                winner = board.getWinner()
        
        printEndGame(winner, userMark)
        
        # See if user wants to play again
        playAgain = input('Would you like to play again? (Y/N) ')
        if playAgain[0].lower() != 'y':
            if playAgain[0].lower() != 'n':
                print('Unrecognized input. Exiting game.')
            print('Thanks for playing!')
            break

if __name__ == '__main__':
    main()