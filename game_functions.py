import pygame as pg
import settings as sett


def draw_board(color = '#ffffff'):
    x = 59
    y = 125

    pg.draw.line(sett.screen, color, (0+x, 93+y), (282+x, 93+y), 5)
    pg.draw.line(sett.screen, color, (0+x, 187+y), (282+x, 187+y), 5)
    pg.draw.line(sett.screen, color, (93+x, 0+y), (93+x, 282+y), 5)    
    pg.draw.line(sett.screen, color, (187+x, 0+y), (187+x, 282+y), 5)

def play_game():
    if(sett.game_status==True and sett.display_winner_status==False):
        if(sett.current_player == 'X'):
            draw_board('#ee7777')
            render_text(f"{sett.current_player}'s Turn", 28, 55)
            place_symbol()
        elif(sett.current_player == 'O'):
            draw_board('#6495ed')
            render_text(f"{sett.current_player}'s Turn", 28, 55)
            place_symbol()
    elif(sett.game_status==True and sett.display_winner_status==True):
        display_winner()
    elif not sett.game_status:
        render_text("Play Tic Tac Toe", 25, 35)
        render_text("Press SPACE to start the Game!", 15, 65)
        draw_board()
        display_score()

def render_text(text, size, y, color='#ffffff'):
    font = pg.font.Font('./assets/font_Consolas.ttf', size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect(center=(400//2, y))
    sett.screen.blit(text_surface, text_rect)

def display_score():

    font = pg.font.Font('./assets/font_Consolas.ttf', 17)

    red = f"Red Wins = {sett.red_score}"
    text_surface = font.render(red, True, '#ee7777')
    sett.screen.blit(text_surface, (5, 425))

    blue = f"Blue Wins = {sett.blue_score}"
    text_surface = font.render(blue, True, '#6495ed')
    sett.screen.blit(text_surface, (260, 425))

def place_value(x, y):
    row = y//sett.box_height
    col = x//sett.box_width

    if(row>=0 and row<=2) and (col>=0 and col<=2):
        if(sett.board[row][col] == None):
            sett.board[row][col] = sett.current_player
            sett.box_filled+=1

            check_winner()

            if(sett.box_filled == 9):
                sett.display_winner_status = True

            if(sett.current_player == 'X'):
                sett.current_player = 'O'
            else:
                sett.current_player = 'X'

def place_symbol():
    for row in range(3):
        for col in range(3):
            if(sett.board[row][col] == 'X'):
                sett.screen.blit(sett.x_image, sett.coordinates[row][col])
            elif(sett.board[row][col] == 'O'):
                sett.screen.blit(sett.o_image, sett.coordinates[row][col])

def check_winner():
    for row in range(3):
        if(sett.board[row][0] == sett.board[row][1] == sett.board[row][2]):
            if(sett.board[row][0] == 'X'):
                sett.red_score+=1
                sett.display_winner_status = True
                return "Player 'X' wins the Game."
            elif(sett.board[row][0] == 'O'):
                sett.blue_score+=1
                sett.display_winner_status = True
                return "Player 'O' wins the Game."
        
    for col in range(3):
        if(sett.board[0][col] == sett.board[1][col] == sett.board[2][col]):
            if(sett.board[0][col] == 'X'):
                sett.red_score+=1
                sett.display_winner_status = True
                return "Player 'X' wins the Game."
            elif(sett.board[0][col] == 'O'):
                sett.blue_score+=1
                sett.display_winner_status = True
                return "Player 'O' wins the Game."
        
    if(sett.board[0][0] == sett.board[1][1] == sett.board[2][2]):
        if(sett.board[0][0] == 'X'):
            sett.red_score+=1
            sett.display_winner_status = True
            return "Player 'X' wins the Game."
        elif(sett.board[0][0] == 'O'):
            sett.blue_score+=1
            sett.display_winner_status = True
            return "Player 'O' wins the Game."
   
    if(sett.board[0][2] == sett.board[1][1] == sett.board[2][0]):
        if(sett.board[0][2] == 'X'):
            sett.red_score+=1
            sett.display_winner_status = True
            return "Player 'X' wins the Game."
        elif(sett.board[0][2] == 'O'):
            sett.blue_score+=1
            sett.display_winner_status = True
            return "Player 'O' wins the Game."
    
    return ""

def display_winner():
    winner = check_winner()

    if(winner!=""):
        draw_board()
        render_text(winner, 18, 35, '#808080')
        render_text("Press SPACE to start again or ESC to Main Menu!", 11, 65)
        place_symbol()
    elif(winner==""):
        draw_board()
        render_text("No One win the Game!", 18, 35)
        render_text("Press SPACE to start again or ESC to Main Menu!", 11, 65)
        place_symbol()

def reset_game():
    sett.board = [[None for _ in range(3)] for _ in range(3)]
    sett.box_filled = 0
    sett.display_winner_status = False