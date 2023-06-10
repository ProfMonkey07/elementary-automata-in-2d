import pygame
import random
import time
pygame.init()
screen = pygame.display.set_mode((500, 500))

world = []
ruleset = {"111":0, "110":1, "101":0, "100":1, "011":1, "010":0, "001":1,"000":0}
for i in range(100):
    row = []
    for x in range(100):
        row.append(0)
    world.append(row)

world[50][50] = 1



def getvals(pos, neighbors, world):
    s1 = ""
    for item in neighbors:
        if -1 < pos[0] + item[0] < 100 and -1 < pos[1] + item[1] < 100:
            s1 += str(world[pos[0] + item[0]][pos[1]+item[1]])
        else:
            position = [pos[0] + item[0], pos[1] + item[1]]
            if position[0] < 0:
                position[0] = 99
            elif position[0] >= 100:
                position[0] = 0

            if position[1] < 0:
                position[1] = 99
            elif position[1] >= 100:
                position[1] = 0
            s1 += str(world[position[0]][position[1]])
    return s1

def calcnextstate(position, world):
    side1 = [(-1, -1), (-1, 0), (-1, 1)]
    side2 = [(-1, 1), (0, 1), (1, 1)]
    side3 = [(1, 1), (1, 0), (1, -1)]
    s1 = ""
    s2 = ""
    s3 = ""
    s1 = getvals(position, side1, world)
    s2 = getvals(position, side2, world)
    s3 = getvals(position, side3, world)
    finalS = str(ruleset[s1]) + str(ruleset[s2]) + str(ruleset[s3])
    state = ruleset[finalS]
    return state

def updateworld(world):
    newworld = []
    for i in range(100):
        row = []
        for x in range(100):
            row.append(calcnextstate([i, x], world))
        newworld.append(row)
    return newworld
        

def updatescreen(world, screen):
    screen.fill((0, 0, 0))
    for x in range(100):
        for y in range(100):
            cell = world[x][y]
            if cell == 0:
                pygame.draw.rect(screen, (0, 0, 0), (x*5, y*5, 5, 5))
            elif cell == 1:
                pygame.draw.rect(screen, (255, 255, 255), (x*5, y*5, 5, 5))
    print("flip")
    pygame.display.flip()

while True:
    time.sleep(.000001)
    world = updateworld(world).copy()
    updatescreen(world, screen)