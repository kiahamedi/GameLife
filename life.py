import os
import time
import sys
import random


class Universe(object):

    def __init__(self, w, h):
        self.w = w
        self.h = h
        self.contents = {}
        self.generation = 0
        for y in range(self.h):
            for x in range(self.w):
                self.contents[x, y] = 0


    # init world with random data
    def randomize(self):
        out = {}
        self.generation = 1
        for y in range(self.h):
            for x in range(self.w):
                c = random.randint(0, 1)
                if c == 0:
                    out[x, y] = 1
                else:
                    out[x, y] = 0

        self.contents = out

    # draw world
    def getString(self):
        drawWorld = ""
        for y in range(self.h):
            for x in range(self.w):
                c = self.contents[x, y]
                if c == 0:
                    drawWorld += " "
                elif c == 1:
                    drawWorld += u"\u2588"
            drawWorld += "\n"
        return drawWorld
    

    # Calculate conditions for neighbours
    def calculate(self):
        newWorld = {}
        for y in range(self.h):
            for x in range(self.w):
                c = self.contents[x, y]
                u, d, l, r ,ur ,ul, dr, dl = self.getNeighbours(x, y)
                n = [u, d, l, r ,ur ,ul, dr, dl]
                n = self.countNeighbours(n)
                if c == 1:
                    if n > 3:
                        newWorld[x, y] = 0
                    elif n < 2:
                        newWorld[x, y] = 0
                    elif n == 2 or n == 3:
                        newWorld[x, y] = 1
                elif c == 0:
                    if n == 3:
                        newWorld[x, y] = 1
                    else:
                        newWorld[x, y] = 0
        
        self.contents = newWorld



    # find all neighbours in the world
    def getNeighbours(self, x, y):
        c = self.contents
        try: u = c[x, y-1]
        except: u = 0
        try: d = c[x, y+1]
        except: d = 0
        try: l = c[x-1, y]
        except: l = 0
        try: r = c[x+1, y]
        except: r = 0
        try: ur = c[x+1, y-1]
        except: ur = 0
        try: ul = c[x-1, y-1]
        except: ul = 0
        try: dr = c[x+1, y+1]
        except: dr = 0
        try: dl = c[x-1, y+1]
        except: dl = 0
        return u, d, l, r ,ur ,ul, dr, dl

    # count number of neighbours
    def countNeighbours(self, n):
        count = 0
        for i in range(len(n)):
            c = n[i]
            if c == 1:
                count += 1
        return count

# clear world for new generation : nt for windows and else for other like linux and mac
def cls():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")



# init world
WIDTH = 120
HEIGHT = 90
DELAY = 0.15

universe = Universe(WIDTH , HEIGHT)
universe.randomize()

while True:
    universe.calculate()
    cls()
    print(universe.getString())
    time.sleep(DELAY)
