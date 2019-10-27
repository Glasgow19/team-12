import sys, random
import pygame as pg

def main():

    pg.init()


    size = width, height = 900, 700
    speed = [0, 2]

    screen = pg.display.set_mode(size)

    background = pg.Surface(screen.get_size())
    background = background.convert()
    background.fill((177,149,160))

    font = pg.font.Font(None, 36)
    text = font.render("Choose one of the options and flip the coin ten times.", 1, (10, 10, 10))
    textpos = text.get_rect()
    textpos = (120, 20)
    background.blit(text, textpos)

    font = pg.font.Font(None, 36)
    quit = font.render("Quit?", 1, (10, 10, 10))
    quitpos = quit.get_rect(center =(45, height-20))
    background.blit(quit, quitpos)

    flip_button = pg.draw.rect(background, (200,2,2), (435, 50, 70, 45))
    flip_buttonrect = flip_button.move(background.get_rect().centerx, 60)
    pg.display.update()

    font = pg.font.Font(None, 36)
    flip = font.render("Flip", 1, (10, 10, 10))
    flippos = (background.get_rect().centerx, 60)
    background.blit(flip, flippos)


    image = pg.image.load("pictures/coin.png")
    coin = pg.transform.scale(image, (300, 200))
    coin.set_colorkey((255,255,255))
    coinrect = coin.get_rect(center =(width/2, height*3/4))
    background.blit(coin, coinrect)
    screen.blit(background,(0,0))
    pg.display.update()

    def flip_coin(screen, coinrect, coin, image):

        pg.draw.rect(background, (177,149,160), (50, 100, 600, 500))

        r = random.randint(0,1)
        for x in range (200):
            coinrect = coinrect.move(0,-2)
            coin = pg.transform.scale(image, (300, 200))
            screen.blit(pg.transform.rotate(coin,x), coinrect)
            pg.display.update()
            pg.time.delay(10)

            screen.blit(background,(0,0))
            pg.display.flip()

        for x in range (200):
            coinrect = coinrect.move(0,2)
            coin = pg.transform.scale(image, (300, 200))
            screen.blit(pg.transform.rotate(coin,200+x), coinrect)
            pg.display.update()
            pg.time.delay(10)

            screen.blit(background,(0,0))
            pg.display.flip()

        if r==1:
            result = "head"
        else:
            result = "tail"

        font = pg.font.Font(None, 36)
        result = font.render(result, 1, (10, 10, 10))
        resultpos = result.get_rect(center =(width/2, height*7/8))
        background.blit(result, resultpos)
        screen.blit(background,(0,0))

        coinrect = coin.get_rect(center =(width/2, height*3/4))
        background.blit(coin, coinrect)
        screen.blit(background,(0,0))
        pg.display.update()


    while(1):
        for event in pg.event.get():
            if event.type == pg.QUIT: sys.exit()
        pg.time.delay(10)

        mouse = pg.mouse.get_pos()

        if 435+70 > mouse[0] > 435 and 50+45 > mouse[1] > 50:
            flip_coin(screen, coinrect, coin, image)

    #    pg.display.update()
    #flip_coin(screen, coinrect, coin, image)
    #pg.display.update()

    while 1:
        for event in pg.event.get():
            if event.type == pg.QUIT: sys.exit()

if __name__ == "__main__":
    main()
