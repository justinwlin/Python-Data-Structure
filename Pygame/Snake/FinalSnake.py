import pygame, random, sys, math
from pygame.locals import *

# screenFont = pygame.font.SysFont('Arial', 20)
#         scoreText = screenFont.render("Score: " + str(score), True, BLACK)
#         t = screenFont.render("Clock Speed: " + str(clockSpeed), True, BLACK)
#         #Pixel Location of Score
#         screen.blit(scoreText, (10, 10))
#         screen.blit(t, (10, 35))

def SNAKEGAME():
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

    FONT = 'Arial'

    # Set the initial starting point
    xs = [290, 290, 290, 290, 290]
    ys = [290, 270, 250, 230, 210]

    #Initializes Direction and Score
    dirs = 0
    score = 0
    move = 1

    tempDir = None
    #Initializes position of apple
    applepos = (random.randint(0, 590), random.randint(0, 590))

    #Initializes sizeOfApple:
    sizeOfApple = 20

    #Initializes size of each snake segment
    SnakeSize = 20
    moveAmt = SnakeSize

    # Call this function so the Pygame library can initialize itself
    pygame.init()

    # Create an 800x600 sized screen
    height_screen = 600
    width_screen = 600
    screen = pygame.display.set_mode([width_screen, height_screen])

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
        moveAmt = SnakeSize

        if dirs == - 1:
            i = len(xs) - 1
            move = 1
            # Moves the trailing tail to follow the head
            while i >= 1:
                xs[i] = xs[i]
                ys[i] = ys[i]
                i -= 1

            xs[0] = xs[0]
            ys[0] = xs [0]
            move = 0
            moveAmt = 0
        if dirs == 0:
            ys[0] += moveAmt
        elif dirs == 1:
            xs[0] += moveAmt
        elif dirs == 2:
            ys[0] -= moveAmt
        elif dirs == 3:
            xs[0] -= moveAmt

        # if dirs == 0:
        #     ys[0] += SnakeSize
        # elif dirs == 1:
        #     xs[0] += SnakeSize
        # elif dirs == 2:
        #     ys[0] -= SnakeSize
        # elif dirs == 3:
        #     xs[0] -= SnakeSize

    pygame.mixer.music.load('naruto.wav')
    pygame.mixer.music.set_endevent(pygame.constants.USEREVENT)
    pygame.mixer.music.play()

    #Controling Menu
    startingMenu = True
    GameStart = False

    #GAME UPDATE
    while not done:
        clock.tick(clockSpeed)

        # Background Color
        screen.fill(BLUE)

        #Keyboard Logic
        pause = True
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
                if e.key == K_EQUALS:
                    clockSpeed += 1
                if e.key == K_MINUS:
                    print("JASLKDJ")
                    clockSpeed -= 1
                if e.key == K_p:
                    dirs = -1

        #Background Music
        if e.type == pygame.constants.USEREVENT:
            pygame.mixer.music.load('naruto.wav')
            pygame.mixer.music.play()

        #If the Snake Collides with itself
        # i = len(xs) - 1
        # if dirs != -1:
        #     while i >= 2:
        #         if collide(xs[0], xs[i], ys[0], ys[i], SnakeSize, SnakeSize, SnakeSize, SnakeSize):
        #             die(screen, score)
        #         i -= 1

        #If the snake Collides with an Apple
        if collide(xs[0], applepos[0], ys[0], applepos[1], SnakeSize, sizeOfApple, SnakeSize, sizeOfApple):
            score += 1
            xs.append(0)
            ys.append(0)
            applepos = (random.randint(0, 590), random.randint(0, 590))

        #Kill snake if it surpasses the boundaries
        if xs[0] < 0 or xs[0] > width_screen - SnakeSize or ys[0] < 0 or ys[0] > height_screen - SnakeSize:
            die(screen, score)

        i = len(xs) - 1

        #Moves the trailing tail to follow the head
        while i >= 1:
            xs[i] = xs[i - move]
            ys[i] = ys[i - move]
            i -= 1

        #INCREASING SNAKE SIZE LOGIC
        snakeLogic()


        #Refreshing the Snake
        for i in range(0, len(xs)):
            screen.blit(img, (xs[i], ys[i]))

        #Refreshing the Apple
        screen.blit(appleimage, applepos)

        #Refreshing the rending of the score
        screenFont = pygame.font.SysFont('Arial', 20)
        scoreText = screenFont.render("Score: " + str(score), True, BLACK)
        t = screenFont.render("Clock Speed: " + str(clockSpeed), True, BLACK)
        #Pixel Location of Score
        screen.blit(scoreText, (10, 10))
        screen.blit(t, (10, 35))

        pygame.display.update()

def main(self):
    SNAKEGAME()

if __name__ == '__main__':
	game = SNAKEGAME()
	game.main()
