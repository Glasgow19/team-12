import pygame

def main():
    # Initialise screen
    pygame.init()
    pygame.display.set_caption('Risk it!')
    screen = pygame.display.set_mode((1000, 700))


    # Fill background
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((250, 250, 250))

    # Display some text
    font = pygame.font.Font(None, 36)
    text = font.render("There are 3 boxes, each with a set amount of money: either 0, 500, or 1000 pounds!", 1, (10, 10, 10))
    textpos = text.get_rect()
    textpos.centerx = background.get_rect().centerx
    background.blit(text, textpos)

    font = pygame.font.Font(None, 30)
    text = font.render("Would you rather get 100 pounds or choose a box?", 1, (10, 10, 10))
    background.blit(text, (200, 100))

    font = pygame.font.Font(None, 30)
    text = font.render("Choose a box!", 1, (10, 10, 10))
    background.blit(text, (100, 400))
    font = pygame.font.Font(None, 30)
    text = font.render("Take the 100 pounds!", 1, (10, 10, 10))
    background.blit(text, (600, 400))

    # Blit everything to the screen
    screen.blit(background, (0, 0))

    # Event loop
    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.blit(background, (0, 0))
        green = ((50,205,50))
        pygame.draw.rect(screen, green, (125,500,100,50))
        red = ((250, 0, 0))
        pygame.draw.rect(screen, red, (650,500,100,50))
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if 125+100 > mouse[0] > 125 and 500 + 50 > mouse[1] >500:
            if click[0] == 1:
                font = pygame.font.SysFont("comicsansms", 30)
                text = font.render("You are very risky :)", 1, (10, 10, 10))
                result = 1
                background.blit(text, (300, 200))
        elif 650+100 > mouse[0] > 650 and 500 + 50 > mouse[1] >500:
            if click[0] == 1:
                font = pygame.font.SysFont("comicsansms", 30)
                text = font.render("You're not very risky :(", 1, (10, 10, 10))
                result = 0
                background.blit(text, (300, 200))
        pygame.display.update()
        pygame.display.flip()


if __name__ == '__main__': main()