# -*- coding: utf-8 -*-
"""
Created on Sun May 10 13:19:24 2020

@author: miles
"""

import pygame as pg

#Some colors 
white = (255, 255, 255) 
hit_red = (204, 0, 0) 
black = (0,0,0)
floating_ship_grey = (191, 191, 191)
sunken_ship_grey = (51, 51, 51)  
backboard_color = (101, 101, 101)
grid_blue = pg.Color('dodgerblue2')
#screen set up 
screen_w = 900
screen_h = 600
screen = pg.display.set_mode((screen_w, screen_h)) 
pg.display.set_caption('Battleship') 
clock = pg.time.Clock()

  

"""
to be implemented:



def render_ship(ship_length, ship_cord_vec): 

def hit(int cord): 
    
def miss(int cord): 
    
def firing_action(int cord): 

def place_ship(): 
"""
    
       
def render_board(colors, scrn, scrn_h, scrn_w):
    
    board_demension = int(scrn_h * .9)
    board_location = (scrn_h - int(scrn_h * 0.96))
    back_board =  pg.Rect(board_location, board_location, board_demension, board_demension) 
    
    pg.draw.rect(scrn, colors[1], back_board, 0)
    board_divison = board_demension/10 
    for i in range(11):
        #horizontal
        pg.draw.line(scrn, colors[0], [board_location, board_location*i], [], 2)
        #vertical 
        pg.draw.line(scrn, colors[0], [], [], 2)
          

def board_setup():
    ships_placed = False
    fps = 30 
    colors = [grid_blue,backboard_color]
    
    while not ships_placed: 
        for event in pg.event.get():
            if event.type == pg.QUIT:
                ships_placed=True
        render_board(colors, screen, screen_h, screen_w)
        pg.display.flip()
        clock.tick(fps)

if __name__ == '__main__':
    pg.init()
    board_setup() 
    pg.quit()