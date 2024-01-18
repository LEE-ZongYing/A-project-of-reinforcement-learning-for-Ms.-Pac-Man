#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pygame
import tkinter
from tkinter import messagebox
import pacman
import sys, types, time, random, os
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 576

# Define some colors
BLACK = (0,0,0)
WHITE = (255,255,255)
BLUE = (0,0,255)
RED = (255,0,0)

class Game(object):
    def __init__(self):
        self.font = pygame.font.Font(None,40)
        self.about = False
        self.game_over = True
        # Create the variable for the score
        self.score = 0
        # Create the font for displaying the score on the screen
        self.font = pygame.font.Font(None,35)
        # Create the menu of the game
        self.menu = Menu(("Start","About","Exit"),font_color = WHITE,font_size=60)
        
        # Create the blocks that will set the paths where the player can go
        self.horizontal_blocks = pygame.sprite.Group()
        self.vertical_blocks = pygame.sprite.Group()
        # Create a group for the dots on the screen
        self.dots_group = pygame.sprite.Group()
        
        
       
    def process_events(self):
        for event in pygame.event.get(): # User did something
            if event.type == pygame.QUIT: # If user clicked close
                return True
            self.menu.event_handler(event)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if self.game_over and not self.about:
                        if self.menu.state == 0:
                            # ---- START ------
                            self.__init__()
                            self.game_over = False
                        elif self.menu.state == 1:
                            # --- ABOUT ------
                            self.about = True
                        elif self.menu.state == 2:
                            # --- EXIT -------
                            # User clicked exit
                            return True
                
                elif event.key == pygame.K_ESCAPE:
                    self.game_over = True
                    self.about = False    
        return False

    def run_logic(self):
        if not self.game_over:
            
            
            # When the block_hit_list contains one sprite that means that player hit a dot
            if len(block_hit_list) > 0:
                # Here will be the sound effect
                self.pacman_sound.play()
                self.score += 1
            
            if len(block_hit_list) > 0:
                
                self.game_over_sound.play()
            
            
           # tkMessageBox.showinfo("GAME OVER!","Final Score = "+(str)(GAME.score))    

    def display_frame(self,screen):
        # First, clear the screen to white. Don't put other drawing commands
        screen.fill(BLACK)
        # --- Drawing code should go here
        if self.game_over:
            if self.about:
                self.display_message(screen,"It is an artificial intelligence course.",-2,0)
                self.display_message(screen,"This is our final project,pacman.",-1,0)
                self.display_message(screen,"Member:",1,1)
                self.display_message(screen,"C107110133 CHEN,THIENG-CHIENG",2,1)
                self.display_message(screen,"C107110106 KUO,KUAN-HUNG",3,1)
                self.display_message(screen,"C107104218 Lee Zong-Ying",4,1)
                #"a maze containing various dots,\n"
                #known as Pac-Dots, and four ghosts.\n"
                #"The four ghosts roam the maze, trying to kill Pac-Man.\n"
                #"If any of the ghosts hit Pac-Man, he loses a life;\n"
                #"the game is over.\n")
            else:
                self.menu.display_frame(screen)
        else:
            # --- Draw the game here ---
            args = pacman.readCommand( sys.argv[1:],0.6,0.4,0.6)
            pacman.runGames( **args )
            self.game_over = True
        # --- Go ahead and update the screen with what we've drawn.
        pygame.display.flip()

    def display_message(self,screen,message,num,altype,color=(255,0,0)):
        label = self.font.render(message,True,color)
        # Get the width and height of the label
        width = label.get_width()
        height = label.get_height()
        # Determine the position of the label
        if altype == 0:
            posX = (SCREEN_WIDTH /2) - (width /2)
        else:
            posX = (SCREEN_WIDTH/4)
        posY = (SCREEN_HEIGHT /2) - (height /2)+(num*30)
        # Draw the label onto the screen
        screen.blit(label,(posX,posY))


class Menu(object):
    state = 0
    def __init__(self,items,font_color=(0,0,0),select_color=(255,0,0),ttf_font=None,font_size=25):
        self.font_color = font_color
        self.select_color = select_color
        self.items = items
        self.font = pygame.font.Font(ttf_font,font_size)
        
    def display_frame(self,screen):
        for index, item in enumerate(self.items):
            if self.state == index:
                label = self.font.render(item,True,self.select_color)
            else:
                label = self.font.render(item,True,self.font_color)
            
            width = label.get_width()
            height = label.get_height()
            
            posX = (SCREEN_WIDTH /2) - (width /2)
            # t_h: total height of text block
            t_h = len(self.items) * height
            posY = (SCREEN_HEIGHT /2) - (t_h /2) + (index * height)
            
            screen.blit(label,(posX,posY))
        
    def event_handler(self,event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                if self.state > 0:
                    self.state -= 1
            elif event.key == pygame.K_DOWN:
                if self.state < len(self.items) -1:
                    self.state += 1
