import graphics as gs
import time
#from graphics import *

window = gs.GraphWin()
myCircle = gs.Circle(gs.Point(50,100),50)
#myCircle = Circle(Point(10,20),5)

myCircle.setFill("blue")
myCircle.draw(window)

myCircle2 = myCircle.clone()
#need this to make two circles
myCircle2.setFill("red")
myCircle2.draw(window)

for i in range(100):
	time.sleep(.1)
	#speed of the movement
	myCircle2.move(1,1)


#myCircle2.move(100,100)




input("enter to quit")
