import pygame
from render import Render
from logic import Logic

def main():
    # pygame setup
    pygame.init()
    WINDOW_WIDTH = 1280
    WINDOW_HEIGHT = 720
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    clock = pygame.time.Clock()
    running = True

    while running:
        # Game loop
        if Logic.main(pygame, screen) == False:
            print("Bye bitch")
            running = False
        else:
            pass

        # Render
        Render.main(pygame, screen, WINDOW_WIDTH, WINDOW_HEIGHT, clock)


    pygame.quit()

main()