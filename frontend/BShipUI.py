# -*- coding: utf-8 -*-
"""
Created on Sun May 10 13:19:24 2020

@author: miles
"""

import pygame as pg

# Some colors
white = (255, 255, 255)
hit_red = (204, 0, 0)
black = (0, 0, 0)
floating_ship_grey = (191, 191, 191)
sunken_ship_grey = (51, 51, 51)
backboard_color = (101, 101, 101)
grid_blue = pg.Color('dodgerblue2')
# screen set up
screen_w = 900
screen_h = 600
screen = pg.display.set_mode((screen_w, screen_h))
pg.display.set_caption('Battleship Probability Map')
clock = pg.time.Clock()


def render_board(colors, scrn, scrn_h, scrn_w):
    board_dimension = int(scrn_h * .9)
    board_location = (scrn_h - int(scrn_h * 0.96))
    back_board = pg.Rect(board_location, board_location, board_dimension, board_dimension)
    board_division = board_dimension / 10

    pg.draw.rect(scrn, colors[1], back_board, 0)

    for i in range(11):
        # horizontal
        pg.draw.line(scrn, colors[0], [board_location, int(board_location + (board_division * i))],
                     [board_location + board_dimension, int(board_location + (board_division * i))], 2)
        # vertical
        pg.draw.line(scrn, colors[0], [int(board_location + (board_division * i)), board_location],
                     [int(board_location + (board_division * i)), board_location + board_dimension], 2)


def board_setup():
    rectangle = pg.rect.Rect(176, 134, 17, 17)
    fps = 30
    colors = [grid_blue, backboard_color]
    game_over = False

    while not game_over:

        for event in pg.event.get():
            if event.type == pg.QUIT:
                game_over = True

        screen.fill((30, 30, 30))
        render_board(colors, screen, screen_h, screen_w)
        pg.draw.rect(screen, hit_red, rectangle)
        pg.display.flip()
        clock.tick(fps)


if __name__ == '__main__':
    pg.init()

    for i in range(0, 10):
        test = pg.rect.Rect(i*17 + 20, 0, 17, 17)
        pg.draw.rect(screen, hit_red, test)
        pg.display.flip()
