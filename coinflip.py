import sys, pygame, random

pygame.init()


size = width, height = 900, 700
speed = [0, 2]

screen = pygame.display.set_mode(size)

background = pygame.Surface(screen.get_size())
background = background.convert()
background.fill((177,149,160))

font = pygame.font.Font(None, 36)
text = font.render("Choose one of the options and flip the coin ten times.", 1, (10, 10, 10))
textpos = text.get_rect()
textpos = (120, 20)
background.blit(text, textpos)

font = pygame.font.Font(None, 36)
quit = font.render("Quit?", 1, (10, 10, 10))
quitpos = quit.get_rect(center =(45, height-20))
background.blit(quit, quitpos)

font = pygame.font.Font(None, 36)
flip = font.render("Flip", 1, (10, 10, 10))
flippos = (background.get_rect().centerx, 60)
background.blit(flip, flippos)


image = pygame.image.load("pictures/coin.png")
coin = pygame.transform.scale(image, (300, 200))
coin.set_colorkey((255,255,255))
coinrect = coin.get_rect(center =(width/2, height*3/4))
screen.blit(background,(0,0))

def flip_coin(screen, coinrect, coin, image):
    r = random.randint(0,1)
    for x in range (200):
        coinrect = coinrect.move(0,-2)
        coin = pygame.transform.scale(image, (300, 200))
        screen.blit(pygame.transform.rotate(coin,x), coinrect)
        pygame.display.update()
        pygame.time.delay(10)

        screen.blit(background,(0,0))
        pygame.display.flip()

    for x in range (200):
        coinrect = coinrect.move(0,2)
        coin = pygame.transform.scale(image, (300, 200))
        screen.blit(pygame.transform.rotate(coin,200+x), coinrect)
        pygame.display.update()
        pygame.time.delay(10)

        screen.blit(background,(0,0))
        pygame.display.flip()

    if r==1:
        result = "head"
    else:
        result = "tail"

    font = pygame.font.Font(None, 36)
    result = font.render(result, 1, (10, 10, 10))
    resultpos = result.get_rect(center =(width/2, height*3/4))
    background.blit(result, resultpos)
    screen.blit(background,(0,0))


flip_coin(screen, coinrect, coin, image)

pygame.display.update()

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
