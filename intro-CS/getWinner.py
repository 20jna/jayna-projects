# getWinner.py
# Jay Na and Gabe Nass
# CS111 Spring 2018
# Here we create a function that determines the winner of Tic-Tac-Toe

def getWinner(board):
#defining the middle space on the tic-tac-toe board
    middle = board[1][1]
    winner = ''

#looping through each list in board  
    for i in range(3):
#checking for winner with three in a row as a row on the board
        if board[i][0] == board[i][1] and board[i][0] == board[i][2]:
            winner = board[i][0]
            return winner
#checking for winner with three in a row as a column on the board                     
        elif board[0][i] == board[1][i] and board[0][i] == board[2][i]:
            winner = board[0][i]
            return winner
#checking for winner with three in a row diagonally (top left to bottom right)      
        elif board[0][0] == middle and middle == board[2][2]:
            winner = board[0][0]
            return winner
#checking for winner with three in a row diagonally (top right to bottom left)       
        elif board[2][0] == middle and middle == board[0][2]:
            winner = board[2][0]
            return winner
        
        else:
#checking for empty spaces to see if no one has won yet        
            for j in range(3):
                if board[i][j] == '-':
                    winner = ''
                    return winner
#returns draw when all spaces are filled and there is no winner                    
            winner = 'Draw'
    return winner
                      
    
if __name__ == '__main__':
   
    #horizontal win ('O')
    #board = [['X','O','X'],['O','O','O'],['X','X','O']]

    #vertical win ('X')
    #board = [['X','O','X'],['X','O','X'],['X','X','O']]
    
    #diagonal win ('X')
    #board = [['O','O','X'],['X','X','O'],['X','X','O']]
    
    #diagonal win ('O')
    #board = [['O','O','X'],['X','O','X'],['X','X','O']]
    
    #draw
    #board = [['X','O','X'],['X','O','X'],['O','X','O']]
    
    #not finished
    #board = [['O','-','X'],['X','X','O'],['O','X','O']]
    #board = [['O','O','X'],['X','O','X'],['X','X','-']]
    
    print(getWinner(board))
