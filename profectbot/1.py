import pyautogui as pg
import time

def click_image(image_path):
    while True:
        image_location = pg.locateOnScreen(image_path)
        if image_location is not None:

            image_center = pg.center(image_location)
            pg.click(image_center)
            break
        else:
            print("I am unable to see it")
def click_right(image_path):
    while True:
        image_location = pg.locateOnScreen(image_path)
        if image_location is not None:

            image_center = pg.center(image_location)
            pg.rightClick(image_center)
            break
        else:
            print("I am unable to see it")

def clickrightlift(image_path):
    while True:
        image_location = pg.locateOnScreen(image_path)
        if image_location is not None:

            image_center = pg.center(image_location)
            pg.click(image_center)
            time.sleep(0.1)
            pg.rightClick(image_center)

            break
        else:
            print("I am unable to see it")

# First image
# click_image('./image/1keep.png')
# click_image('./image/2.png')
# click_image('./image/3.png')
# click_image('./image/4.png')
# click_image('./image/5.png')
# click_image('./image/6.png')
# click_image('./image/7.png')
# click_image('./image/8.png')
# click_image('./image/9.png')
# click_image('./image/10.png')


def clientmanager(image_path):
    while True:
        image_location = pg.locateOnScreen(image_path)
        if image_location is not None:

            image_center = pg.center(image_location)
            pg.doubleClick(image_center)
            break
        else:
            print("I am unable to see it")

def typehost(image_path):

    while True:
        image_location = pg.locateOnScreen(image_path)
        if image_location is not None:
            
            image_center = pg.center(image_location)
            pg.click(image_center)
            pg.write("vpn.kku.ac.th")
      
            break
        else:
            print("I am unable to see it")

def typehub(image_path):

    while True:
        image_location = pg.locateOnScreen(image_path)
        if image_location is not None:
            
            image_center = pg.center(image_location)
            pg.click(image_center)
            pg.write("vpn")
      
            break
        else:
            print("I am unable to see it")
def typeusername(image_path):

    while True:
        image_location = pg.locateOnScreen(image_path)
        if image_location is not None:
            
            image_center = pg.center(image_location)
            pg.click(image_center)
            pg.write("6534500883")
      
            break
        else:
            print("I am unable to see it")
def typepassword(image_path):

    while True:
        image_location = pg.locateOnScreen(image_path)
        if image_location is not None:
            
            image_center = pg.center(image_location)
            pg.click(image_center)
            pg.write("Muffyn29300..")
      
            break
        else:
            print("I am unable to see it")
def typeenter(image_path):

    while True:
        image_location = pg.locateOnScreen(image_path)
        if image_location is not None:
            
            image_center = pg.center(image_location)
            pg.click(image_center)
            
      
            break
        else:
            print("I am unable to see it")


# clientmanager('./image/11.png')
# click_image('./image/12.png')
# click_image('./image/13.png')
# clientmanager('./image/14.png')
# typehost('./image/15.png')
# typehub('./image/16.png')
# click_image('./image/17.png')
# click_image('./image/18.png')
# typeusername('./image/19.png')
# typepassword('./image/20.png')
# click_image('./image/21.png')
# clickrightlift('./image/22.png')
# click_image('./image/23.png')
# click_image('./image/24.png')

# clickrightlift('./image/25.png')
# click_image('./image/26.png')
# click_image('./image/27.png')

# click_right('./image/28.png')
# click_image('./image/29.png')
# click_image('./image/30.png')

click_right('./image/28.png')
click_image('./image/29.png')
click_image('./image/31.png')