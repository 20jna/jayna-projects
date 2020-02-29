# Author: Sherri Goings
# Simple example using cImage to filter a .gif to be in greyscale
# Also includes helper function to use in saturate filter

from cImage import *

def saturatedRGB(r,g,b,k):
    """ inputs the r,g,b values of a pixel and an intensity parameter k, returns
    a list with the 3 saturated values for r,g,b """
    newRGB = []
    
    # add new adjusted values for r, g, b, to list
    newRGB.append((.3+.7*k)*r + .6*(1-k)*g + .1*(1-k)*b)
    newRGB.append(.3*(1-k)*r + (.6+.4*k)*g + .1*(1-k)*b)
    newRGB.append(.3*(1-k)*r + .6*(1-k)*g + (.1+.9*k)*b)
    
    # convert each value in the list into an int in the range (0,255) before returns
    newRGB = [min(255, max(0,int(val))) for val in newRGB]
    return newRGB


def greyscale(imag):
    """ takes the original image as an argument, returns a twotone version
    without modifying the original image at all """
    greyIm = imag.copy()

    # loop through each pixel in the orig image, set the pixel in the new
    # greyscale image to have all r,g,b values be the average of the original
    # r,b,g values
    numPix = imag.getNumPixels()
    for i in range(numPix):
        p = imag.getPixel1D(i)
        aveCol = (p.red+p.green+p.blue)//3    # RGB color values must be ints
        p.red = aveCol
        p.green = aveCol
        p.blue = aveCol
        greyIm.setPixel1D(i, p)
    return greyIm

def lighten(origIm, amount):
	lightIm = origIm.copy()
	
	for x in range(orig.getWidth()):
		for y in range(origIm.getHeight()//2, origIm.getHeight()):
			p = origIm.getPixel(x,y)
			p.red = updateColor(p.red, amount)
			p.green = updateColor(p.blue, amount)
			lightIm.setPixel(x,y,p)
	returnlightIm
	
def vertLine(origIm, linewidth):
	for y range(origIm.getHeight()):
		p = im.getPixel(im.getWidth()//2, y)
		p.red = 0
		p.green = 0
		p.blue 255
		im.setPixel(im.getWidth()//2, y, p)
		return im	
	
def main():
    # open AA.gif and use its dimensions to make a suitably sized window
    origImage = FileImage("AA.gif")
    win = ImageWin("dogs! are great!",origImage.getWidth()*2,origImage.getHeight())
    origImage.draw(win)

    # draw the greyscale version of origImage to the right of origImage
    greyImage = greyscale(origImage)
    greyImage.setPosition(origImage.getWidth()+1,0)
    greyImage.draw(win)

    # ask for input so window stays open until user hits enter on terminal
    input("enter to quit")

main()
