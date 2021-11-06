import builtins
import pygame
import sys

from pygame import mouse 
from game_window_class import *
from button_class import *

width, height = 800, 800
background = (199, 199, 199)
FPS = 60


def get_events():
    global running
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if mouse_on_grid(mouse_pos):
                click_cell(mouse_pos)
            else:
                for button in buttons:
                    button.click()


def update():
    game_window.update()
    for button in buttons:
        # button.update()
        button.update(mouse_pos)

def draw():
    window.fill(background)
    for button in buttons:
        button.draw()
    game_window.draw()

# functions for the running functionality

def running_get_events():
    global running
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if mouse_on_grid(mouse_pos):
                click_cell(mouse_pos)
            else:
                for button in buttons:
                    button.click()


def running_update():
    game_window.update()
    for button in buttons:
        # button.update()
        button.update(mouse_pos)

def running_draw():
    window.fill(background)
    for button in buttons:
        button.draw()
    game_window.draw()

# function for the pausing functionality

def paused_get_events():
    global running
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if mouse_on_grid(mouse_pos):
                click_cell(mouse_pos)
            else:
                for button in buttons:
                    button.click()


def paused_update():
    game_window.update()
    for button in buttons:
        # button.update()
        button.update(mouse_pos)

def paused_draw():
    window.fill(background)
    for button in buttons:
        button.draw()
    game_window.draw()

# end of the particular pausing functions

#once there is a mouse on a grid, this lines of codes from 26 to 37 should make a cell alive   
def mouse_on_grid(pos):
    if pos[0] > 180 and pos[0] < width-100:
        if pos[1] > 100 and pos[1] < height - 20:
            return True
        return False

def click_cell(pos):
    grid_pos = [pos[0]-180, pos[1]-100]
    grid_pos[0] = grid_pos[0]//20
    grid_pos[1] = grid_pos[1]//20
    #this if statement allow to make a cell alive or dead by just clicking on it
    if game_window.grid[grid_pos[1]][grid_pos[0]].alive:
        game_window.grid[grid_pos[1]][grid_pos[0]].alive = False
    else:
        game_window.grid[grid_pos[1]][grid_pos[0]].alive = True


def make_buttons():
    buttons = []
    buttons.append(Button(window, width//5-50, 50, 100, 20, text = 'RUN', colour = (28, 111, 51), hover_colour = (92, 232, 77), function=run_game))
    buttons.append(Button(window, width//2-50, 50, 100, 20, text = 'PAUSE', colour = (18, 104, 135), hover_colour = (140, 180, 245), function= pause_game))
    buttons.append(Button(window, width//1.2-50, 50, 100, 20, text = 'RESET', colour = (117, 14, 14), hover_colour = (237, 66, 75), function = reset_grid))
    return buttons

def run_game():
    global state
    state = 'running'

def pause_game():
    global state
    state = 'paused'

def reset_grid():
    pass

pygame.init()
window = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
game_window = Game_window(window, 180, 100)
buttons = make_buttons()
state = 'setting'


running = True
while running:
    mouse_pos = pygame.mouse.get_pos()
    if state == 'setting':
        get_events() 
        update()
        draw()
    if state == 'running':
        running_get_events() 
        running_update()
        running_draw()
    if state == 'paused':
        paused_get_events() 
        paused_update()
        paused_draw()
    pygame.display.update()
    clock.tick(FPS)
    print(state)
pygame.quit()
sys.exit()
