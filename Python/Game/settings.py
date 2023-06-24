from os import walk
import pygame , sys, os

map_1 = [
"1111111111111111111111",
"2          02        0",
"2    XX    02      53X",
"234  02    02  4536  0",
"2    02  p 02        0",
"2  34XX34  02  4536  0",
"2    02    02 R E  R 0",
"X34  02  3402  4536  0",
"2    02   R E  R     0",
"2   XXX    4536    XX0",
"1111111111111111111111",
]

map_2 = [
"                       ",
"                       ",
"                       ",
" XX      XXX        XX ",
" XX                    ",
" XXXXX          XX     ",
" XXXXX       XXX       ",
" XXX       XXXX        ",
"       X   XXXX    XX  ",
"     XXX   XXXXX   XX  ",
" XXXXXXX   XXXXX   XX  ",
]



size_plataforma = 64
SCREEN_WIDTH = 1406
SCREEN_HEIGHT = 704
CENTER = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
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

