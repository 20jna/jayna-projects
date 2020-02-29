# greenscreen.py
# Jay Na and Gabe Nass
# This program runs a function called replaceWall that alters the image amy.gif, replacing
# the wall pixels of the image with a different image

import cImage

def replaceWall(originalImage, replacementImage):
	height = originalImage.getHeight()
	width = originalImage.getWidth()
	newImage = cImage.EmptyImage(width, height)
	
	for row in range(height):
		for col in range(width):
			pixel = originalImage.getPixel(col, row)
			r = pixel.getRed()
			g = pixel.getGreen()
			b = pixel.getBlue()
			if r >= 100 and g >= 100 and abs(r - g) < 30 and abs(r - b) < 30 and abs(g - b) < 30:
				newImage.setPixel(row, col, cImage.replacementImage)
	
	return newImage


def main():
    originalImage = 'images/amy.gif'
    replacementImage = 'images/background2.gif'
    replaceWall(originalImage, replacementImage)

if __name__ == '__main__':
    main()