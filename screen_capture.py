# Simple capture image and convert to gif tool

from PIL import Image, ImageSequence
import os, sys, subprocess
# from images2gif import writeGif

# os.system("screencapture my_screen.png")
# image = Image.open("my_screen.png")
# new_image = image.crop((200,200,400,400))
# new_image.show()



"""Takes a screenshot of the entire screen"""
def capture_screen():
    os.system("screencapture my_screen.png")
    return Image.open("my_screen.png")


"""Takes a 512x256 screenshot centered at x,y. 
    Returns the screenshot Image"""
def screen_shot(name, x, y):
    os.system("screencapture my_screen.png")
    full_screen = Image.open("my_screen.png")
    cropped = crop_image(full_screen, x ,y)
    cropped.save(name + ".png")
    os.system("rm my_screen.png")
    return cropped


"""Crops the given image, centered at x, y. The cropped image is 512x256"""
def crop_image(image, x, y):
    left = x - 256
    up = y - 128
    right = x + 256
    down = y + 128
    return image.crop((left, up, right, down))

"""Returns a tuple of the coordinates of the mouse in the form (x,y)"""
def get_mouse_coords():
    location = subprocess.check_output(['./MouseTools', '-location'])
    firstNewline = location.find('\n')
    secondNewLine = location.find('\n', firstNewline + 1)
    x = int(location[:firstNewline])
    y = int(location[firstNewline+1:secondNewLine])
    return x,y


#for testing
def main():
    screen = capture_screen()
    image_list = across_screen(screen, [])
    # writeGif("my_gif.GIF", image_list, duration = 0.5)

    sc = 0
    while sc < 10:
        image_list[sc].save("img" + str(sc) + ".png")
        sc += 1

if __name__ == '__main__':
    main()

