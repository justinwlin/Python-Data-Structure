def main():
    #480 x 320 Screen
    #W * H

    import pygame, random, sys, os
    # --- Globals ---
    # Colors
    if not True:
        import codecs

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

    # Call this function so the Pygame library can initialize itself
    pygame.init()

    # Set the width and height of each snake segment
    segment_width = 10
    segment_height = 10
    # Margin between each segment
    segment_margin = 3

    # Set initial speed
    x_change = segment_width + segment_margin
    y_change = 0

    #Set up initial direction:
    dir = 1 #0 = up, 1 = right, 2 = down, 3 = left

    #Set initial score
    score = 0

    #Sets up Speed
    speed = 1

    #Set up a clock
    appleClock = 0
    clockTick = 5

    #Event Control Booleans
    oneEvent = True
    threeEvent = True
    fiveEvent = True
    #Font:
    FONT = "Fonts/snakeFont.ttf"

    class Segment(pygame.sprite.Sprite):
        """ Class to represent one segment of the snake. """

        # -- Methods
        # Constructor function
        def __init__(self, x, y):
            # Call the parent's constructor
            super().__init__()

            # Set height, width
            self.image = pygame.Surface([segment_width, segment_height])
            self.image.fill(BLACK)

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
            self.image.fill(RED)

            # Make our top-left corner the passed-in location.
            self.rect = self.image.get_rect()
            self.rect.x = x
            self.rect.y = y


    #Joystick
    # Create an 800x600 sized screen
    height_screen = 320
    width_screen = 480
    screen = pygame.display.set_mode([width_screen, height_screen])

    # Set the title of the window
    pygame.display.set_caption('Snake Example')

    allspriteslist = pygame.sprite.Group()
    snakespritelist = pygame.sprite.Group()
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
        snakespritelist.add(segment)
        allspriteslist.add(segment)

    clock = pygame.time.Clock()
    AppleClock = pygame.time.Clock()
    done = False

    #Setting up Background:
    #Initializing Images
    blueBG = pygame.image.load("Images/bluebackground.jpg").convert()
    purpleBG = pygame.image.load("Images/Purple_BG.png").convert()
    tealBG = pygame.image.load("Images/Teal_BG.png").convert()
    whiteBG = pygame.image.load("Images/White_BG.png").convert()
    introBG = pygame.image.load("Images/Intro_Screen.png").convert()

    BGlist = []
    BGlist.append((purpleBG, "NYU"))
    BGlist.append((blueBG, "Blue"))
    BGlist.append((tealBG, "Teal"))
    BGlist.append((whiteBG, "White"))
    BGindex = 0

    #Music List
    BGmusic = []
    BGmusic.append('Music/pallet_town.wav')
    BGmusic.append('Music/angel.wav')
    BGmusic.append('Music/naruto.wav')
    BGmusicindex = 0

    #Music Name:
    BGmusicname = []
    BGmusicname.append("Pallet Town")
    BGmusicname.append("Angel Beats")
    BGmusicname.append("Naruto")

    #BG Name:
    BGname = []
    BGname.append("Test1")
    BGname.append("Test2")



    #Setting Music
    pygame.mixer.music.load(BGmusic[BGmusicindex])
    pygame.mixer.music.set_endevent(pygame.constants.USEREVENT)
    pygame.mixer.music.play()

    def textToScreen(str):
        basicfont = pygame.font.SysFont(FONT, 48)
        basicfont.render
        text = basicfont.render(str, True, WHITE, BLACK)
        textrect = text.get_rect()
        textrect.centerx = screen.get_rect().centerx
        textrect.centery = screen.get_rect().centery
        screen.blit(text, textrect)

    def createText(str, x, y):
        basicFont = pygame.font.SysFont(FONT, 24)
        basicFont.render
        text = basicFont.render(str, True, BLACK)
        screen.blit(text, (x, y))

    def createTextSize(str, size, x, y):
        basicFont = pygame.font.SysFont(FONT, size)
        basicFont.render
        text = basicFont.render(str, True, BLACK)
        screen.blit(text, (x, y))

    def createTextSizeBG(str, size, background, x, y):
        basicFont = pygame.font.SysFont(FONT, size)
        basicFont.render
        text = basicFont.render(str, True, BLACK, background)
        screen.blit(text, (x, y))

    def createbutton(color, x, y):
        widthButton = 100
        heightButton = 50

        rect = pygame.draw.rect(screen, color, [x,y, widthButton, heightButton])
    #initialize Joystick
    joystickExist = False
    if pygame.joystick.get_count() >= 1:
        joystickExist = True
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
            if joystickExist:
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
            textToScreen("PAUSED")
            pygame.display.update()
            clock.tick(5)

    #Die Function
    def die(screen, score):
        dead = True
        while dead:
            createText("You score was: " + str(score), 10, 270)
            # f = pygame.font.SysFont(FONT, 30)
            # t = f.render('Your score was: ' + str(score), True, (0, 0, 0))
            if joystickExist:
                for k in range(buttons):
                    newbutton = joystick.get_button(k)
                    if newbutton == 1 and (k == 0):
                        pygame.time.wait(100)
                        dead = False
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_c:
                        start = False
                    if event.key == pygame.K_q:
                        pygame.quit()
                        quit()
                    if event.key == pygame.K_c:
                        return

            pygame.display.update()
            clock.tick(20)

    def start():
        start = True
        right = False
        left = True

        colorLeft = bright_green
        colorRight = REDBUTTON

        while start:
            screen.fill(RED)
            screen.blit(introBG, (0, 0))

            createbutton(colorLeft, width_screen / 6, height_screen / 4 * 3)
            createbutton(colorRight, width_screen / 6 * 4, height_screen / 4 * 3)

            createTextSize("Start", 48 ,width_screen / 6 + 10, height_screen / 4 * 3 + 10)
            createTextSize("ABOUT", 40, width_screen / 6 * 4 + 1, height_screen / 4 * 3 + 15)
            #pygame.draw.rect(screen, GREENBUTTON, [width_screen / 6, height_screen / 10 * 7, 100, 50])
            if joystickExist:
                for k in range(buttons):
                    newbutton = joystick.get_button(k)
                    if newbutton == 1 and (k == 0):
                        if left is True:
                            start = False
                    if newbutton == 1 and k == 0:
                        if left is False:
                            pygame.time.delay(400)
                            about()
                for i in range(hats):
                    hat = joystick.get_hat(i)
                    if hat[0] == 1:
                        colorRight = bright_red
                        colorLeft = GREENBUTTON
                        left = False
                        right = True
                    if hat[0] == -1:
                        colorLeft = bright_green
                        colorRight = REDBUTTON
                        left = True
                        right = False

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_c:
                        start = False
                    if event.key == pygame.K_RIGHT:
                        colorRight = bright_red
                        colorLeft = GREENBUTTON
                    if event.key == pygame.K_LEFT:
                        colorLeft = bright_green
                        colorRight = REDBUTTON
                    if event.key == pygame.K_c:
                        start = False

            pygame.display.update()
            clock.tick(20)
    def about():
        event1 = True
        string = "Congrats you just captured your first apple!"
        counter = 0
        slide1 = pygame.image.load("Images/AboutUs.png").convert()
        slideList = [slide1]
        slideIndex = 0

        while event1:
            screen.fill(WHITE)
            if slideIndex == len(slideList):
                return
            screen.blit(slideList[slideIndex], (0, 0))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_c:
                        return
            for k in range(buttons):
                newbutton = joystick.get_button(k)
                #k is the button number
                if newbutton == 1 and (k == 0):
                    print("ESCAPE!")
                    event1 = False
                    pygame.time.delay(400)
            pygame.display.update()
            clock.tick(20)

    def apple_one_event():
        event1 = True
        string = "Congrats you just captured your first apple!"
        counter = 0
        slide1 = pygame.image.load("Images/Apple_One_Slide_One.jpg").convert()
        slide2 = pygame.image.load("Images/Apple_One_Slide_Two.jpg").convert()
        slide3 = pygame.image.load("Images/Apple_One_Slide_Three.jpg").convert()
        slide4 = pygame.image.load("Images/Apple_One_Slide_Four.jpg").convert()
        slideList = [slide1, slide2, slide3, slide4]
        slideIndex = 0

        while event1:
            screen.fill(WHITE)
            if slideIndex == len(slideList):
                return
            screen.blit(slideList[slideIndex], (0, 0))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_c:
                        if slideIndex < len(slideList):
                            slideIndex += 1
                            pygame.time.delay(1)
                        else:
                            event1 = False
            for k in range(buttons):
                newbutton = joystick.get_button(k)
                #k is the button number
                if newbutton == 1 and (k == 0) and score >= 1:
                    slideIndex += 1
                    pygame.time.delay(400)
            pygame.display.update()
            clock.tick(20)

    def apple_three_event():
        event1 = True

        slide1 = pygame.image.load("Images/Apple_Three_Slide_One.jpg").convert()
        slide2 = pygame.image.load("Images/Apple_Three_Slide_Two.jpg").convert()

        slideList = [slide1, slide2]
        slideIndex = 0

        while event1:
            screen.fill(WHITE)
            if slideIndex == len(slideList):
                return
            screen.blit(slideList[slideIndex], (0, 0))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_c:
                        if slideIndex < len(slideList):
                            slideIndex += 1
                            pygame.time.delay(1)
                        else:
                            event1 = False
            for k in range(buttons):
                newbutton = joystick.get_button(k)
                #k is the button number
                if newbutton == 1 and (k == 0) and score >= 1:
                    slideIndex += 1
                    pygame.time.delay(400)
            pygame.display.update()
            clock.tick(20)

    def apple_five_event():
        event1 = True

        slide1 = pygame.image.load("Images/Apple_Five_Slide_One.jpg").convert()
        slide2 = pygame.image.load("Images/Apple_Five_Slide_Two.jpg").convert()

        slideList = [slide1, slide2]
        slideIndex = 0

        while event1:
            screen.fill(WHITE)
            if slideIndex == len(slideList):
                return
            screen.blit(slideList[slideIndex], (0, 0))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_c:
                        if slideIndex < len(slideList):
                            slideIndex += 1
                            pygame.time.delay(1)
                        else:
                            event1 = False
            for k in range(buttons):
                newbutton = joystick.get_button(k)
                #k is the button number
                if newbutton == 1 and (k == 0) and score >= 1:
                    slideIndex += 1
                    pygame.time.delay(400)
            pygame.display.update()
            clock.tick(20)

    gameStart = True
    gameIntro = True
    while not done:
        screen.fill(WHITE)
        screen.blit(BGlist[BGindex][0], (0, 0))
        # Clear screen
        if gameStart:
            start()
            gameStart = False

        #CLOCK
        appleClock += 1
        #if appleClock % (clockTick * 2)== 0:
        if appleClock % 10 == 0:
            appleClock = 0
            x = (random.randint(0, width_screen)) - (segment_width + segment_margin) * i
            y = (random.randint(0, height_screen)) - (segment_width + segment_margin) * i
            apple = APPLE(x, y)
            apple_segments.append(apple)
            allspriteslist.add(apple)
            applespriteslist.add(apple)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

            if joystickExist:
                for i in range(hats):
                    # 0 = up, 1 = right, 2 = down, 3 = left
                    hat = joystick.get_hat(i)
                    if hat[0] == -1 and dir != 1:
                        dir = 3
                        x_change = (segment_width + segment_margin) * -1
                        y_change = 0
                    if hat[0] == 1 and dir != 3:
                        dir = 1
                        x_change = (segment_width + segment_margin)
                        y_change = 0
                    if hat[1] == 1 and dir != 2:
                        dir = 0
                        x_change = 0
                        y_change = (segment_height + segment_margin) * -1
                    if hat[1] == -1 and dir != 0:
                        dir = 2
                        x_change = 0
                        y_change = (segment_height + segment_margin) * 1

                #Joystick Pause

                for k in range(buttons):
                    newbutton = joystick.get_button(k)
                    #k is the button number
                    if newbutton == 1 and (k == 5) and score >= 1:
                        clockTick += 1
                    if newbutton == 1 and k == 4 and score >= 1:
                        clockTick -= 1
                    if newbutton == 1 and (k == 1)and score >= 3:
                        pygame.time.delay(200)
                        if BGindex != len(BGlist) - 1:
                            print(len(BGlist))
                            print(BGindex)
                            BGindex += 1
                        else:
                            BGindex = 0
                    if (newbutton == 1 and (k == 3)):#and score >= 5:
                        pygame.time.delay(200)
                        pygame.mixer.music.stop()
                        if BGmusicindex == len(BGmusic) - 1:
                            BGmusicindex = 0
                        else:
                            BGmusicindex += 1
                        pygame.mixer.music.load(BGmusic[BGmusicindex])
                        pygame.mixer.music.play()

            #------------------------------------
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and dir != 1:
                    dir = 3
                    x_change = (segment_width + segment_margin) * -1
                    y_change = 0
                if event.key == pygame.K_RIGHT and dir != 3:
                    dir = 1
                    x_change = (segment_width + segment_margin)
                    y_change = 0
                if event.key == pygame.K_UP and dir != 2:
                    dir = 0
                    x_change = 0
                    y_change = (segment_height + segment_margin) * -1
                if event.key == pygame.K_DOWN and dir != 0:
                    dir = 2
                    x_change = 0
                    y_change = (segment_height + segment_margin)
                if event.key == pygame.K_p:
                    paused()
                if event.key == pygame.K_q:
                    pygame.quit()
                    quit()

                #FEATURES
                if event.key == pygame.K_EQUALS:
                    clockTick += 1
                if event.key == pygame.K_MINUS:
                    if clockTick != 1:
                        clockTick -= 1
                if event.key == pygame.K_l: #Controls changing the background
                    if BGindex != len(BGlist) - 1:
                        print(len(BGlist))
                        print(BGindex)
                        BGindex += 1
                    else:
                        BGindex = 0
                if event.key == pygame.K_o:
                    pygame.mixer.music.stop()
                    if BGmusicindex == len(BGmusic) -1:
                        BGmusicindex = 0
                    else:
                        BGmusicindex += 1
                    pygame.mixer.music.load(BGmusic[BGmusicindex])
                    pygame.mixer.music.play()
                if event.type == pygame.constants.USEREVENT:
                    pygame.mixer.music.load(BGmusic[BGmusicindex])
                    pygame.mixer.music.play()


        # Get rid of last segment of the snake .pop() command removes last item in list
        old_segment = snake_segments.pop()
        allspriteslist.remove(old_segment)
        snakespritelist.remove(old_segment)

        # Figure out where new segment will be
        x = snake_segments[0].rect.x + x_change
        y = snake_segments[0].rect.y + y_change
        segment = Segment(x, y)

        # Insert new segment into the list
        snake_segments.insert(0, segment)
        allspriteslist.add(segment)
        snakespritelist.add(segment)
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
        #Collision with itself:
        collide2 = False
        head = snake_segments[0]
        for i in range(1, len(snake_segments)):
            if head.rect.x == snake_segments[i].rect.x and head.rect.y == snake_segments[i].rect.y:
                die(screen, score)
                main()
        for i in range(0, len(snake_segments)):
            if head.rect.x > width_screen or head.rect.y > height_screen or head.rect.x < 0 or head.rect.y < 0:
                die(screen,score)
                main()


        # -- Draw everything
        if score == 1 and oneEvent == True:
            apple_one_event()
            oneEvent = False
        if score == 3 and threeEvent == True:
            apple_three_event()
            threeEvent = False
        if score == 5 and fiveEvent == True:
            apple_five_event()
            fiveEvent = False
        #Background Image
        #screen.blit(blueBG, (0, 0))
        #TEXT
        createText("Speed: " + str(clockTick), 5, 0)
        createText("Music: " + str(BGmusicname[BGmusicindex]), 5, 20)
        createText("BG: " + str(BGlist[BGindex][1]), 5, 40)
        createText("Score " + str(score), 5, 60)

        #Drawing Sprites
        allspriteslist.draw(screen)

        # Flip screen
        pygame.display.flip()
        pygame.display.update()
        # Pause
        clock.tick(clockTick)

    pygame.quit()

main()
