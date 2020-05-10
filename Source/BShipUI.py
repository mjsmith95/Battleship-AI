# -*- coding: utf-8 -*-
"""
Created on Sun May 10 13:19:24 2020

@author: miles
"""

import pygame as pg

#Some colors 
white = (255, 255, 255) 
red = () 
black = (0,0,0)
grey = ()
dark_grey = ()  

#screen set up 
screen_h = 800
screen_w = 600
screen = pg.display.set_mode((screen_h, screen_w)) 
clock = pg.time.Clock()
pg.display.set_caption('Battleship') 

  

"""
to be implemented:


def render_ship(ship_length, ship_cord_vec): 

def hit(int cord): 
    
def miss(int cord): 
    
def firing_action(int cord): 

def place_ship(): 
"""
    
       
def render_ship(color,screen):
    


if __name__ == '__main__':
    pg.init()