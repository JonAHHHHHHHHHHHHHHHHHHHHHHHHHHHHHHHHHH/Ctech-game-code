import pygame
import random

pygame.font.init()

# global variables
s_with = 800
s_height = 700
play_width = 300
play_height = 600
block_size = 30

top_left_x = (s_with - play_width) // 2
top_left_y = s_height - play_height

# shape formats
S = [['.....',
      '.....',
      '..00.',
      '.00..',
      '.....'],
     ['.....',
        '..0..',
        '..00.',
        '...0.',
        '.....']]

Z = [['.....
        '.....',
        '.00..',
        '..00.',
        '.....'],
         ['.....',
            '..0..',
            '.00..',
            '.0...',
            '.....']]