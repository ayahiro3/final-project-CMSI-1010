# main file for running shadle game
# import needed libraries and modules
import pygame
import random
import sys

# initialize pygame 
pygame.init()

# Setting up game variables.
white = (255, 255, 255)
black = (0, 0, 0)
gray = (127, 127, 127)
red = (255, 0, 0)
orange = (255, 128, 0)
yellow = (255, 215, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
purple = (148, 0, 211)
pink = (255, 20, 147)
lightgray = (220,220,220)

width = 600
height = 900
btn_width = 100
btn_height = 50
color_width = 50
color_height = 50

# initialize variables
color_choices = [red, orange, yellow, green, blue, purple]
color_sequence = [white, white, white, white]
attempt_counter = 0

# initialize user guess as a blank list
user_guess = []

# Setting up the game display.
display_width = 600 
display_height = 750

key = pygame.key.get_pressed()

# display
screen = pygame.display.set_mode((width, height))
window = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Shadle')

# button class 
class Button:
    def __init__(self, x, y , width, height, text, color, action=None):
        self.box = pygame.Rect(x, y, width, height)
        self.text = text
        self.color = color


    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.box)
        font = pygame.font.Font(None, 16)
        text = font.render(self.text, True, (0,0,0))
        text_box = text.get_rect(center = self.box.center)
        screen.blit(text, text_box)

    def is_clicked(self, mouse_click):
        return self.box.collidepoint(mouse_click)
    
# empty_space class 
class Empty_Space:
    def __init__(self, x, y, width, height, color):
        self.box = pygame.Rect(x, y, width, height)
        self.color = color
    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.box)

# generates the sequence to be guessed
def generate_sequence():
    for i in range(len(color_sequence)):
        color_sequence[i] = random.choice(color_choices)
    return color_sequence

# compares user_guess to color_sequence
def check_guess():
    global attempt_counter

    attempt_counter +=1

    # check if user guess equals the color sequence and wins the game
    if user_guess == color_sequence:
        win_game()

    #condition for losing so that it goes to intro screen
    if attempt_counter >= 6:
        lose_game()

    # gives hints for the color sequence
    else:
        for i in range(len(user_guess)):
            subtitle_x = (display_width - 100) // (2)
            subtitle_y = ((display_height) // (8)) + 15 * i

            if user_guess[i] == color_sequence[i]:
                medtext = pygame.font.SysFont('franklingothicmedium', 20)
                SmallSurf, SmallRect = text_objects('''Box''' + str(i + 1) + ''': Correct color, correct place.''', medtext)
                SmallRect.center =(subtitle_x, subtitle_y)

                window.blit(SmallSurf, SmallRect)

            else:
                if user_guess[i] in color_sequence:
                    medtext = pygame.font.SysFont('franklingothicmedium', 20)
                    SmallSurf, SmallRect = text_objects('''Box''' + str(i + 1) + ''': Correct color, incorrect place.''', medtext)
                    SmallRect.center =(subtitle_x, subtitle_y)
                    window.blit(SmallSurf, SmallRect)
                else:
                    medtext = pygame.font.SysFont('franklingothicmedium', 20)
                    SmallSurf, SmallRect = text_objects('''Box''' + str(i + 1) + ''': Incorrect color, incorrect place.''', medtext)
                    SmallRect.center =(subtitle_x, subtitle_y)
                    window.blit(SmallSurf, SmallRect)
    
    # continue button
    continue_button = Button(400, 50, 100, 50, 'Continue', pink)
    continue_button.draw(screen)

    checking = True
    while checking:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_click = event.pos
                if continue_button.is_clicked(mouse_click):
                    return
        pygame.display.update()
        
def quitgame():
# quits the game
   pygame.quit()
   quit()

def text_objects(text, font):
    # text objects for screen
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def lose_game():
    global attempt_counter
    # will show up if the user loses
    # lose game screen
    window.fill(lightgray)
    largeText = pygame.font.SysFont('franklingothicmedium', 100)
    medtext = pygame.font.SysFont('franklingothicmedium', 30)
    TextSurf, TextRect = text_objects('Shadle', largeText)
    TextRect.center = (display_width/2), (display_height/2)
    SmallSurf, SmallRect = text_objects('''You lost!''', medtext)
    subtitle_x = (display_width ) // (2)
    subtitle_y = (display_width +500) // (2)
    SmallRect.center =(subtitle_x, subtitle_y)
    window.blit(TextSurf, TextRect)
    window.blit(SmallSurf, SmallRect)

    # making x and y coordinates to center the buttons
    play_again_button_x = (display_width -300) // (2)
    quit_button_x = (display_width +100) // (2)
    play_again_button_y = (display_width +600) // (2)
    quit_button_y = (display_width +600) // (2)

    # create buttons for the start of the game
    play_again_button = Button(play_again_button_x, play_again_button_y, 100, 50, "Play again", pink)
    quit_button= Button(quit_button_x, quit_button_y, 100, 50, "Quit", pink, quitgame)
    play_again_button.draw(screen)
    quit_button.draw(screen)

    # remove previous user guess and reset attempts
    user_guess.clear()
    attempt_counter = 0
    
    # while loop for loss screen
    lose = True
    while lose:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_click = event.pos
                if play_again_button.is_clicked(mouse_click):
                    button_loop()
                elif quit_button.is_clicked(mouse_click):
                    quitgame()
            
        pygame.display.update()

def win_game():
    global attempt_counter
    # will show up if the user wins
    # set up text modeled after wordle
    window.fill(lightgray)
    largeText = pygame.font.SysFont('franklingothicmedium', 100)
    medtext = pygame.font.SysFont('franklingothicmedium', 30)
    TextSurf, TextRect = text_objects('Shadle', largeText)
    TextRect.center = (display_width/2), (display_height/2)
    SmallSurf, SmallRect = text_objects('''You win!''', medtext)
    subtitle_x = (display_width ) // (2)
    subtitle_y = (display_width +500) // (2)
    SmallRect.center =(subtitle_x, subtitle_y)
    window.blit(TextSurf, TextRect)
    window.blit(SmallSurf, SmallRect)

    # making x and y coordinates to center the buttons
    play_again_button_x = (display_width -300) // (2)
    quit_button_x = (display_width +100) // (2)
    play_again_button_y = (display_width +600) // (2)
    quit_button_y = (display_width +600) // (2)

    # create buttons for the start of the game
    play_again_button = Button(play_again_button_x, play_again_button_y, 100, 50, "Play again", pink)
    quit_button= Button(quit_button_x, quit_button_y, 100, 50, "Quit", pink, quitgame)
    play_again_button.draw(screen)
    quit_button.draw(screen)

    # remove previous user guess and reset attempts
    user_guess.clear()
    attempt_counter = 0

    # while loop for win screen
    win = True
    while win:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_click = event.pos
                if play_again_button.is_clicked(mouse_click):
                    button_loop()
                elif quit_button.is_clicked(mouse_click):
                    quitgame()
            
        pygame.display.update()


def game_intro():
    # set up game intro, user can either click start or quit
    # set up intro display
    # set up background image that I drew in procreate
    image = pygame.image.load('shadle_logo.png')
    window.blit(image, image.get_rect())
    largeText = pygame.font.SysFont('franklingothicmedium', 100)
    medtext = pygame.font.SysFont('franklingothicmedium', 30)
    TextSurf, TextRect = text_objects('Shadle', largeText)
    TextRect.center = (display_width/2), (display_height/2)
    SmallSurf, SmallRect = text_objects('''Get 6 chances to guess a 4 color sequence.''', medtext)
    subtitle_x = (display_width ) // (2)
    subtitle_y = (display_width +500) // (2)
    SmallRect.center =(subtitle_x, subtitle_y)
    window.blit(TextSurf, TextRect)
    window.blit(SmallSurf, SmallRect)

    # making x and y coordinates to center the buttons
    start_button_x = (display_width -300) // (2)
    quit_button_x = (display_width +100) // (2)
    start_button_y = (display_width +600) // (2)
    quit_button_y = (display_width +600) // (2)

    # create buttons for the start of the game
    start_button = Button(start_button_x, start_button_y, 100, 50, "Play", pink)
    quit_button= Button(quit_button_x, quit_button_y, 100, 50, "Quit", pink, quitgame)
    start_button.draw(screen)
    quit_button.draw(screen)

    # while loop for intro
    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_click = event.pos
                if start_button.is_clicked(mouse_click):
                    button_loop()
                    # intro = False
                elif quit_button.is_clicked(mouse_click):
                    quitgame()
                    # intro = False
            
        pygame.display.update()

# main button loop
def button_loop():
    # generating the sequence a user will guess
    generate_sequence()

    # updating buttons
    enter_btn = Button(width // 1.1 - btn_width // 1.1, height // 1.4 - btn_height // 1.4, btn_width, btn_height, 'Enter', lightgray)
    delete_btn = Button(width // 1.1 - btn_width // 1.1, height // 1.25 - btn_height // 1.25, btn_width, btn_height, 'Delete', lightgray)

    # color buttons
    red_btn = Button(width // 5 - color_width // 1, height // 1.4 - color_height // 1.4, color_width, color_height, "", red)
    orange_btn = Button(width // 3 - color_width // 1, height // 1.4 - color_height // 1.4, color_width, color_height, "", orange)
    yellow_btn = Button(width // 2.142857 - color_width // 1, height // 1.4 - color_height // 1.4, color_width, color_height, "", yellow)
    green_btn = Button(width // 5 - color_width // 1, height // 1.25 - color_height // 1.25, color_width, color_height, "", green)
    blue_btn = Button(width // 3 - color_width // 1, height // 1.25 - color_height // 1.25, color_width, color_height, "", blue)
    purple_btn = Button(width // 2.142857 - color_width // 1, height // 1.25 - color_height // 1.25, color_width, color_height, "", purple)

    # empty space buttons
    #empty spaces(Line-1)
    emp_spc0 = Empty_Space(width // 5, height // 5.5, color_width * 1, color_height * 1, gray)
    emp_spc1 = Empty_Space(width // 3, height // 5.5, color_width * 1, color_height * 1, gray)
    emp_spc2 = Empty_Space(width // 2.142857, height // 5.5, color_width * 1, color_height * 1, gray)
    emp_spc3 = Empty_Space(width // 1.666666, height // 5.5, color_width * 1, color_height * 1, gray)
    #empty spaces(Line-2)
    emp_spc4 = Empty_Space(width // 5, height // 4, color_width * 1, color_height * 1, gray)
    emp_spc5 = Empty_Space(width // 3, height // 4, color_width * 1, color_height * 1, gray)
    emp_spc6 = Empty_Space(width // 2.142857, height // 4, color_width * 1, color_height * 1, gray)
    emp_spc7 = Empty_Space(width // 1.666666, height // 4, color_width * 1, color_height * 1, gray)
    #empty spaces(Line-3)
    emp_spc8 = Empty_Space(width // 5, height // 3.1, color_width * 1, color_height * 1, gray)
    emp_spc9 = Empty_Space(width // 3, height // 3.1, color_width * 1, color_height * 1, gray)
    emp_spc10 = Empty_Space(width // 2.142857, height // 3.1, color_width * 1, color_height * 1, gray)
    emp_spc11 = Empty_Space(width // 1.666666, height // 3.1, color_width * 1, color_height * 1, gray)
    #empty spaces(Line-4)
    emp_spc12 = Empty_Space(width // 5, height // 2.55, color_width * 1, color_height * 1, gray)
    emp_spc13 = Empty_Space(width // 3, height // 2.55, color_width * 1, color_height * 1, gray)
    emp_spc14 = Empty_Space(width // 2.142857, height // 2.55, color_width * 1, color_height * 1, gray)
    emp_spc15 = Empty_Space(width // 1.666666, height // 2.55, color_width * 1, color_height * 1, gray)
    #empty spaces(Line-5)
    emp_spc16 = Empty_Space(width // 5, height // 2.16, color_width * 1, color_height * 1, gray)
    emp_spc17 = Empty_Space(width // 3, height // 2.16, color_width * 1, color_height * 1, gray)
    emp_spc18 = Empty_Space(width // 2.142857, height // 2.16, color_width * 1, color_height * 1, gray)
    emp_spc19 = Empty_Space(width // 1.666666, height // 2.16, color_width * 1, color_height * 1, gray)
    #empty spaces(Line-6)
    emp_spc20 = Empty_Space(width // 5, height // 1.88, color_width * 1, color_height * 1, gray)
    emp_spc21 = Empty_Space(width // 3, height // 1.88, color_width * 1, color_height * 1, gray)
    emp_spc22 = Empty_Space(width // 2.142857, height // 1.88, color_width * 1, color_height * 1, gray)
    emp_spc23 = Empty_Space(width // 1.666666, height // 1.88, color_width * 1, color_height * 1, gray)

    # set up variables 
    empty_space_index = 0
    number_times_clicked = 0
    can_click = True

    while True:
        empty_spaces = [emp_spc0, emp_spc1, emp_spc2, emp_spc3, emp_spc4, emp_spc5, emp_spc6, emp_spc7, 
                        emp_spc8, emp_spc9, emp_spc10, emp_spc11, emp_spc12, emp_spc13, emp_spc14, 
                        emp_spc15, emp_spc16, emp_spc17, emp_spc18, emp_spc19, emp_spc20, emp_spc21, 
                        emp_spc22, emp_spc23]

        for event in pygame.event.get():
                # check to see if the number of times clicked is 4, or one row, and if it is you can't click anymore
                if number_times_clicked == 4: 
                    can_click = False
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                # Checks for mouse interaction with the button
                # Executes display of user guess
                key = pygame.key.get_pressed()
                # keyboard enter button

                if key[pygame.K_RETURN] or key[pygame.K_KP_ENTER]:
                    number_times_clicked = 0
                    can_click = True
                        # Perform button action here
                    if len(user_guess) == 4:
                        check_guess()   
                        user_guess.clear()
                # UI enter button
                elif event.type == pygame.MOUSEMOTION:
                    if enter_btn.box.collidepoint(event.pos):
                        enter_btn.color = gray
                    else:
                        enter_btn.color = lightgray

                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1 and enter_btn.box.collidepoint(event.pos):
                        number_times_clicked = 0
                        can_click = True
                        enter_btn.color = white
                        # Perform button action here
                        if len(user_guess) == 4:
                            check_guess()   
                            user_guess.clear()

                elif event.type == pygame.MOUSEBUTTONUP:
                    if event.button == 1 and enter_btn.box.collidepoint(event.pos):
                        enter_btn.color = lightgray

                # key board delete button 
                if key[pygame.K_BACKSPACE] or key[pygame.K_DELETE]:
                    number_times_clicked -=1
                    delete_btn.color = black
                    # Perform button action here
                    if user_guess != [] :
                        # delete from list if pressed backspace or the button
                        user_guess.pop()
                        empty_space_index = (empty_space_index - 1) % len(empty_spaces)
                        empty_spaces[empty_space_index].color = gray

                # UI delete button
                elif event.type == pygame.MOUSEMOTION:
                    if delete_btn.box.collidepoint(event.pos):
                        delete_btn.color = gray
                    else:
                        delete_btn.color = lightgray

                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1 and delete_btn.box.collidepoint(event.pos):
                        number_times_clicked -=1
                        delete_btn.color = black
                        # Perform button action here
                        if user_guess != [] :
                            user_guess.pop()

                            empty_space_index = (empty_space_index - 1) % len(empty_spaces)
                            empty_spaces[empty_space_index].color = gray

                elif event.type == pygame.MOUSEBUTTONUP:
                    if event.button == 1 and delete_btn.box.collidepoint(event.pos):
                        delete_btn.color = lightgray

                # red button
                if event.type == pygame.MOUSEMOTION:
                    if red_btn.box.collidepoint(event.pos):
                        red_btn.color = gray
                    else:
                        red_btn.color = red

                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1 and red_btn.box.collidepoint(event.pos) and can_click:
                        number_times_clicked +=1
                        red_btn.color = black
                        # Perform button action here
                        if len(user_guess) < 4:
                            user_guess.append(red)
                            empty_spaces[empty_space_index].color = red
                            empty_space_index = (empty_space_index + 1) % len(empty_spaces)

                elif event.type == pygame.MOUSEBUTTONUP:
                    if event.button == 1 and red_btn.box.collidepoint(event.pos):
                        red_btn.color = red

                # orange button
                if event.type == pygame.MOUSEMOTION:
                    if orange_btn.box.collidepoint(event.pos):
                        orange_btn.color = gray
                    else:
                        orange_btn.color = orange

                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1 and orange_btn.box.collidepoint(event.pos) and can_click:
                        number_times_clicked +=1
                        orange_btn.color = black
                        # Perform button action here
                        user_guess.append(orange)
                        empty_spaces[empty_space_index].color = orange
                        empty_space_index = (empty_space_index + 1) % len(empty_spaces)

                elif event.type == pygame.MOUSEBUTTONUP:
                    if event.button == 1 and orange_btn.box.collidepoint(event.pos):
                        orange_btn.color = orange

                # yellow button
                if event.type == pygame.MOUSEMOTION:
                    if yellow_btn.box.collidepoint(event.pos):
                        yellow_btn.color = gray
                    else:
                        yellow_btn.color = yellow

                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1 and yellow_btn.box.collidepoint(event.pos) and can_click:
                        number_times_clicked +=1
                        yellow_btn.color = black
                        # Perform button action here
                        user_guess.append(yellow)
                        empty_spaces[empty_space_index].color = yellow
                        empty_space_index = (empty_space_index + 1) % len(empty_spaces)

                elif event.type == pygame.MOUSEBUTTONUP:
                    if event.button == 1 and yellow_btn.box.collidepoint(event.pos):
                        yellow_btn.color = yellow

                # green button
                if event.type == pygame.MOUSEMOTION:
                    if green_btn.box.collidepoint(event.pos):
                        green_btn.color = gray
                    else:
                        green_btn.color = green

                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1 and green_btn.box.collidepoint(event.pos) and can_click:
                        number_times_clicked +=1
                        green_btn.color = black
                        # Perform button action here
                        user_guess.append(green)
                        empty_spaces[empty_space_index].color = green
                        empty_space_index = (empty_space_index + 1) % len(empty_spaces)

                elif event.type == pygame.MOUSEBUTTONUP:
                    if event.button == 1 and green_btn.box.collidepoint(event.pos):
                        green_btn.color = green

                # blue button
                if event.type == pygame.MOUSEMOTION:
                    if blue_btn.box.collidepoint(event.pos):
                        blue_btn.color = gray
                    else:
                        blue_btn.color = blue

                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1 and blue_btn.box.collidepoint(event.pos) and can_click:
                        number_times_clicked +=1
                        blue_btn.color = black
                        # Perform button action here
                        user_guess.append(blue)
                        empty_spaces[empty_space_index].color = blue
                        empty_space_index = (empty_space_index + 1) % len(empty_spaces)

                elif event.type == pygame.MOUSEBUTTONUP:
                    if event.button == 1 and blue_btn.box.collidepoint(event.pos):
                        blue_btn.color = blue
                # purple button
                if event.type == pygame.MOUSEMOTION:
                    if purple_btn.box.collidepoint(event.pos):
                        purple_btn.color = gray
                    else:
                        purple_btn.color = purple

                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1 and purple_btn.box.collidepoint(event.pos) and can_click:
                        number_times_clicked +=1
                        purple_btn.color = black
                        # Perform button action here
                        user_guess.append(purple)
                        empty_spaces[empty_space_index].color = purple
                        empty_space_index = (empty_space_index + 1) % len(empty_spaces)

                elif event.type == pygame.MOUSEBUTTONUP:
                    if event.button == 1 and purple_btn.box.collidepoint(event.pos):
                        purple_btn.color = purple
            

        # Clear the screen
        screen.fill((255, 255, 255))

        # Draw the button
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

        # Shadle lettering on main screen setup
        letters = pygame.font.SysFont('franklingothicmedium', 80)
        S_Surf, S_Rect = text_objects('S', letters)
        H_Surf, H_Rect = text_objects('H', letters)
        A_Surf, A_Rect = text_objects('A', letters)
        D_Surf, D_Rect = text_objects('D', letters)
        L_Surf, L_Rect = text_objects('L', letters)
        E_Surf, E_Rect = text_objects('E', letters)
        s_x = (display_width + 350 ) // (2)
        s_y = (display_width -250) // (2)
        h_x = (display_width + 350 ) // (2)
        h_y = (display_width -150) // (2)
        a_x = (display_width +350) // (2)
        a_y = (display_width -50) // (2)
        d_x = (display_width + 350 ) // (2)
        d_y = (display_width +50) // (2)
        l_x = (display_width + 350 ) // (2)
        l_y = (display_width +150) // (2)
        e_x = (display_width + 350 ) // (2)
        e_y = (display_width +250) // (2)
        S_Rect.center = (s_x), (s_y)
        H_Rect.center = (h_x), (h_y)
        A_Rect.center = (a_x), (a_y)
        D_Rect.center = (d_x), (d_y)
        L_Rect.center = (l_x), (l_y)
        E_Rect.center = (e_x), (e_y)
        window.blit(S_Surf, S_Rect)
        window.blit(H_Surf, H_Rect)
        window.blit(A_Surf, A_Rect)
        window.blit(D_Surf, D_Rect)
        window.blit(L_Surf, L_Rect)
        window.blit(E_Surf, E_Rect)
        
       

        # Update the display
        pygame.display.flip()

        # Cap the frame rate
        pygame.time.Clock().tick(60)

# call the intro to begin the game
game_intro()
