import game_functions as func
from settings import filled_box


if __name__=="__main__":
    player = "O"
    print("_____ Play Tic-Tac-Toe _____\n")
    func.print_board()
    while True:
        if(filled_box == 9):
            print(func.check_winner())
            break
        else:
            if(func.check_winner()):
                print(func.check_winner())
                break
            else:
                filled_box+=1

                if(player == "O"):
                    func.player_turn(player)
                    player = "X"
                else:
                    func.player_turn(player)
                    player = "O"