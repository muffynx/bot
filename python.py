import pyautogui as pg
import time

def click_image(image_path):
    while True:
        image_location = pg.locateOnScreen(image_path)
        if image_location is not None:
            print("I can see it")
            # image_center = pg.center(image_location)
            # pg.click(image_center)
            break
        else:
            print("I am unable to see it")

# First image
click_image('./image/1keep.png')
