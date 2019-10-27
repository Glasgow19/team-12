import pygame

def main():
    # Initialise screen
    pygame.init()
   
    logo = pygame.image.load("boxes.png")
    pygame.display.set_icon(logo)
    pygame.display.set_caption('Risk it!')
  
    screen = pygame.display.set_mode((900, 700))


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
    text = font.render("Would you rather take 100 pounds or choose a box?", 1, (10, 10, 10))
    background.blit(text, (200, 100))

    # Blit everything to the screen
    screen.blit(background, (0, 0))
    screen.blit(logo, (50,100))
    pygame.display.flip()
    # Event loop
    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.blit(background, (0, 0))
        pygame.display.flip()



if __name__ == '__main__': main()