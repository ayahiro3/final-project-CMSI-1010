# Preliminary version of the button and empty space classes.

# Import pygame and sys.
import pygame as pg
import sys

# initialize pygame
pg.init()

# measurements and variables to use throughout
width = 600
height = 900
btn_width = 50
btn_height = 50
color_width = 50
color_height = 50
key = pg.key.get_pressed()

# button class
class Button:
    def __init__(self, x, y , width, height, text):
        self.box = pg.Rect(x, y, width, height)
        self.text = text
        self.color = (50,125,225)

    def draw(self, screen):
        pg.draw.rect(screen, self.color, self.box)
        font = pg.font.Font(None, 16)
        text = font.render(self.text, True, (0,0,0))
        text_box = text.get_rect(center = self.box.center)
        screen.blit(text, text_box)

# empty space class
class Empty_Space:
    def __init__(self, x, y, width, height, color):
        self.box = pg.Rect(x, y, width, height)
        self.color = color
    def draw(self, screen):
        pg.draw.rect(screen, self.color, self.box)
    
# set up the display
screen = pg.display.set_mode((width, height))
pg.display.set_caption('Shadle')

# updating buttons
# delete and enter buttons
enter_btn = Button(width // 1.666666, height // 1.25, btn_width, btn_height, 'Enter')
delete_btn = Button(width // 1.666666, height // 1.1, btn_width, btn_height, 'Delete')

# empty spaces(Line-1)
emp_spc0 = Empty_Space(width // 5, height // 3, color_width * 1, color_height * 1,(50,125,225))
emp_spc1 = Empty_Space(width // 3, height // 3, color_width * 1, color_height * 1,(50,125,225))
emp_spc2 = Empty_Space(width // 2.142857, height // 3, color_width * 1, color_height * 1,(50,125,225))
emp_spc3 = Empty_Space(width // 1.666666, height // 3, color_width * 1, color_height * 1,(50,125,225))
# empty spaces(Line-2)
emp_spc4 = Empty_Space(width // 5, height // 2.5, color_width * 1, color_height * 1,(50,125,225))
emp_spc5 = Empty_Space(width // 3, height // 2.5, color_width * 1, color_height * 1,(50,125,225))
emp_spc6 = Empty_Space(width // 2.142857, height // 2.5, color_width * 1, color_height * 1,(50,125,225))
emp_spc7 = Empty_Space(width // 1.666666, height // 2.5, color_width * 1, color_height * 1,(50,125,225))
# empty spaces(Line-3)
emp_spc8 = Empty_Space(width // 5, height // 2.14285714, color_width * 1, color_height * 1,(50,125,225))
emp_spc9 = Empty_Space(width // 3, height // 2.14285714, color_width * 1, color_height * 1,(50,125,225))
emp_spc10 = Empty_Space(width // 2.142857, height // 2.14285714, color_width * 1, color_height * 1,(50,125,225))
emp_spc11 = Empty_Space(width // 1.666666, height // 2.14285714, color_width * 1, color_height * 1,(50,125,225))
# empty spaces(Line-4)
emp_spc12 = Empty_Space(width // 5, height // 1.875, color_width * 1, color_height * 1,(50,125,225))
emp_spc13 = Empty_Space(width // 3, height // 1.875, color_width * 1, color_height * 1,(50,125,225))
emp_spc14 = Empty_Space(width // 2.142857, height // 1.875, color_width * 1, color_height * 1,(50,125,225))
emp_spc15 = Empty_Space(width // 1.666666, height // 1.875, color_width * 1, color_height * 1,(50,125,225))
# empty spaces(Line-5)
emp_spc16 = Empty_Space(width // 5, height // 1.6666667, color_width * 1, color_height * 1,(50,125,225))
emp_spc17 = Empty_Space(width // 3, height // 1.6666667, color_width * 1, color_height * 1,(50,125,225))
emp_spc18 = Empty_Space(width // 2.142857, height // 1.6666667, color_width * 1, color_height * 1,(50,125,225))
emp_spc19 = Empty_Space(width // 1.666666, height // 1.6666667, color_width * 1, color_height * 1,(50,125,225))
# empty spaces(Line-6)
emp_spc20 = Empty_Space(width // 5, height // 1.5, color_width * 1, color_height * 1,(50,125,225))
emp_spc21 = Empty_Space(width // 3, height // 1.5, color_width * 1, color_height * 1,(50,125,225))
emp_spc22 = Empty_Space(width // 2.142857, height // 1.5, color_width * 1, color_height * 1,(50,125,225))
emp_spc23 = Empty_Space(width // 1.666666, height // 1.5, color_width * 1, color_height * 1,(50,125,225))

# color buttons
red_btn = Button(width // 5, height // 1.25, color_width, color_height, "")
orange_btn = Button(width // 3, height // 1.25, color_width, color_height, "")
yellow_btn = Button(width // 2.142857, height // 1.25, color_width, color_height, "")
green_btn = Button(width // 5, height // 1.1, color_width, color_height, "")
blue_btn = Button(width // 3, height // 1.1, color_width, color_height, "")
purple_btn = Button(width // 2.142857, height // 1.1, color_width, color_height, "")

# creating loop to display buttons in button class
while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()

        # Check for mouse interaction with the button
        if event.type == pg.MOUSEMOTION:
            if enter_btn.box.collidepoint(event.pos):
                enter_btn.color = (100,175,255)
            else:
                enter_btn.color = (50,125,255)

        if event.type == pg.MOUSEBUTTONDOWN:
            if event.button == 1 and enter_btn.box.collidepoint(event.pos):
                enter_btn.color = (25,50,200)
                # Perform button action here

        if event.type == pg.MOUSEBUTTONUP:
            if event.button == 1 and enter_btn.box.collidepoint(event.pos):
                enter_btn.color = (100,175,255)
#_-_-_-_-_-_-_-_-        
        if event.type == pg.MOUSEMOTION:
            if delete_btn.box.collidepoint(event.pos):
                delete_btn.color = (100,175,255)
            else:
                delete_btn.color = (50,125,255)

        if event.type == pg.MOUSEBUTTONDOWN:
            if event.button == 1 and delete_btn.box.collidepoint(event.pos):
                delete_btn.color = (25,50,200)
                # Perform button action here

        if event.type == pg.MOUSEBUTTONUP:
            if event.button == 1 and delete_btn.box.collidepoint(event.pos):
                delete_btn.color = (100,175,255)
#_-_-_-_-_-_-_-_-
        if event.type == pg.MOUSEMOTION:
            if red_btn.box.collidepoint(event.pos):
                red_btn.color = (255,0,0)
            else:
                red_btn.color = (255,0,0)

        if event.type == pg.MOUSEBUTTONDOWN:
            if event.button == 1 and red_btn.box.collidepoint(event.pos):
                red_btn.color = (220,0,0)
                # Perform button action here

        if event.type == pg.MOUSEBUTTONUP:
            if event.button == 1 and red_btn.box.collidepoint(event.pos):
                red_btn.color = (255,0,0)
#_-_-_-_-_-_-_-_-
        if event.type == pg.MOUSEMOTION:
            if orange_btn.box.collidepoint(event.pos):
                orange_btn.color = (255,130,0)
            else:
                orange_btn.color = (255,130,0)

        if event.type == pg.MOUSEBUTTONDOWN:
            if event.button == 1 and orange_btn.box.collidepoint(event.pos):
                orange_btn.color = (230,115,0)
                # Perform button action here

        if event.type == pg.MOUSEBUTTONUP:
            if event.button == 1 and orange_btn.box.collidepoint(event.pos):
                orange_btn.color = (255,130,0)
#_-_-_-_-_-_-_-_-
        if event.type == pg.MOUSEMOTION:
            if yellow_btn.box.collidepoint(event.pos):
                yellow_btn.color = (255,240,0)
            else:
                yellow_btn.color = (255,240,0)

        if event.type == pg.MOUSEBUTTONDOWN:
            if event.button == 1 and yellow_btn.box.collidepoint(event.pos):
                yellow_btn.color = (235,225,0)
                # Perform button action here

        if event.type == pg.MOUSEBUTTONUP:
            if event.button == 1 and yellow_btn.box.collidepoint(event.pos):
                yellow_btn.color = (255,240,0)
#_-_-_-_-_-_-_-_-
        if event.type == pg.MOUSEMOTION:
            if green_btn.box.collidepoint(event.pos):
                green_btn.color = (0,240,0)
            else:
                green_btn.color = (0,240,0)

        if event.type == pg.MOUSEBUTTONDOWN:
            if event.button == 1 and green_btn.box.collidepoint(event.pos):
                green_btn.color = (0,205,0)
                # Perform button action here

        if event.type == pg.MOUSEBUTTONUP:
            if event.button == 1 and green_btn.box.collidepoint(event.pos):
                green_btn.color = (0,240,0)
#_-_-_-_-_-_-_-_-
        if event.type == pg.MOUSEMOTION:
            if blue_btn.box.collidepoint(event.pos):
                blue_btn.color = (50,70,255)
            else:
                blue_btn.color = (50,70,255)

        if event.type == pg.MOUSEBUTTONDOWN:
            if event.button == 1 and blue_btn.box.collidepoint(event.pos):
                blue_btn.color = (0,0,200)
                # Perform button action here

        if event.type == pg.MOUSEBUTTONUP:
            if event.button == 1 and blue_btn.box.collidepoint(event.pos):
                blue_btn.color = (50,70,255)
#_-_-_-_-_-_-_-_-
        if event.type == pg.MOUSEMOTION:
            if purple_btn.box.collidepoint(event.pos):
                purple_btn.color = (150,0,240)
            else:
                purple_btn.color = (150,0,240)

        if event.type == pg.MOUSEBUTTONDOWN:
            if event.button == 1 and purple_btn.box.collidepoint(event.pos):
                purple_btn.color = (100,0,215)
                # Perform button action here

        if event.type == pg.MOUSEBUTTONUP:
            if event.button == 1 and purple_btn.box.collidepoint(event.pos):
                purple_btn.color = (150,0,240)
        


    # Clear the screen
    screen.fill((255, 255, 255))

    # Draw the buttons
    enter_btn.draw(screen)
    delete_btn.draw(screen)
    red_btn.draw(screen)
    orange_btn.draw(screen)
    yellow_btn.draw(screen)
    blue_btn.draw(screen)
    green_btn.draw(screen)
    purple_btn.draw(screen)
    # Draw The Empty Spaces
    emp_spc0.draw(screen)
    emp_spc1.draw(screen)
    emp_spc2.draw(screen)
    emp_spc3.draw(screen)
    emp_spc4.draw(screen)
    emp_spc5.draw(screen)
    emp_spc6.draw(screen)
    emp_spc7.draw(screen)
    emp_spc8.draw(screen)
    emp_spc9.draw(screen)
    emp_spc10.draw(screen)
    emp_spc11.draw(screen)
    emp_spc12.draw(screen)
    emp_spc13.draw(screen)
    emp_spc14.draw(screen)
    emp_spc15.draw(screen)
    emp_spc16.draw(screen)
    emp_spc17.draw(screen)
    emp_spc18.draw(screen)
    emp_spc19.draw(screen)
    emp_spc20.draw(screen)
    emp_spc20.draw(screen)
    emp_spc21.draw(screen)
    emp_spc22.draw(screen)
    emp_spc23.draw(screen)

    # Update the display
    pg.display.flip()

    # Cap the frame rate
    pg.time.Clock().tick(60)
