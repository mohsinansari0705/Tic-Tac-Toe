import pygame as pg
import game_functions as g_func
import settings as sett

pg.init()

pg.display.set_icon(pg.image.load('./assets/images/logo.png'))
pg.display.set_caption("Tic Tac Toe :Falcon")

running = True
while running:
    sett.screen.fill('#1f1f1f')
    g_func.play_game()

    for event in pg.event.get():
        if(event.type == pg.QUIT):
            running = False

        if(event.type == pg.KEYDOWN):
            if(event.key == pg.K_SPACE):
                sett.game_status = True

            if(event.key == pg.K_ESCAPE):
                sett.game_status = False
                sett.display_winner_status = False

            if(sett.game_status==True and sett.display_winner_status==True):
                if(event.key == pg.K_SPACE):
                    g_func.reset_game()

        if(sett.game_status == True):
            if(event.type == pg.MOUSEBUTTONDOWN):
                mouse_x, mouse_y = pg.mouse.get_pos()
                g_func.place_value(mouse_x-59, mouse_y-125)

    pg.display.update()