import pygame, random

# --- Globals ---
# Colors
WHITE = (255, 255, 255)
GREEN = (78, 255, 87)
YELLOW = (241, 255, 0)
BLUE = (80, 255, 239)
PURPLE = (203, 0, 255)
RED = (237, 28, 36)
BLACK = (0, 0, 0)

REDBUTTON = (200, 40, 40)
GREENBUTTON = (78, 200, 87)
bright_red = (255,0,0)
bright_green = (0,255,0)

# Set the width and height of each snake segment
segment_width = 15
segment_height = 15
# Margin between each segment
segment_margin = 3

# Set initial speed
x_change = segment_width + segment_margin
y_change = 0

#Set initial score
score = 0


class Segment(pygame.sprite.Sprite):
    """ Class to represent one segment of the snake. """

    # -- Methods
    # Constructor function
    def __init__(self, x, y):
        # Call the parent's constructor
        super().__init__()

        # Set height, width
        self.image = pygame.Surface([segment_width, segment_height])
        self.image.fill(WHITE)

        # Make our top-left corner the passed-in location.
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class APPLE(pygame.sprite.Sprite):
    """ Class to represent one segment of the snake. """

    # -- Methods
    # Constructor function
    def __init__(self, x, y):
        # Call the parent's constructor
        super().__init__()

        # Set height, width
        self.image = pygame.Surface([segment_width, segment_height])
        self.image.fill(BLUE)

        # Make our top-left corner the passed-in location.
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

# Call this function so the Pygame library can initialize itself
pygame.init()

#Joystick

# Create an 800x600 sized screen
height_screen = 600
width_screen = 800
screen = pygame.display.set_mode([width_screen, height_screen])

# Set the title of the window
pygame.display.set_caption('Snake Example')

allspriteslist = pygame.sprite.Group()
applespriteslist = pygame.sprite.Group()

# Create an initial snake
snake_segments = []
apple_segments = []
lengthSnake = 3
for i in range(lengthSnake):
    x = 250 - (segment_width + segment_margin) * i
    y = 30
    segment = Segment(x, y)
    snake_segments.append(segment)
    allspriteslist.add(segment)

clock = pygame.time.Clock()
done = False

#Setting Music
pygame.mixer.music.load('naruto.wav')
pygame.mixer.music.set_endevent(pygame.constants.USEREVENT)
pygame.mixer.music.play()

def textToScreen(str):
    basicfont = pygame.font.SysFont('Arial', 48)
    basicfont.render
    text = basicfont.render(str, True, WHITE, BLACK)
    textrect = text.get_rect()
    textrect.centerx = screen.get_rect().centerx
    textrect.centery = screen.get_rect().centery
    screen.blit(text, textrect)

#initialize Joystick
joystick_count = pygame.joystick.get_count()

# For each joystick:
for i in range(joystick_count):
    joystick = pygame.joystick.Joystick(i)
    joystick.init()

buttons = joystick.get_numbuttons()
hats = joystick.get_numhats()

#Pausing Game
def paused():
    paused = True
    while paused:
        for k in range(buttons):
            newbutton = joystick.get_button(k)
            if newbutton == 1 and (k == 0 or k == 1 or k == 2 or k == 3):
                paused = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    paused = False
                elif event.key == pygame.K_q:
                    pygame.quit()
                    quit()
        screen.fill(WHITE)
        textToScreen("PAUSED: Press a Letter Button To Resume")
        pygame.display.update()
        clock.tick(5)


# def game_intro(intro, brightGreen, brightRed):
#     while intro:
#         for event in pygame.event.get():
#             # print(event)
#             if event.type == pygame.QUIT:
#                 pygame.quit()
#                 quit()
#
#         screen.fill(WHITE)
#         largeText = pygame.font.Font('freesansbold.ttf', 115)
#         textToScreen("A bit Racey" + str(brightGreen)+ str(brightRed))
#         for i in range(hats):
#             hat = joystick.get_hat(i)
#             if hat[0] == -1:
#                 brightGreen = True
#                 brightRed = False
#             if hat[0] == 1:
#                 brightGreen = False
#                 brightRed = True
#         if brightGreen is True:
#             pygame.draw.rect(screen, bright_green, (150, 450, 100, 50))
#             pygame.draw.rect(screen, RED, (550, 450, 100, 50))
#         else:
#             pygame.draw.rect(screen, GREENBUTTON, (150, 450, 100, 50))
#             pygame.draw.rect(screen, bright_red, (550, 450, 100, 50))
#
#         for k in range(buttons):
#             newbutton = joystick.get_button(k)
#             if newbutton == 1 and (k == 0 or k == 1 or k == 2 or k == 3):
#                 intro = False
#
#         pygame.display.update()
#         clock.tick(15)
#     return

while not done:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        # Set the speed based on the key pressed
        # We want the speed to be enough that we move a full
        # segment, plus the margin.

        #JOY STICK CONTROL
        # while intro:
        #     pass
        #     #Passing in intro parameter, Start with GreenButton Lit, and Redbutton Unlit
        #     #game_intro(intro, True, False)
        for i in range(hats):
            hat = joystick.get_hat(i)
            if hat[0] == 1:
                x_change = (segment_width + segment_margin)
                y_change = 0
            if hat[0] == -1:
                x_change = (segment_width + segment_margin) * -1
                y_change = 0
            if hat[1] == 1:
                x_change = 0
                y_change = (segment_height + segment_margin) * -1
            if hat[1] == -1:
                x_change = 0
                y_change = (segment_height + segment_margin)
        #Joystick Pause
        for i in range(buttons):
            button = joystick.get_button(i)
            tuple = (i, button)
            if tuple == (7, 1):
                pygame.time.wait(1)
                paused()
        #------------------------------------
        move = 0
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_change = (segment_width + segment_margin) * -1
                y_change = 0
            if event.key == pygame.K_RIGHT:
                x_change = (segment_width + segment_margin)
                y_change = 0
            if event.key == pygame.K_UP:
                x_change = 0
                y_change = (segment_height + segment_margin) * -1
            if event.key == pygame.K_DOWN:
                x_change = 0
                y_change = (segment_height + segment_margin)
            if event.key == pygame.K_p:
                paused()
            if event.key == pygame.K_EQUALS:
                for i in range(1):
                    x = (random.randint(0, width_screen)) - (segment_width + segment_margin) * i
                    y = (random.randint(0, height_screen)) - (segment_width + segment_margin) * i
                    apple = APPLE(x, y)
                    apple_segments.append(apple)
                    allspriteslist.add(apple)
                    applespriteslist.add(apple)
            if event.type == pygame.constants.USEREVENT:
                pygame.mixer.music.load('naruto.wav')
                pygame.mixer.music.play()


    # Get rid of last segment of the snake
    # .pop() command removes last item in list
    old_segment = snake_segments.pop()
    allspriteslist.remove(old_segment)

    # Figure out where new segment will be
    x = snake_segments[0].rect.x + x_change
    y = snake_segments[0].rect.y + y_change
    segment = Segment(x, y)

    # Insert new segment into the list
    snake_segments.insert(0, segment)
    allspriteslist.add(segment)

    #Collision Detection with Apple Sprite:
    collide = False
    collide = pygame.sprite.spritecollide(snake_segments[0], applespriteslist, True)
    if collide:
        score += 1
        for i in range(1):
            x = 0 - 100 * i
            y = 0-100
            segment = Segment(x, y)
            snake_segments.append(segment)
            allspriteslist.add(segment)
    #Bounds the snake

    # -- Draw everything

    # Clear screen
    screen.fill(RED)

    #TEXT
    textToScreen(str(hat))

    #Drawing Sprites
    allspriteslist.draw(screen)

    # Flip screen
    pygame.display.flip()
    pygame.display.update()
    # Pause
    clock.tick(5)

pygame.quit()