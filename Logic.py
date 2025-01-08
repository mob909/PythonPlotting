from render import Render

def main(pygame, screen):
    # poll for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False

    # Get variables
    mousePos = pygame.mouse.get_pos()
    Render.drawCircleOnMouse(pygame, screen, mousePos)