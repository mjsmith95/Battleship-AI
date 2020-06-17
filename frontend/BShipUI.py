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
    rectangle_dragging = False
    ships_placed = False
    fps = 30
    colors = [grid_blue, backboard_color]

    while not ships_placed:

        for event in pg.event.get():
            if event.type == pg.QUIT:
                ships_placed = True

            elif event.type == pg.MOUSEBUTTONDOWN:
                # button == 1 means left click
                if event.button == 1:
                    for ship in ship_list:

                        if ship[0].collidepoint(event.pos):
                            print("cur ship size " + str(len(ship)))
                            rectangle_dragging = True
                            offset_x = [0] * len(ship)
                            offset_y = [0] * len(ship)
                            mouse_x, mouse_y = event.pos
                            for i in range(len(ship)):
                                offset_x[i] = (ship[i].x - mouse_x)  # + (ship[0].x - segment.x)))
                                offset_y[i] = (ship[i].y - mouse_y)  # +(ship[0].y - segment.y)))
                            print("offset len: " + str(len(offset_x)))
            elif event.type == pg.MOUSEBUTTONUP:
                if event.button == 1:
                    rectangle_dragging = False

            elif event.type == pg.MOUSEMOTION:
                if rectangle_dragging:
                    for ship in ship_list:
                        print("list len " + str(len(offset_x)))
                        print("cur ship size " + str(len(ship)))
                        mouse_x, mouse_y = event.pos
                        if len(ship) == len(offset_x):
                            for i in range(len(ship)):
                                print(i)
                                ship[i].x = mouse_x + offset_x[i]
                                ship[i].y = mouse_y + offset_y[i]

        screen.fill((30, 30, 30))
        render_board(colors, screen, screen_h, screen_w)
        draw_ship(cruiser, floating_ship_grey, screen)
        draw_ship(sub, floating_ship_grey, screen)
        pg.draw.rect(screen, hit_red, rectangle)
        pg.display.flip()
        clock.tick(fps)


if __name__ == '__main__':
    pg.init()
    board_setup()
    pg.quit()
