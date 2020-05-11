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

def hit(int cord): 
    
def miss(int cord): 
    
def firing_action(int cord): 

"""
    
       
def render_board(colors, scrn, scrn_h, scrn_w):
    
    board_demension = int(scrn_h * .9)
    board_location = (scrn_h - int(scrn_h * 0.96))
    back_board = pg.Rect(board_location, board_location, board_demension, board_demension) 
    board_divison = board_demension/10 

    pg.draw.rect(scrn, colors[1], back_board, 0)
    
    for i in range(11):
        #horizontal
        pg.draw.line(scrn, colors[0], [board_location, board_location+(board_divison*i)], [board_location+board_demension, board_location+(board_divison*i)], 2)
        #vertical 
        pg.draw.line(scrn, colors[0], [board_location+(board_divison*i),board_location], [board_location+(board_divison*i), board_location+board_demension], 2)
          
def build_ship(ship_length, spacing, ship_cords, scrn_h, is_vertical): 
    box_demension = int((scrn_h * .9) / 10)
    print(box_demension)
    box_demension = (box_demension - (spacing)) 
    #implement converstion from list cords to screen cords 
    pos = ship_cords
    ship = []
    for i in range(ship_length): 
        # draw cubes with consec spacing = line lenght in board 
        if (is_vertical):
            ship_segment = pg.Rect(pos[0],pos[1] + (box_demension + spacing)*i, box_demension, box_demension)
        else: 
            ship_segment = pg.Rect((pos[0] + (box_demension + spacing)*i), pos[1], box_demension, box_demension) 
        # add to collection  
        ship.append(ship_segment)
    return(ship)

def draw_ship(ship, color, scrn):
    for segement in ship: 
        pg.draw.rect(scrn, color, segement)

def move_ship(ship, cords, mouse_pos): 
    for segement in ship: 
        segement.x = cords[0]
        segement.y = cords[1]
    
def board_setup():
    rectangle = pg.rect.Rect(176, 134, 17, 17)
    rectangle_draging = False
    ships_placed = False
    fps = 30 
    colors = [grid_blue,backboard_color]
   
    cruiser = build_ship(5, 2, [(screen_h - int(screen_h * 0.96))+2, (screen_h - int(screen_h * 0.96))+2], screen_h, True) 
    sub = build_ship(3, 2, [(screen_h - int(screen_h * 0.96))+2+int((screen_h * .9) / 10), (screen_h - int(screen_h * 0.96))+2+int((screen_h * .9) / 10)], screen_h, True)

    ship_list = [cruiser,sub] 
    while not ships_placed: 
        
        for event in pg.event.get():
            if event.type == pg.QUIT:
                ships_placed = True
                
            elif event.type == pg.MOUSEBUTTONDOWN:
                if event.button == 1:   
                    for ship in ship_list:
                     
                        if ship[0].collidepoint(event.pos):
                            print("cur ship size " + str(len(ship)))
                            rectangle_draging = True 
                            offset_x = [0] * len(ship)
                            offset_y = [0] * len(ship)
                            mouse_x, mouse_y = event.pos
                            for i in range(len(ship)): 
                                print(ship[i].x)
                                offset_x[i] = (ship[i].x - (mouse_x)) #+ (ship[0].x - segment.x)))
                                offset_y[i] = (ship[i].y - (mouse_y)) #+(ship[0].y - segment.y)))
    
            elif event.type == pg.MOUSEBUTTONUP:
                if event.button == 1:            
                    rectangle_draging = False
                     
            elif event.type == pg.MOUSEMOTION:
                if rectangle_draging:
                    print("lsit len " + str(len(offset_x)))
                    for ship in ship_list:
                        mouse_x, mouse_y = event.pos 
                        for i in range(len(ship)):
                            print(ship[i].x)
                            ship[i].x = mouse_x + offset_x[i]
                            ship[i].y = mouse_y + offset_y[i]
        
        screen.fill((30,30,30))
        pg.draw.rect(screen, hit_red, rectangle)
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