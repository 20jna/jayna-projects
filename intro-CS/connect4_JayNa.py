#connect4_JayNa.py
#Jay Na
#CS111 Spring 2018
#This file creates a version of the game Connect4, where the user plays against an AI

from graphics import *
import random

class ConnectWindow:

	def __init__(self):
		self.window = GraphWin("Connect Four", 690, 590)
		self.window.setMouseHandler(self.handleClick)
		self.startScreen()
		self.currentUser = 1
		self.limitCounter = 0
		

	def startScreen(self):
		'''This function creates the board and intializes the board count for each column'''

	#draws blue rectangle as the background
		self.background = Rectangle(Point(0,0), Point(690,590))
		self.background.setFill('blue')
		self.background.draw(self.window)
		
	#draws white circles to represent the spots for the game	
		for i in range(7):
			for j in range(6):
				self.Circles = Circle(Point(i*100+50,j*100+50),(30))
				self.Circles.setFill('white')
				self.Circles.draw(self.window)
				
	#draws lines to separate circles in rectangle
		for i in range(6):
			self.horizLine = Line(Point(0,i*100+100), Point(900,i*100+100))
			self.vertLine = Line(Point(100*i+100,0), Point(100*i+100,900))
			self.horizLine.draw(self.window)
			self.vertLine.draw(self.window)
			
	#initiates counts for each column and creates grid
		self.grid = [[],[],[],[],[],[],[]]
		self.boardCount = [0,0,0,0,0,0,0]
		counter = 2
		
		#help from CS Major, Joh Farmer
		for x in range(7):
			for y in range(6):
				self.grid[x].append(counter)
				counter += 1
				

	def validClick(self, x):
		'''This function checks if there is enough space vertically for move to be valid'''
		
		if self.boardCount[x] >= 6:
			print("Invalid Move")
			return False
		else:
			return True


	def drawUmove(self):
		'''This function prints the pieces onto the board at the given position from the user'''
		
		piece = Circle(Point(self.x*100+50, 600-(self.y*100+50)),30)
		piece.setFill('red')
		piece.draw(self.window)
		return

	def handleClick(self, point):
		'''This function works with the user to add each move into the board count and to the current grid'''

		self.newX = point.getX()
		self.x = self.newX//100
		self.y = self.boardCount[self.x]
		
		if self.validClick(self.x):
			self.boardCount[self.x] += 1
			self.limitCounter += 1
			self.grid[self.x][self.y] = self.currentUser
			
		if self.isWon() == False:
			self.limitCounter += 1
			self.computerMove()
			self.drawUmove()


	def isWon(self):
		'''This function checks if there is a winner in the game (True/False) and calls printWinner function'''

	#checks to see if there is a winner vertically
		for i in range(7):
			for j in range(3):
				self.square1 = self.grid[i][j]
				self.square2 = self.grid[i][j+1]
				self.square3 = self.grid[i][j+2]
				self.square4 = self.grid[i][j+3]
				if self.square1 == self.square2 and self.square2 == self.square3 and self.square3 == self.square4:
					self.printWinner(self.square1)
					return True

	#checks to see if there is a winner diagonally from lower left to upper right
		for i in range(4):
			for j in range(3):
				self.square1 = self.grid[i][j]
				self.square2 = self.grid[i+1][j+1]
				self.square3 = self.grid[i+2][j+2]
				self.square4 = self.grid[i+3][j+3]
				if self.square1 == self.square2 and self.square2 == self.square3 and self.square3 == self.square4:
					self.printWinner(self.square1)
					return True
					
	#checks to see if there is a winner diagonally from upper left to lower right
		for i in range(3,7):
			for j in range(3):
				self.square1 = self.grid[i][j]
				self.square2 = self.grid[i-1][j+1]
				self.square3 = self.grid[i-2][j+2]
				self.square4 = self.grid[i-3][j+3]
				if self.square1 == self.square2 and self.square2 == self.square3 and self.square3 == self.square4:
					self.printWinner(self.square1)
					return True			
					
	#checks to see if there is a winner horizontally
		for i in range(4):
			for j in range(6):
				self.square1 = self.grid[i][j]
				self.square2 = self.grid[i+1][j]
				self.square3 = self.grid[i+2][j]
				self.square4 = self.grid[i+3][j]
				if self.square1 == self.square2 and self.square2 == self.square3 and self.square3 == self.square4: 
					self.printWinner(self.square1)
					return True				
					
	#checks if board is full without a winner (tie)
		if self.limitCounter == 42:
			self.printWinner(3)
			return True
		return False


	def printWinner(self, winner):
		'''This function prints who the winner is or if it is a tie'''
		
	#if input is 3 from isWon() fxn, game is tied and so "Tie Game!" is printed 
		if winner == 3:
			txt = Text(Point(345, 300), "Tie Game!")
			txt.setFill('white')
			txt.setSize(35)
			txt.draw(self.window)
			return		
		else:
	#prints "You Won!" if user wins
			if winner == 1:
				txt = Text(Point(345, 300), "You Won!")
				txt.setFill('white')
				txt.setSize(35)
				txt.draw(self.window)
				return
			else:
	#prints "Computer Won!" if computer wins
				txt = Text(Point(345, 300), "Computer Won!")
				txt.setFill('white')
				txt.setSize(35)
				txt.draw(self.window)
				return


	def validCmove(self, x, y):
		'''This function checks if the computer's move will be valid'''
	
	#checks if 	'''if it tries to place it higher than the highest piece'''
		if self.boardCount[x] > y:
			return False
		''' if it tries to place below the highest piece'''
		if self.boardCount[x] < y:
			return False
		'''if it tries to place it in a column with 6 pieces already'''
		if self.boardCount[x] >= 6:
			return False
		else:
			return True
	

	def drawCmove(self, x ,y):
		'''This function adds the computer's move to the game board and adds it to the board count'''

		piece = Circle(Point((x)*100+50, 600 - ((y)*100+50)),30)
		piece.setFill('yellow')
		piece.draw(self.window)
		self.boardCount[x] += 1
		self.grid[x][y] = -1
		return


	def computerMove(self):
		'''This function computes where the computer will put its next move and calls the drawCmove() fxn to do so.
		The computer will add its piece to wherever there are three in a row in either color then looks to see when 
		there are two in a row. Move will be placed randomly if no pieces are placed in a row'''

	#checks if there are three pieces lined up vertically in a row and places its move to win or prevent the win'''
		for i in range(7):
			for j in range(3):
				self.square1 = self.grid[i][j]
				self.square2 = self.grid[i][j+1]
				self.square3 = self.grid[i][j+2]
				if self.square1 == self.square2 and self.square2 == self.square3:
					if self.validCmove(i,j+3):
						self.drawCmove(i,j+3)
						return
					else:
						self.randomMove()
						return
								
	#checks if there are three pieces lined up diagonally from lower left to upper right and places its move to win or prevent the win
	#help from CS major, Joh Farmer
		for i in range(4):
			for j in range(3):
				self.square1 = self.grid[i][j]
				self.square2 = self.grid[i+1][j+1]
				self.square3 = self.grid[i+2][j+2]
				if self.square1 == self.square2 and self.square2 == self.square3:
					if self.validCmove(i+3,j+3):
						self.drawCmove(i+3,j+3)
						return
					if self.validCmove(i-1,j-1):
						self.drawCmove(i-1,j-1)

					else:
						self.randomMove()
						return
						
	#checks if there are three pieces lined up diagonally from lower right to upper left and places its move to win or prevent the win		
		for i in range(3,7):
			for j in range(3):
				self.square1 = self.grid[i][j]
				self.square2 = self.grid[i-1][j+1]
				self.square3 = self.grid[i-2][j+2]
				if self.square1 == self.square2 and self.square2 == self.square3:
					if self.validCmove(i-3,j+3):
						self.drawCmove(i-3,j+3)
						return
					if self.validCmove(i+1,j-1):
						self.drawCmove(i+1,j-1)
					else:
						self.randomMove()
						return
						
	#checks if there are three pieces lined up horizontally in a row and places its move to win or prevent the win (either side)'''
		for i in range(4):
			for j in range(6):
				self.square1 = self.grid[i][j]
				self.square2 = self.grid[i+1][j]
				self.square3 = self.grid[i+2][j]
				if self.square1 == self.square2 and self.square2 == self.square3:
					if self.validCmove(i+3,j):
						self.drawCmove(i+3,j)
						return
					if self.validCmove(i-1,j):
						self.drawCmove(i-1,j)
						return
					else:
						self.randomMove()
						return



	#checks if there are two in a row diagonally from lower left to upper right and places its move accordingly
		for i in range(4):
			for j in range(3):
				self.square1 = self.grid[i][j]
				self.square2 = self.grid[i+1][j+1]
				if self.square1 == self.square2:
					if self.validCmove(i+2,j+2):
						self.drawCmove(i+2,j+2)
						return
					if self.validCmove(i-1,j-1):
						self.drawCmove(i-1,j-1)
					else:
						self.randomMove()
						return
						
	#checks if there are two in a row vertically and places its move accordingly
		for i in range(7):
			for j in range(3):
				self.square1 = self.grid[i][j]
				self.square2 = self.grid[i][j+1]
				if self.square1 == self.square2:
					if self.validCmove(i,j+2):
						self.drawCmove(i,j+2)
						return
					if self.validCmove(i,j-1):
						self.drawCmove(i,j-1)
						return
					else:
						self.randomMove()
						return					
						
	#checks if there are two in a row diagonally from lower right to upper left and places its move accordingly	
		for i in range(3,7):
			for j in range(3):
				self.square1 = self.grid[i][j]
				self.square2 = self.grid[i-1][j+1]
				if self.square1 == self.square2:
					if self.validCmove(i-2,j+2):
						self.drawCmove(i-2,j+2)
						return
					if self.validCmove(i+1,j-1):
						self.drawCmove(i+1,j-1)
					else:
						self.randomMove()
						return
					
	#checks if there are two in a row horizontally and places its move accordingly
		for i in range(4):
			for j in range(6):
				self.square1 = self.grid[i][j]
				self.square2 = self.grid[i+1][j]
				if self.square1 == self.square2:
					if self.validCmove(i+2,j):
						self.drawCmove(i+2,j)
						return
					if self.validCmove(i-1,j):
						self.drawCmove(i-1,j)
						return
					else:
						self.randomMove()
						return

	#places move randomly if no pieces are being placed in a row
		else:
			self.randomMove()


	def randomMove(self):
		'''This function creates a random coordinate for its move, checks if it's valid, then prints the move.
		It will continue to run until numbers are valid for current board'''
	
		randY = random.randint(0,6)
		randX = random.randint(0,7)
		
		if self.validCmove(randY,randX):
			self.drawCmove(randY,randX)
			return
		else:
			self.randomMove()


def main():
	gameOver = False
	connect4 = ConnectWindow()
	while gameOver == False:
		connect4.window.getMouse()
		gameOver = connect4.isWon()
	input("Hit enter to quit")

	
main()







