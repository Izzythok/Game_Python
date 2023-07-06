import pygame , sys, os
import random

map_0 = [
"1111111111111111111111",
"2         N02    p   W0",
"2 M  XX   XX2 R  E R3X",
"X34  02    02  4536  0",
"2   M02 M  02 R E  RM0",
"2  34XX34  02  4536  0",
"2 M  02   M02 R E  RM0",
"X34  02  34XX  4536  0",
"2   M02   R E  R    N0",
"2   XXX  E 4536    XX0",
"1111111111111111111111",
]

map_1 = [    
"111111111111 11111 111",
"X     I         p    WX",
"X8889 I   DAAAAAAAAAAAX",
"X     I               X",
"X 7888IAAAAAAAAAAAF   X",
"X     I               X",
"X8889 I   DAAAAAAAAAAAX",
"X     I               X",
"X 7888IAAAAAAAAAAAF   X",
"X                     X",
"JJJJJJJJJJJJJJJJJJJJJJ",
]

map_2 = [    
"1111111111111111111111",
"X                    X",
"X                    X",
"X                    X",
"X                    X",
"X                    X",
"X               B    X",
"X                    X",
"X                    X",
"X p                  X",
"8888888888888888888888",
]

size_plataforma = 64
SCREEN_WIDTH = 1406
SCREEN_HEIGHT = 704
CENTER = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
CLOSE = (SCREEN_WIDTH // 0.5, SCREEN_HEIGHT // 0.5)
FPS = 30
SPEED = 10
SPEED_ENEMY = 8

RED = (255,0,0)
BLUE = (0,0,255)
GREEN = (0,255,0)
BLACK = (0,0,0)
WHITE = (255,255,255)
MAGENTA = (255,0,255)
YELLOW = (255,255,0)
CYAN = (0,255,255)

