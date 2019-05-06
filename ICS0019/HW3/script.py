"""
task

Make Python3 program to tint photos like flag overlay.
You may use Estonian flag or flag of some other (your own) country. Stripes may be horisontal or vertical, minimum 3 stripe.
Program must work with different size of .jpg or .png photos (your own choice).

From: Hannes Toots

NB: This script uses a Library called "Pillow" (pip install Pillow)
NB2: New image gets saved as a png because JPEGs do not represent an alpha
channel and we need it.
"""

from PIL import Image

def openImage(image):
    """
    Function to open specified image file

    :param image: Image file name
    :return: Image.open(image) as RGBA
    """
    return Image.open(image).convert("RGBA")

def resizeImage(image, size):
    """
    Function to resize image to specified size

    :param image: Opened image
    :param size: size tuple
    :return: image.resize(size) with resampling of ANTIALIAS
    """
    return image.resize(size, Image.ANTIALIAS)

def addOverlay(bg, fg, transparency):
    """
    Function to add fg ontop of bg

    :param bg: Background image
    :param fg: Foreground image
    :param transparency: Transparency value for fg image
    :return: new Image blended together from bg and fg
    """

    return Image.blend(bg, fg, transparency)

def saveImage(image, name):
    """
    Function to save image

    :param image: Image to save
    :param name: Name to save as
    :return:
    """
    print("Saving image as {}".format(name))
    image.save(name)

def main():
    # Open images
    bg = openImage('background.jpg')
    fg = openImage('foreground.jpg')

    # Resize foreground(flag) to background(profile picture)
    fg = resizeImage(fg, bg.size)

    # Add foreground to background with transparency of 50%
    new = addOverlay(bg, fg, .5)

    # Show and save image
    new.show()
    saveImage(new, 'test.png')

if __name__ == '__main__':
    main()
