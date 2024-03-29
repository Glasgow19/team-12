import sys, pygame, random

heads = 0
total = 0

def game_coin_flip():
    pygame.init()


    size = width, height = 900, 700
    speed = [0, 2]

    screen = pygame.display.set_mode(size)

    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((177,149,160))

    font = pygame.font.Font(None, 36)
    text = font.render("How many flips will you need to get three heads?", 1, (10, 10, 10))
    textpos = text.get_rect()
    textpos = (120, 20)
    background.blit(text, textpos)

    font = pygame.font.Font(None, 36)
    text1 = font.render("No of heads:"+str(heads), 1, (10, 10, 10))
    textpos1 = text.get_rect()
    textpos1 = (10, 180)
    background.blit(text1, textpos1)

    font = pygame.font.Font(None, 36)
    text2 = font.render("Total no of throws:"+ str(total), 1, (10, 10, 10))
    textpos2 = text.get_rect()
    textpos2 = (10, 210)
    background.blit(text2, textpos2)


    quit_button = pygame.draw.rect(background, (200,2,2), (5, height-50, 80, 40))
    quit_buttonrect = quit_button.move(background.get_rect().centerx, 60)
    pygame.display.update()

    font = pygame.font.Font(None, 36)
    quit = font.render("Quit?", 1, (10, 10, 10))
    quitpos = quit.get_rect(center =(45, height-30))
    background.blit(quit, quitpos)

    flip_button = pygame.draw.rect(background, (200,2,2), (435, 50, 70, 45))
    flip_buttonrect = flip_button.move(background.get_rect().centerx, 60)
    pygame.display.update()

    font = pygame.font.Font(None, 36)
    flip = font.render("Flip", 1, (10, 10, 10))
    flippos = (background.get_rect().centerx, 60)
    background.blit(flip, flippos)


    image = pygame.image.load("pictures/coin.png")
    coin = pygame.transform.scale(image, (300, 200))
    coin.set_colorkey((255,255,255))
    coinrect = coin.get_rect(center =(width/2, height*3/4))
    background.blit(coin, coinrect)
    screen.blit(background,(0,0))
    pygame.display.update()

    def flip_coin(screen, coinrect, coin, image):

        pygame.draw.rect(background, (177,149,160), (330, 400, 250, 250))

        r = random.randint(0,1)
        for x in range (200):
            coinrect = coinrect.move(0,-2)
            coin = pygame.transform.scale(image, (300, 200))
            screen.blit(pygame.transform.rotate(coin,x), coinrect)
            pygame.display.update()
            pygame.time.delay(8)

            screen.blit(background,(0,0))
            pygame.display.flip()

        for x in range (200):
            coinrect = coinrect.move(0,2)
            coin = pygame.transform.scale(image, (300, 200))
            screen.blit(pygame.transform.rotate(coin,200+x), coinrect)
            pygame.display.update()
            pygame.time.delay(8)

            screen.blit(background,(0,0))
            pygame.display.flip()

        if r==1:
            result = "head"
            global heads
            heads += 1
        else:
            result = "tail"

        global total
        total += 1


        pygame.draw.rect(background, (177,149,160), (157, 150, 50, 50))
        pygame.draw.rect(background, (177,149,160), (230, 210, 50, 50))

        font = pygame.font.Font(None, 36)
        text1 = font.render("No of heads: "+str(heads), 1, (10, 10, 10))
        textpos1 = text.get_rect()
        textpos1 = (10, 180)
        background.blit(text1, textpos1)

        font = pygame.font.Font(None, 36)
        text2 = font.render("Total no of throws: "+ str(total), 1, (10, 10, 10))
        textpos2 = text.get_rect()
        textpos2 = (10, 210)
        background.blit(text2, textpos2)


        font = pygame.font.Font(None, 36)
        result = font.render(result, 1, (10, 10, 10))
        resultpos = result.get_rect(center =(width/2, height*7/8))
        background.blit(result, resultpos)
        screen.blit(background,(0,0))

        coinrect = coin.get_rect(center =(width/2, height*3/4))
        background.blit(coin, coinrect)
        screen.blit(background,(0,0))
        pygame.display.update()
        pygame.time.delay(1200)


    while(1):
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
        pygame.time.delay(10)

        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        if 435+70 > mouse[0] > 435 and 50+45 > mouse[1] > 50 and click[0] == 1:
            flip_coin(screen, coinrect, coin, image)


        if 5+80 > mouse[0] > 5 and height-50+40 > mouse[1] > height-50 and click[0] == 1:
            return

game_coin_flip()
