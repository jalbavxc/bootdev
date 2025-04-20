#this allows us to use code from
#the open_source pygame library
#throughout this file
import pygame
from constants import *


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH} \nScreen height: {SCREEN_HEIGHT}") 
    #Infinite game loop
    while True:
          for event in pygame.event.get():
                #if the user clicks the close button
                if event.type == pygame.QUIT:
                #Exit the game
                   return
          #Fill the screen with black block
          screen.fill((0,0,0)) #The RGB for black color
          #Update the display
          pygame.display.flip()

if __name__ == "__main__":
        main()