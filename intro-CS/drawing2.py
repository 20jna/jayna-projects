import graphics as gs
import time

window = gs.GraphWin("Star Moves",500,500)
myOval = gs.Oval(gs.Point(50,300),gs.Point(20,400))
myOval.setFill(gs.color_rgb(200,100,100))
#can do any color
myOval.draw(window)
for i in range(100):
	myOval.move(10,2)
	
	
	
myRectangle = gs.Rectangle(gs.Point(100,10),gs.Point(60,50))
myRectangle.draw(window)

for i in range(20):
	myRectangle.move(5,5)
	

input("enter to quit")