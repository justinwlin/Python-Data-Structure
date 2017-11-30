import pygame, random, sys
from pygame.locals import *

# --- Globals ---
# Colors
#           R    G    B
WHITE 	= (255, 255, 255)
GREEN 	= (78, 255, 87)
YELLOW 	= (241, 255, 0)
BLUE 	= (80, 255, 239)
PURPLE 	= (203, 0, 255)
RED 	= (237, 28, 36)
BLACK   = (0,   0,   0)

# Set the initial starting point
xs = [290, 290, 290, 290, 290]
ys = [290, 270, 250, 230, 210]

#Initializes Direction and Score
dirs = 0
score = 0

#Initializes position of apple
applepos = (random.randint(0, 590), random.randint(0, 590))

#Initializes sizeOfApple:
sizeOfApple = 20

#Initializes size of each snake segment
SnakeSize = 20

# Call this function so the Pygame library can initialize itself
pygame.init()

# Create an 800x600 sized screen
height_screen = 600
width_screen = 600
s = pygame.display.set_mode([width_screen, height_screen])

# Set the title of the window
pygame.display.set_caption('The best game')

#Coloring in APPLE
appleimage = pygame.Surface((sizeOfApple, sizeOfApple))
appleimage.fill(RED)

#Coloring in snake
img = pygame.Surface((SnakeSize, SnakeSize))
img.fill(YELLOW)

#System Font + Flock Speed
f = pygame.font.SysFont('Arial', 20)
clock = pygame.time.Clock()

#Clock Speed
clockSpeed = 10
done = False


# --- Functions ---
def collide(x1, x2, y1, y2, w1, w2, h1, h2):
    if x1 + w1 > x2 and x1 < x2 + w2 and y1 + h1 > y2 and y1 < y2 + h2:
        return True
    else:
        return False


def die(screen, score):
    f = pygame.font.SysFont('Arial', 30)
    t = f.render('Your score was: ' + str(score), True, (0, 0, 0))
    screen.blit(t, (10, 270))
    pygame.display.update()
    pygame.time.wait(2000)
    sys.exit(0)


def snakeLogic():
    if dirs == 0:
        ys[0] += SnakeSize
    elif dirs == 1:
        xs[0] += SnakeSize
    elif dirs == 2:
        ys[0] -= SnakeSize
    elif dirs == 3:
        xs[0] -= SnakeSize

pygame.mixer.music.load('naruto.wav')
pygame.mixer.music.set_endevent(pygame.constants.USEREVENT)
pygame.mixer.music.play()

#GAME UPDATE
while not done:
    clock.tick(clockSpeed)
    pygame.draw.ellipse(s, BLUE, [100, 100, 200, 50])
    for e in pygame.event.get():
        if e.type == KEYDOWN:
            if e.key == K_UP and dirs != 0:
                dirs = 2
            elif e.key == K_DOWN and dirs != 2:
                dirs = 0
            elif e.key == K_LEFT and dirs != 1:
                dirs = 3
            elif e.key == K_RIGHT and dirs != 3:
                dirs = 1
            if e.key == K_ESCAPE:
                sys.exit(0)
            if e.key == K_0:
                clockSpeed = 1
            if e.key == K_5:
                clockSpeed = 5
            if e.key == K_9:
                clockSpeed = 9
        if e.type == pygame.constants.USEREVENT:
            pygame.mixer.music.load('naruto.wav')
            pygame.mixer.music.play()


    i = len(xs) - 1

    while i >= 2:
        if collide(xs[0], xs[i], ys[0], ys[i], SnakeSize, SnakeSize, SnakeSize, SnakeSize):
            die(s, score)
        i -= 1

    if collide(xs[0], applepos[0], ys[0], applepos[1], SnakeSize, sizeOfApple, SnakeSize, sizeOfApple):
        score += 1
        xs.append(0)
        ys.append(0)
        applepos = (random.randint(0, 590), random.randint(0, 590))

    if xs[0] < 0 or xs[0] > 580 or ys[0] < 0 or ys[0] > 580:
        die(s, score)

    i = len(xs) - 1

    while i >= 1:
        xs[i] = xs[i - 1]
        ys[i] = ys[i - 1]
        i -= 1

    #INCREASING SNAKE SIZE LOGIC
    snakeLogic()

    #Background Color
    s.fill(BLUE)

    #REfreshing the Snake
    for i in range(0, len(xs)):
        s.blit(img, (xs[i], ys[i]))

    #Refreshing the Apple
    s.blit(appleimage, applepos)

    #Refreshing the rending of the score
    t = f.render("Score: " + str(score), True, BLACK)

    #Pixel Location of Score
    s.blit(t, (10, 10))

    font = pygame.font.SysFont('Arial', 20)
    # -- Draw everything
    t = font.render("Score: " + str(score), True, BLACK)
    #Pixel Location of Score
    s.blit(t, (30, 30))

    pygame.display.update()