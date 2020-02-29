# Noah's Quest for A Perfect Score
# You can do it my dude


# Basic Overview; Importing Graphics and time
import graphics as gs
import time
#Prompting the user for a time
UserTime = input("What time is it?: ")
UserTime = int(UserTime)
shift = input("Am or Pm? (Uppercase then Lowercase): ")




#24-Hour Time Cycle
if UserTime == -1:

    #Creating the Window
    window = gs.GraphWin('Project', 1000, 750)

    #Drawing shape (Sky variability)
    mysky = gs.Rectangle(gs.Point(0, 0), gs.Point(1000, 650))
    mysky.setFill(gs.color_rgb(color1,color1,color1))
    mysky.draw(window)

    #Drawing shape (grass)
    myrectangle2 = gs.Rectangle(gs.Point(0, 750), gs.Point(1000, 620))
    myrectangle2.setFill(gs.color_rgb(40,135,26))
    myrectangle2.draw(window)
    #Drawing Shape (Skateboard Wheel #1)
    mycircle = gs.Circle(gs.Point(400,600), 50)
    mycircle.setFill(gs.color_rgb(46,46,46))
    mycircle.draw(window)
    #Drawing shape (Skateboard Wheel #2)
    mycircle2 = gs.Circle(gs.Point(100,600), 50)
    mycircle2.setFill(gs.color_rgb(46,46,46))
    mycircle2.draw(window)
    #Drawing shape (Rim for wheel 1)
    mycircle3 = gs.Circle(gs.Point(400,600), 30)
    mycircle3.setFill('grey')
    mycircle3.draw(window)
    #Drawing shape (Rim for wheel 2)
    mycircle4 = gs.Circle(gs.Point(100,600), 30)
    mycircle4.setFill('grey')
    mycircle4.draw(window)
    #Drawing shape (Deck of Skateboard)
    myrectangle = gs.Rectangle(gs.Point(10, 550), gs.Point(510, 570))
    myrectangle.setFill(gs.color_rgb(172,24,44))
    myrectangle.draw(window)


    for i in range(250):
        time.sleep(0.005)
        #movement for wheels
        mycircle.move(2,0)
        mycircle2.move(2,0)
        #movement for rims
        mycircle3.move(2,0)
        mycircle4.move(2,0)
        #movement for Deck
        myrectangle.move(2,0)

    for i in range(500):
        time.sleep(0.005)
        #movement for wheels
        mycircle.move(-2,0)
        mycircle2.move(-2,0)
        #movement for rims
        mycircle3.move(-2,0)
        mycircle4.move(-2,0)
        #movement for Deck
        myrectangle.move(-2,0)




#Standard 1-12 Time Variables
else:
    #Edge Cases (Noon and Midnight)
    if UserTime == 12:
        UserTime = 0
        UserTime = int(0)

    #color differentiation (255/12 = 21.25)
    if shift == "Pm":
        color1 = (0 + (255-(21.25*(UserTime))))
        color1 = int(color1)
    elif shift == "Am":
        color1 = (0 + (21.25*(UserTime)))
        color1 = int(color1)
    else:
        print("Invalid input")
        closing = input("Program will now close. ")
        quit()

    #Creating the Window
    window = gs.GraphWin('Project', 1000, 750)
    #Drawing shape (Sky variability)
    mysky = gs.Rectangle(gs.Point(0, 0), gs.Point(1000, 650))
    mysky.setFill(gs.color_rgb(color1,color1,color1))
    mysky.draw(window)
    #Drawing shape (grass)
    myrectangle2 = gs.Rectangle(gs.Point(0, 750), gs.Point(1000, 620))
    myrectangle2.setFill(gs.color_rgb(40,135,26))
    myrectangle2.draw(window)
    #Drawing Shape (Skateboard Wheel #1)
    mycircle = gs.Circle(gs.Point(400,600), 50)
    mycircle.setFill(gs.color_rgb(46,46,46))
    mycircle.draw(window)
    #Drawing shape (Skateboard Wheel #2)
    mycircle2 = gs.Circle(gs.Point(100,600), 50)
    mycircle2.setFill(gs.color_rgb(46,46,46))
    mycircle2.draw(window)
    #Drawing shape (Rim for wheel 1)
    mycircle3 = gs.Circle(gs.Point(400,600), 30)
    mycircle3.setFill('grey')
    mycircle3.draw(window)
    #Drawing shape (Rim for wheel 2)
    mycircle4 = gs.Circle(gs.Point(100,600), 30)
    mycircle4.setFill('grey')
    mycircle4.draw(window)
    #Drawing shape (Deck of Skateboard)
    myrectangle = gs.Rectangle(gs.Point(10, 550), gs.Point(510, 570))
    myrectangle.setFill(gs.color_rgb(172,24,44))
    myrectangle.draw(window)


    for i in range(250):
        time.sleep(0.005)
        #movement for wheels
        mycircle.move(2,0)
        mycircle2.move(2,0)
        #movement for rims
        mycircle3.move(2,0)
        mycircle4.move(2,0)
        #movement for Deck
        myrectangle.move(2,0)

    for i in range(500):
        time.sleep(0.005)
        #movement for wheels
        mycircle.move(-2,0)
        mycircle2.move(-2,0)
        #movement for rims
        mycircle3.move(-2,0)
        mycircle4.move(-2,0)
        #movement for Deck
        myrectangle.move(-2,0)