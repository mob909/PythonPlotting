maxFps = 60
gridPositionList = []

def main(pygame, screen, WINDOW_WIDTH, WINDOW_HEIGHT, clock):
    # get mouse position
    mousePos = pygame.mouse.get_pos()
    
    # fill the screen with a color to wipe away anything from last frame
    screen.fill("white")

    # do the rendering or else (●'◡'●)

    drawGrid(pygame, WINDOW_WIDTH, WINDOW_HEIGHT, screen, 20)
    drawCircleOnMouse(pygame, screen, mousePos)

    # flip front and back buffer
    pygame.display.flip()

    clock.tick(maxFps)  # limits FPS to 60

def drawGrid(pygame, WINDOW_WIDTH, WINDOW_HEIGHT, SCREEN, blockSize):
    global gridPositionList
    for x in range(0, WINDOW_WIDTH, blockSize): # 0 - 1200, intervals of 20
        for y in range(0, WINDOW_HEIGHT, blockSize):
            gridPositionList.append((x, y))
            # print(gridPositionList)
            rect = pygame.Rect(x, y, blockSize, blockSize)
            pygame.draw.rect(SCREEN, "black", rect, 1)

def drawCircleOnMouse(pygame, screen, mousePos):
    closestMousePos = ()

    pygame.draw.circle(screen, "red", mousePos, 6)



# Python program to find element
# closest to given target using two pointers
# This code is contributed by Susobhan Akhuli
import sys
  
def findClosest(tuple: tuple, array: list):
    pass