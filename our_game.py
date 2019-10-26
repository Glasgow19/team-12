#!/usr/bin/python

import numpy as np
import pygame as pg
from pg.locals import *

# Global constants
 
# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


class Player(pg.sprite.Sprite):
    def __init__(self, *args, **kwargs):
        return super().__init__(*args, **kwargs)

        width = 40
        height = 60
        self.image = pg.Surface([width, height])
        self.image.fill(RED)
        self.change_x = 0
        self.change_y = 0

        self.active = True

        self.position = 0
        self.points = 0

    def go_previous():
        self.position = self.position - 1

    def go_next():
        self.position = self.position + 1

    def stop():
        self

class Cell():


class Our_Map():
    def __init__:
        cells = range(32)
        positions_of_cells = dict()

        positions_of_cells[0] = [180,1215]
        positions_of_cells[1] = [303,1215]
        positions_of_cells[2] = [430,1200]
        positions_of_cells[3] = [450,1080]
        positions_of_cells[4] = [437,955]
        positions_of_cells[5] = [314,936]
        positions_of_cells[6] = [188,923]
        positions_of_cells[7] = [140,819]
        positions_of_cells[8] = [140,689]
        positions_of_cells[9] = [140,558]
        positions_of_cells[10] = [173,433]
        positions_of_cells[11] = [298,423]
        positions_of_cells[12] = [406,474]
        positions_of_cells[13] = [416,600]
        positions_of_cells[14] = [474,698]
        positions_of_cells[15] = [600,693]
        positions_of_cells[16] = [661,600]
        positions_of_cells[17] = [661,468]
        positions_of_cells[18] = [671,341]
        positions_of_cells[19] = [792,296]
        positions_of_cells[20] = [896,361]
        positions_of_cells[21] = [896,486]
        positions_of_cells[22] = [896,616]
        positions_of_cells[23] = [896,750]
        positions_of_cells[24] = [896,874]
        positions_of_cells[25] = [896,1000]
        positions_of_cells[26] = [828,1110]
        positions_of_cells[27] = [707,1116]
        positions_of_cells[28] = [645,1217]
        positions_of_cells[29] = [673,1344]
        positions_of_cells[30] = [794,1365]
        positions_of_cells[31] = [923,1358]
        
def main():
    """ Main Program """
    pg.init()
 
    # Set the height and width of the screen
    size = [SCREEN_WIDTH, SCREEN_HEIGHT]
    screen = pg.display.set_mode(size)
 
    pg.display.set_caption("Best game ever!")

    # Set img to background
    background_image = pygame.image.load("pictures/plansza.jpg").convert()
    our_map = Our_map.init()
 
    # Create the player
    player = Player()
 
    active_sprite_list = pg.sprite.Group()
    player.level = current_level
 
    player.rect.x = 340
    player.rect.y = SCREEN_HEIGHT - player.rect.height
    active_sprite_list.add(player)
 
    # Loop until the user clicks the close button.
    done = False
 
    # Used to manage how fast the screen updates
    clock = pg.time.Clock()
 
    # -------- Main Program Loop -----------
    while not done:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                done = True
 
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_LEFT:
                    player.go_previous()
                if event.key == pg.K_RIGHT:
                    player.go_next()
                
            """ DO WE NEED THAT
            if event.type == pg.KEYUP:
                if event.key == pg.K_LEFT and player.change_x < 0:
                    player.stop()
                if event.key == pg.K_RIGHT and player.change_x > 0:
                    player.stop()
            """
 
        # If the player gets near the right side, shift the world left (-x)
        if player.rect.right > SCREEN_WIDTH:
            player.rect.right = SCREEN_WIDTH
 
        # If the player gets near the left side, shift the world right (+x)
        if player.rect.left < 0:
            player.rect.left = 0
 
        # ALL CODE TO DRAW SHOULD GO BELOW THIS COMMENT
        screen.blit(background_image, [0, 0])
        our_map.draw(screen)
        player.draw(screen)
        # ALL CODE TO DRAW SHOULD GO ABOVE THIS COMMENT
 
        # Limit to 60 frames per second
        clock.tick(60)
 
        # Go ahead and update the screen with what we've drawn.
        pg.display.flip()
 
    # Be IDLE friendly. If you forget this line, the program will 'hang'
    # on exit.
    pg.quit()
 
if __name__ == "__main__":
    main()