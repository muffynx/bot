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
     
            
def click_imageandtype(image_path):
    while True:
        image_location = pg.locateOnScreen(image_path)

        if image_location is not None:
            image_center = pg.center(image_location)
            
            pg.click(image_center)
            time.sleep(0.5)
            pg.write("thai")
            
            break
        else:
            print("I am unable to see it")
       

# First image
click_image('./image/1addinfirefox.png')

# Second image
click_image('./image/2Add.png')

#third image
click_image('./image/3ok.png')

#fourth image
click_image('./image/4cog.png')

#fifth image
click_image('./image/5extension.png')

#sixth image
click_image('./image/6agree.png')

#seventh image
click_image('./image/7agree22.png')


#eighth image
click_imageandtype('./image/8autoserver.png')

#ninth image
click_imageandtype('./image/9flagthailand.png')


