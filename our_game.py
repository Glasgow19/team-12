#!/usr/bin/python
import coinflip2

import numpy as np
import pygame as pg
from pygame.locals import *
import os, sys, random
from subprocess import call
from subprocess import Popen

# Global constants
 
# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Screen dimensions
SCREEN_WIDTH = 700
SCREEN_HEIGHT = 900

# Challenges from girls
challenges = []
# Please here upload couple of mini-games or challenges.
challenges.append("nothing.py")
challenges.append("coinflip2.py")
for j in range(30):
    challenges.append("nothing.py")

class Background(pg.sprite.Sprite):
    def __init__(self, image_file, location):
        pg.sprite.Sprite.__init__(self)  #call Sprite initializer
        self.image = pg.image.load(image_file)
        self.image = pg.transform.scale(self.image, (SCREEN_WIDTH, SCREEN_HEIGHT))
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location

class Cell:
    def __init__(self, i):
        self.challenge = challenges[i]
        self.color = RED

    def playTheGame(self, player):
        # player.points = player.points + self.challenge.reward
        pass


class Our_Map():
    def __init__(self):
        self.number_of_cells = 32
        self.cells = []
        for i in range(self.number_of_cells):
            self.cells.append(Cell(i))


        self.positions_of_cells = dict()
        self.positions_of_cells[0] = [100,705]
        self.positions_of_cells[1] = [185,710]
        self.positions_of_cells[2] = [260,710]
        self.positions_of_cells[3] = [283,642]
        self.positions_of_cells[4] = [287,557]
        self.positions_of_cells[5] = [314,936]
        self.positions_of_cells[6] = [188,923]
        self.positions_of_cells[7] = [140,819]
        self.positions_of_cells[8] = [140,689]
        self.positions_of_cells[9] = [140,558]
        self.positions_of_cells[10] = [173,433]
        self.positions_of_cells[11] = [298,423]
        self.positions_of_cells[12] = [406,474]
        self.positions_of_cells[13] = [416,600]
        self.positions_of_cells[14] = [474,698]
        self.positions_of_cells[15] = [600,693]
        self.positions_of_cells[16] = [661,600]
        self.positions_of_cells[17] = [661,468]
        self.positions_of_cells[18] = [671,341]
        self.positions_of_cells[19] = [792,296]
        self.positions_of_cells[20] = [896,361]
        self.positions_of_cells[21] = [896,486]
        self.positions_of_cells[22] = [896,616]
        self.positions_of_cells[23] = [896,750]
        self.positions_of_cells[24] = [896,874]
        self.positions_of_cells[25] = [896,1000]
        self.positions_of_cells[26] = [828,1110]
        self.positions_of_cells[27] = [707,1116]
        self.positions_of_cells[28] = [645,1217]
        self.positions_of_cells[29] = [673,1344]
        self.positions_of_cells[30] = [794,1365]
        self.positions_of_cells[31] = [923,1358]

    # This may be useful for later if we have scoreboard etc.
    #def draw(self, screen):
        #return
        #do nothing
  
class Player(pg.sprite.Sprite):
    def __init__(self, *args, **kwargs):
        super().__init__()

        width = 30
        height = 30
        self.image = pg.Surface([width, height])
        self.image.fill(RED)
        self.change_x = 0
        self.change_y = 0

        self.active = True

        self.position = 0
        self.points = 0

        self.rect = self.image.get_rect()
        self.rect.center = [180,1215]

        self.explored = []

    def go_previous(self, our_map):
        self.position = self.position - 1
        self.update_position(our_map)

    def go_next(self, our_map):
        self.position = self.position + 1
        if self.position not in self.explored:
            if challenges[self.position] != "nothing.py":
                '''open the game'''
                # exec(open(challenges[self.position]).read())
                Popen('python ' + challenges[self.position])
        self.update_position(our_map)

    def update_position(self, our_map):
        self.rect.center = (our_map.positions_of_cells[self.position][0], our_map.positions_of_cells[self.position][1])
        self.explored.append(self.position)

    def draw(self, screen):
        """ HOW TO DRAW PLAYER?"""
        pg.draw.rect(screen, RED, self.rect)  

        
def main():
    """ Main Program """
    pg.init()

    # Global Map
    our_map = Our_Map() 
 
    # Set the height and width of the screen
    size = [SCREEN_WIDTH, SCREEN_HEIGHT]
    screen = pg.display.set_mode(size)
 
    pg.display.set_caption("Best game ever!")

    # Set img to background
    background = Background("pictures/plansza.jpg", [0,0])
 
    # Create the player
    player = Player()
 
    player.rect.x = our_map.positions_of_cells[0][0]
    player.rect.y = our_map.positions_of_cells[0][1]
 
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
                    player.go_previous(our_map)
                if event.key == pg.K_RIGHT:
                    player.go_next(our_map)
                
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
        screen.blit(background.image, background.rect)
        # our_map.draw(screen) # called when implemented
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