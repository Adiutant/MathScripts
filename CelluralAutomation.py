import pygame
from random import randint

screenY = 600
screenX =600
blockSize = 6
blocknumX = int(screenX/blockSize)
blocknumY = int(screenY/blockSize)

ScreenResolution = (screenX, screenY)
TimeStep = 160
GameField  = [[0] * blocknumX for i in range(blocknumY)]
CellField  = [[0] *blocknumX for i in range(blocknumY)]
pygame.init()
Screen = pygame.display.set_mode(ScreenResolution)

def drawGrid8():
    GameField = [[0] * blocknumX for i in range(blocknumY)]
    for x in range(blocknumX):
        for y in range(blocknumY):
           #
            #if not x+1 == blocknumX and not y+1 == blocknumY:
            if not y + 1>blocknumY-1:
                if CellField[x][y + 1]==1:
                    GameField[x][y] += 1
            if not y-1<0 :
                if CellField[x][y - 1] == 1:
                    GameField[x][y] += 1
            if not x+1>blocknumX-1:
               if CellField[x + 1][y] == 1:
                    GameField[x][y] += 1
            if  not x-1<0:
                if CellField[x - 1][y] == 1:
                    GameField[x][y] += 1
            if not y + 1>blocknumY-1and not x+1>blocknumX-1:
                if CellField[x+1][y + 1]==1:
                    GameField[x][y] += 1
            if not y-1<0 and not x+1>blocknumX-1 :
                if CellField[x+1][y - 1] == 1:
                    GameField[x][y] += 1
            if not x-1<0 and not y + 1>blocknumY-1:
               if CellField[x -1][y+1] == 1:
                    GameField[x][y] += 1
            if  not x-1<0 and not y-1<0 :
                if CellField[x -1 ][y-1] == 1:
                    GameField[x][y] += 1
    for x in range(blocknumX):
        for y in range(blocknumY):
            Rect = pygame.Rect(x*blockSize, y*blockSize, blockSize, blockSize)
            if GameField[x][y]>3 or GameField[x][y]<2:
                pygame.draw.rect(Screen, (200, 200, 200), Rect, 1)
                CellField[x][y] = 0
            if GameField[x][y] == 3:
                pygame.draw.rect(Screen, (0,255, 0), Rect, 0)
                #image = pygame.Surface((blockSize,blockSize))
               # image.fill((255,0,0),Rect)
                CellField[x][y] = 1
            if GameField[x][y] == 2 and CellField[x][y]==1:
                pygame.draw.rect(Screen, (0,255,0), Rect, 0)
                #image = pygame.Surface((blockSize,blockSize))
                #image.fill((255,0,0),Rect)
                CellField[x][y] = 1

def drawGrid():
    #GameField = [[0] * blocknumX for i in range(blocknumY)]
    for x in range(blocknumX):
        for y in range(blocknumY):
           #
            #if not x+1 == blocknumX and not y+1 == blocknumY:

            if not y + 1>blocknumY-1:
                if CellField[x][y + 1]==1:
                    GameField[x][y] += 1
            if not y-1<0 :
                if CellField[x][y - 1] == 1:
                    GameField[x][y] += 1
            if not x+1>blocknumX-1:
               if CellField[x + 1][y] == 1:
                    GameField[x][y] += 1
            if  not x-1<0:
                if CellField[x - 1][y] == 1:
                    GameField[x][y] += 1
    for x in range(blocknumX):
        for y in range(blocknumY):
            Rect = pygame.Rect(x*blockSize, y*blockSize, blockSize, blockSize)
            if GameField[x][y]>3 or GameField[x][y]<2:
                pygame.draw.rect(Screen, (0, 0, 0), Rect, 1)
                CellField[x][y]=0
            if GameField[x][y] == 3:
                pygame.draw.rect(Screen, (0,255, 0), Rect, 0)
                #image = pygame.Surface((blockSize,blockSize))
               # image.fill((255,0,0),Rect)
                CellField[x][y] = 1
            if GameField[x][y] == 2 and CellField[x][y]==1:
                pygame.draw.rect(Screen, (0,255,0), Rect, 0)
                #image = pygame.Surface((blockSize,blockSize))
                #image.fill((255,0,0),Rect)
                CellField[x][y] = 1

NextMove = pygame.time.get_ticks() + TimeStep
GameRunning = True


def randomSpread():
    for x in range(blocknumX):
        for y in range(blocknumY):
            CellField[x][y] = randint(0,1)
#randomSpread()
CellField[5][5]=1
CellField[5][6]=1
CellField[5][7]=1
while GameRunning:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            GameRunning = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                SpacePressed = True
                randomSpread()
                while SpacePressed:
                    for event2 in pygame.event.get():
                        if event2.type == pygame.KEYDOWN:
                            if event2.key == pygame.K_SPACE:
                                SpacePressed = False
    
    CurrentTime = pygame.time.get_ticks()
    if CurrentTime >= NextMove:
        Screen.fill((220, 220, 220))
        drawGrid8()
        pygame.display.update()
        NextMove = pygame.time.get_ticks() + TimeStep
