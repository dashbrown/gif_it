# Simple capture image and convert to gif tool

from PIL import Image, ImageSequence
import os, sys, subprocess, time
# from images2gif import writeGif

"""Takes a screenshot of the entire screen"""
def capture_screen(n):
    os.system("screencapture my_screen" + str(n) + ".png")
    return Image.open("my_screen" + str(n) + ".png")


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


"""Take screenshots centered around the mouse cursor"""
def main():
    t0 = time.time()
    # screen_list = []
    # mouse_list = []
    i = 0
    while time.time() - t0 < 5:
        x, y = get_mouse_coords()
        screen_shot(str(i), x, y)
        i += 1

def two(s, l):
    t = time.time()
    while time.time() - 2 < t:
        l[0] += 1
    #print s,l[0]

def thread_two():
    import thread
    t = time.time()
    l1 = [0]
    l2 = [0]
    l3 = [0]
    l4 = [0]
    thread.start_new_thread(two, ("one",l1))
    thread.start_new_thread(two, ("two",l2))
    thread.start_new_thread(two, ("three",l3))
    thread.start_new_thread(two, ("four",l4))
    while time.time() - t < 3:
        pass
    print l1[0] + l2[0] + l3[0] + l4[0]
    




if __name__ == '__main__':
    main()
    # thread_two()

