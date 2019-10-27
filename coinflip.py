import sys, pygame
pygame.init()

size = width, height = 900, 700
speed = [0, 2]

screen = pygame.display.set_mode(size)

background = pygame.Surface(screen.get_size())
background = background.convert()
background.fill((177,149,160))

font = pygame.font.Font(None, 36)
text = font.render("Flip the coin.", 1, (10, 10, 10))
textpos = text.get_rect()
textpos.centerx = background.get_rect().centerx
background.blit(text, textpos)

image = pygame.image.load("pictures/coin.png")
coin = pygame.transform.scale(image, (300, 200))
coin.set_colorkey((255,255,255))
coinrect = coin.get_rect(center =(width/2, height*3/4))
screen.blit(background,(0,0))

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

screen.blit(coin, coinrect)
pygame.display.update()

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
