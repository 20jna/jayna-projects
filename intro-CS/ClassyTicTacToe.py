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
        pass
        
    # Checks to see if (r,c) is a legal move given the current state of the board
    def isLegalMove(self, r, c):
        pass
        
    # Checks to see who has won (if anyone)
    # Returns 'X', 'O', 'Draw', or '' if no one has won yet
    def getWinner(self):
        pass
        
    # Draws board in its current state
    def drawBoard(self):
        for row in self.board:
            for spot in row:
                print(spot, end='')
            print()
        print()

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