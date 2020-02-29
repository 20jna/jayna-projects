# photoLab.py
# Jay Na and Gabe Nass
# A series of functions performing image processing
# Adapted from code by Eric Alexander.
# CS 111

import cImage

def test_filter(image_file, func_name):
    '''
    This function will display an original image next to its modified image.
    
    Parameters:
    image_file (string) - the name of a file containing an image.
    func_name (function) - the name of a function in this module that takes in
    an Image Object and returns a modified image object.
    
    Returns:
    None
    '''
    orig_image = cImage.FileImage(image_file)
    new_image = func_name(orig_image)
    win = cImage.ImageWin("Image Processing", orig_image.getWidth() * 2, orig_image.getHeight())
    
    orig_image.draw(win)
    new_image.setPosition(orig_image.getWidth()+ 1,0)
    new_image.draw(win)
    win.exitOnClick()
    
    
def mute(image):
    ''' Function that returns copy of given image with "muted" color intensity. '''
    height = image.getHeight()
    width = image.getWidth()
    newImage = cImage.EmptyImage(width, height)

    for row in range(height):
        for col in range(width):
            pixel = image.getPixel(col, row)
            r = pixel.getRed()
            g = pixel.getGreen()
            b = pixel.getBlue()
            newImage.setPixel(col, row, cImage.Pixel(r // 2, g // 2, b // 2))

    return newImage

def flip(image):
    ''' Function that returns copy of given image that has been vertically flipped. '''
    height = image.getHeight()
    width = image.getWidth()
    newImage = cImage.EmptyImage(width, height)

    for row in range(height):
        for col in range(width):
            pixel = image.getPixel(col, row)
            newImage.setPixel(col, height - row - 1, pixel)

    return newImage
    

def onlyRed(image):
	''' Function that returns copy of given image in only red'''
    height = image.getHeight()
    width = image.getWidth()
    newImage = cImage.EmptyImage(width, height)
    
    for row in range(height):
        for col in range(width):
            pixel = image.getPixel(col, row)
            r = pixel.getRed()
            g = pixel.getGreen()
            b = pixel.getBlue()
            newImage.setPixel(col, row, cImage.Pixel(r, 0, 0))
            
    return newImage
    
def colorBlind(image):
	''' Function that returns copy of given image as a red-green colorblind viewer'''
    height = image.getHeight()
    width = image.getWidth()
    newImage = cImage.EmptyImage(width, height)
    
    for row in range(height):
        for col in range(width):
            pixel = image.getPixel(col, row)
            r = (pixel.getRed() + pixel.getGreen()) // 2
            g = (pixel.getGreen() + r) // 2
            b = pixel.getBlue()
            newImage.setPixel(col, row, cImage.Pixel(r, g, b))
    
    return newImage
    
def negate(image):
	''' Function that returns copy of given image in negative form'''
	height = image.getHeight()
	width = image.getWidth()
	newImage = cImage.EmptyImage(width, height)
	
	for row in range(height):
		for col in range(width):
			pixel = image.getPixel(col, row)
			r = pixel.getRed()
			g = pixel.getGreen()
			b = pixel.getBlue()
			newImage.setPixel(col, row, cImage.Pixel(255 - r, 255 - g, 255 - b))
    
	return newImage
			
	

def main():
    imgFile = 'images/poskanzer.gif'
    test_filter(imgFile, mute)
    test_filter(imgFile, flip)
    test_filter(imgFile, onlyRed)
    test_filter(imgFile, colorBlind)
    test_filter(imgFile, negate)
       
if __name__ == '__main__':
    main()