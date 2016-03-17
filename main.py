import random
import time
import pygame
import math
import os
import sys
from AI_engine import *

display_width = 240
display_height = 320

black = (0,0,0)
white = (215,215,215)
red = (200,0,0)
green = (0,200,0)
blue = (0,0,255)
bright_red = (255, 0, 0)
bright_green = (0, 255, 0)

human_plays_first = bool(random.getrandbits(1))

paddle_y = 200
player=1
score=0
round=0

winnings = "NO-ONE"
grid = [["0","0","0"],
        ["0","0","0"],
        ["0","0","0"]]

possible_wins = ["100010001","001010100","100100100","010010010","001001001","111000000","000111000","000000111"]
pos_win_copy = possible_wins

os.environ["SDL_FBDEV"] = "/dev/fb1"
os.environ["SDL_MOUSEDEV"] = "/dev/input/touchscreen"
os.environ["SDL_MOUSEDRV"] = "TSLIB"

pygame.init()

screen = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Tic Tac Toe') # Title of windows
clock = pygame.time.Clock() # Built In Clock


class Platform:
    x = 0
    y = 0
    length = 0
    width = 0

    def __init__(self, x, y, length, width):
        self.x = x
        self.y = y
        self.length = length
        self.width = width

    def draw(self):
        pygame.draw.rect(screen, white, pygame.Rect((self.x,self.y),(self.length,self.width)))

def displayMessage(text, size, x, y):
    font = pygame.font.SysFont(None, size)
    image = font.render(text, True, blue)
    screen.blit(image,(x, y))

##If windows, set UNC homepath
if sys.platform == 'win32':
    homePath = str(sys.modules[__name__]).split("'")[3].split("'")[0].rsplit("\\",1)[0].replace("\\\\","\\")
else:
    homePath = ""

print(homePath)

noughts=pygame.image.load(homePath + "noughts.jpg")
noughts=pygame.transform.scale(noughts,(60,60))
crosses=pygame.image.load(homePath + "crosses.jpg")
crosses=pygame.transform.scale(crosses,(60,60))

noughtsize = pygame.Rect(0,0,100,160)
crosssize = pygame.Rect(0,0,130,130)

floor = Platform(0,290,240, 5)
column1 = Platform(80,70,7,300)
column2 = Platform(160,70,7,300)
row1 = Platform(0,150,300,7)
row2 = Platform(0,240,300,7)

## START OF GAME LOGICS ==============================================================================

def set_Move(x,y,p):
    grid[x-1][y-1] = str(p)
    print(grid)

def check_win(player):
    wins = False
    if player == 1:
        for i in range(0,8):
            itm = possible_wins[i]
            if (itm == get_grid(player).replace("X","0")):
                wins = True
    if player == 2:
        for i in range(0,8):
            itm = possible_wins[i]
            if (itm == get_grid(player).replace("X","0")):
                wins = True
    return wins

def set_pawn(player, pointx):
    hasSet = True
    p = noughts
    if player == 2:
        p = noughts
    else:
        p = crosses

    if pointx == "Top left" and grid[1-1][1-1]=="0":
        screen.blit(p, (10,80))
        grid[1-1][1-1] = str(player)
    elif pointx == ("Middle left") and grid[2-1][1-1] == "0":
        screen.blit(p, (10,170))
        grid[2-1][1-1] = str(player)
    elif pointx == ("Bottom left") and grid[3-1][1-1] == "0":
        screen.blit(p, (10,250))
        grid[3-1][1-1] = str(player)
    elif pointx == ("Middle top") and grid[1-1][2-1] == "0":
        screen.blit(p, (95,80))
        grid[1-1][2-1] = str(player)
    elif pointx == ("Middle middle") and grid[2-1][2-1] == "0":
        screen.blit(p, (95,170))
        grid[2-1][2-1] = str(player)
    elif pointx == ("Middle bottom") and grid[3-1][2-1] == "0":
        screen.blit(p, (96,250))
        grid[3-1][2-1] = str(player)
    elif pointx == ("Top right") and grid[1-1][3-1] == "0":
        screen.blit(p,(175,80))
        grid[1-1][3-1] = str(player)
    elif pointx == ("Middle right") and grid[2-1][3-1] == "0":
        screen.blit(p, (176,167))
        grid[2-1][3-1] = str(player)
    elif pointx == ("Bottom right") and grid[3-1][3-1] == "0":
        screen.blit(p, (175,254))
        grid[3-1][3-1] = str(player)
    else:
        hasSet = False
    return hasSet


def get_grid(player = 0):
    current_grid = str(grid).replace(",","").replace("[","").replace("]","").replace("'","").replace(" ","")
    if player == 1:
        current_grid = current_grid.replace(str(2),"X").replace(str(player),"1")
    elif player == 2:
        current_grid = current_grid.replace(str(1),"X").replace(str(player),"1")
    else:
        current_grid = current_grid
    return current_grid

## Checking if human should play first. If not, AI makes first move ==============================================
if (human_plays_first == False):
    print("AI is playing first this round . . .")
    play()
else:
    print("HUMAN is playing first this round . . .")

while True:
    mx,my = pygame.mouse.get_pos() # this is to obtain mouse x and y position
    
    # Check if grid is full
    if get_grid().find("0") == -1:
        winnings = "NOBODY"

    # Check if anyone has won the game
    if winnings != "NO-ONE":
        print(str(winnings) + " has won!")
        break

    for event in pygame.event.get(): # Gets any events that happens

        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        if event.type==pygame.mouse:
            if pygame.MOUSEBUTTONDOWN:
                pygame.draw.rect(screen, blue, pygame.Rect((mx,my),(30,30)))

        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_q:
                pygame.quit()
                quit()

        if player==1:
            if event.type==pygame.MOUSEBUTTONDOWN: #this is what happens when you click in the different part on the grid
                if mx >0 and mx < 76 and my> 70 and my <150:
                    set_pawn(player, ("Top left"))
                if mx >0 and mx < 76 and my> 156 and my <240:
                    set_pawn(player, "Middle left")
                if mx >0 and mx < 76 and my> 247 and my <318:
                    set_pawn(player, ("Bottom left"))
                if mx >87 and mx < 159 and my> 70 and my <150:
                    set_pawn(player, "Middle top")
                if mx >87 and mx < 159 and my> 156 and my <240:
                    set_pawn(player, "Middle middle")
                if mx >87 and mx < 159 and my> 247 and my <318:
                    set_pawn(player, "Middle bottom")
                if mx >165 and mx < 239 and my> 70 and my <150:
                    set_pawn(player,("Top right"))
                if mx >165 and mx < 239 and my> 156 and my <240:
                    set_pawn(player, ("Middle right"))
                if mx >165 and mx < 239 and my> 247 and my <318:
                    set_pawn(player, ("Bottom right"))

        if player==2:
            if event.type==pygame.MOUSEBUTTONDOWN: #this is what happens when you click in the different part on the grid
                if mx >0 and mx < 76 and my> 70 and my <150:
                    set_pawn(player, ("Top left"))
                if mx >0 and mx < 76 and my> 156 and my <240:
                    set_pawn(player, "Middle left")
                if mx >0 and mx < 76 and my> 247 and my <318:
                    set_pawn(player, ("Bottom left"))
                if mx >87 and mx < 159 and my> 70 and my <150:
                    set_pawn(player, "Middle top")
                if mx >87 and mx < 159 and my> 156 and my <240:
                    set_pawn(player, "Middle middle")
                if mx >87 and mx < 159 and my> 247 and my <318:
                    set_pawn(player, "Middle bottom")
                if mx >165 and mx < 239 and my> 70 and my <150:
                    set_pawn(player,("Top right"))
                if mx >165 and mx < 239 and my> 156 and my <240:
                    set_pawn(player, ("Middle right"))
                if mx >165 and mx < 239 and my> 247 and my <318:
                    set_pawn(player, ("Bottom right"))

        if event.type==pygame.MOUSEBUTTONDOWN:
            if player == 1:
                play()
            else:
                check_if_won(1)
                player = 1

    #messages on top
    displayMessage(". . .", 20, 0, 0)
    displayMessage("1 Player", 25, 85, 0)
    displayMessage("Tic-Tac-Toe", 26, 75, 20)

    #floor.draw()
    column1.draw()
    column2.draw()
    row1.draw()
    row2.draw()

    pygame.display.update()
    #Refreshes the screen with a black rectangle
    #The draw.rect is the background
    pygame.draw.rect(screen, red, pygame.Rect((0,0),(320,35)))

while True:
    #messages on top
    displayMessage(str(winnings), 25, 80, 0)
    displayMessage("    WON    ", 26, 80, 20)

    #floor.draw()
    column1.draw()
    column2.draw()
    row1.draw()
    row2.draw()

    pygame.display.update()
    #Refreshes the screen with a black rectangle
    #The draw.rect is the background
    pygame.draw.rect(screen, red, pygame.Rect((0,0),(320,35)))

    for event in pygame.event.get(): # Gets any events that happens

        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        if event.type==pygame.mouse:
            if pygame.MOUSEBUTTONDOWN:
                pygame.draw.rect(screen, blue, pygame.Rect((mx,my),(30,30)))

        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_q:
                pygame.quit()
                quit()