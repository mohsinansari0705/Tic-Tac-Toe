import pygame as pg

dimensions = (400, 450)
screen = pg.display.set_mode(dimensions)
x_image = pg.image.load('./assets/images/x_image.png')
o_image = pg.image.load('./assets/images/o_image.png')
board = [[None for _ in range(3)] for _ in range(3)]
box_height, box_width = 90, 90
box_filled = 0
current_player = 'X'
game_status = False
display_winner_status = False
red_score = 0
blue_score = 0
coordinates = [
    [[72, 138], [167, 138], [262, 138]],
    [[72, 233], [167, 233], [262, 233]],
    [[72, 328], [167, 328], [262, 328]]
]