from os import walk
import pygame , sys, os

map_1 = [
"1111111111111111111111",
"2                    0",
"2                    0",
"2                    0",
"2                    0",
"2                    0",
"2p      R E  R       0",
"234      3456      340",
"2                    0",
"2    XXX   4536    XX0",
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

