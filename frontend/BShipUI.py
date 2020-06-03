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
pg.display.set_caption('Battleship')
clock = pg.time.Clock()

"""
to be implemented:

def hit(int cord): 
    
def miss(int cord): 
    
def firing_action(int cord): 

"""


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


def build_ship(ship_length, spacing, ship_cords, scrn_h, is_vertical):
    box_dimension = int((scrn_h * .9) / 10)
    print(box_dimension)
    box_dimension = (box_dimension - spacing)
    # implement conversion from list cords to screen cords
    pos = ship_cords
    ship = []
    for i in range(ship_length):
        # draw cubes with segment spacing = line length in board
        if is_vertical:
            ship_segment = pg.Rect(pos[0], pos[1] + (box_dimension + spacing) * i, box_dimension, box_dimension)
        else:
            ship_segment = pg.Rect((pos[0] + (box_dimension + spacing) * i), pos[1], box_dimension, box_dimension)
            # add to collection
        ship.append(ship_segment)
    return ship


def draw_ship(ship, color, scrn):
    for segment in ship:
        pg.draw.rect(scrn, color, segment)


def move_ship(ship, cords):
    for segment in ship:
        segment.x = cords[0]
        segment.y = cords[1]


def board_setup():
    rectangle = pg.rect.Rect(176, 134, 17, 17)
    rectangle_dragging = False
    ships_placed = False
    fps = 30
    colors = [grid_blue, backboard_color]

    carrier = build_ship(5, 2, [(screen_h - int(screen_h * 0.96)) + 2, (screen_h - int(screen_h * 0.96)) + 2], screen_h,
                         True)

    battleship = build_ship(4, 2, [(screen_h - int(screen_h * 0.96)) + 2 + int((screen_h * .9) / 10),
                                   (screen_h - int(screen_h * 0.96)) + 2 + int((screen_h * .9) / 10)], screen_h, True)

    cruiser = build_ship(3, 2, [(screen_h - int(screen_h * 0.96)) + 2 + int((screen_h * .9) / 10),
                                (screen_h - int(screen_h * 0.96)) + 2 + int((screen_h * .9) / 10)], screen_h, True)

    sub = build_ship(3, 2, [(screen_h - int(screen_h * 0.96)) + 2 + int((screen_h * .9) / 10),
                            (screen_h - int(screen_h * 0.96)) + 2 + int((screen_h * .9) / 10)], screen_h, True)

    destroyer = build_ship(2, 2, [(screen_h - int(screen_h * 0.96)) + 2 + int((screen_h * .9) / 10),
                                  (screen_h - int(screen_h * 0.96)) + 2 + int((screen_h * .9) / 10)], screen_h, True)

    ship_list = [cruiser, sub]
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
