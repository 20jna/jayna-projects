# Author: Kanin Bunajinda & Jay Na 
#Image Processing Project

from cImage import *
import sys 
def saturatedRGB(r,g,b,k):
    newRGB = []
    newRGB.append((.3+.7*k)*r + .6*(1-k)*g + .1*(1-k)*b)
    newRGB.append(.3*(1-k)*r + (.6+.4*k)*g + .1*(1-k)*b)
    newRGB.append(.3*(1-k)*r + .6*(1-k)*g + (.1+.9*k)*b)
    newRGB = [min(255, max(0,int(val))) for val in newRGB]
    return newRGB
#given equation to change saturation

def oneColor(origImage, color): 
	oneColor=origImage.copy()  
	numPix= oneColor.getNumPixels()
	if color == "r":
		for i in range(numPix):
			p=oneColor.getPixel1D(i)
			p.green= 0
			p.blue= 0
			oneColor.setPixel1D(i,p)
	elif color == "b":
		for i in range (numPix):
			p=oneColor.getPixel1D(i)
			p.green= 0
			p.red = 0
			oneColor.setPixel1D(i,p)
	else:
		for i in range (numPix):
			p=oneColor.getPixel1D(i)
			p.blue= 0
			p.red= 0
			oneColor.setPixel1D(i,p)		
	return oneColor
#function to change image to have only one color. If statements depending on what color
#user inputs. 

def negate(origImage):
	negIm=origImage.copy()
	numPix=origImage.getNumPixels()
	for i in range(numPix):
		p=negIm.getPixel1D(i)
		p.red= 255- p.red
		p.green=255- p.green
		p.blue=255- p.blue
		negIm.setPixel1D(i,p)
	return negIm
#function to create negate image. Does so by reverting color to it's opposite end

def saturated(origImage, k):
	sat=origImage.copy()
	numPix=sat.getNumPixels()
	for i in range(numPix):
		p=sat.getPixel1D(i)
		set=saturatedRGB(p.red, p.green, p.blue, k)
		p.red=set[0]
		p.green=set[1]
		p.blue=set[2]
		sat.setPixel1D(i,p)
	return sat
#function to create saturated image. Does so by doing a loop and changing the color of each
#pixel by the value given back from the saturationRGB equation. 

def main():
    origImage = FileImage(sys.argv[1])
    win = ImageWin("image processing",origImage.getWidth()*2,origImage.getHeight()*2)
    origImage.draw(win)

    colorIm = oneColor(origImage, sys.argv[2])
    colorIm.setPosition(origImage.getWidth()+1,0)
    colorIm.draw(win)
    
    negateIm= negate(origImage)
    negateIm.setPosition(0, origImage.getHeight()+1)
    negateIm.draw(win)
    
    satIm= saturated(origImage,int(sys.argv[3]))
    satIm.setPosition(origImage.getWidth()+1, origImage.getHeight()+1)
    satIm.draw(win)
#positions and draw each image to fit a square
    
    input("enter to quit")

main()