# Simple capture image and convert to gif tool

from PIL import Image, ImageSequence
import os, sys
from images2gif import writeGif

# os.system("screencapture my_screen.png")
# image = Image.open("my_screen.png")
# new_image = image.crop((200,200,400,400))
# new_image.show()

def capture_screen():
    os.system("screencapture my_screen.png")
    return Image.open("my_screen.png")

def crop_screen(screen, left, up, right, bottom):
    return screen.crop((left, up, right, bottom))

def across_screen(screen, image_list):
    i = 0
    while i < 10:
        image_list.append(crop_screen(screen, i * 50, 0, 200 + i * 50, 200))
        i += 1
    return image_list

def main():
    screen = capture_screen()
    image_list = across_screen(screen, [])
    writeGif("my_gif.GIF", image_list, duration = 0.5)

    # sc = 0
    # while sc < 10:
    #     image_list[sc].save("img" + str(sc) + ".png")
    #     sc += 1

if __name__ == '__main__':
    main()

