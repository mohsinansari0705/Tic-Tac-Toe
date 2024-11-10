from settings import board

def print_board():
    for i in range(9):
        if(i==2 or i==5):
            print(f" {board[i]} ")
            print("-----------")
        elif(i == 8):
            print(f" {board[i]} ")
        else:
            print(f" {board[i]} |", end="")

    print()

def player_turn(player):
    print(f"--- {player}'s Turn...")
    idx = int(input("Enter the number of the box : "))

    while True:
        if(board[idx-1] == "O" or board[idx-1] == "X"):
            idx = int(input("This box is already occupied. Please give another box number : "))
        else:
            board.pop(idx-1)
            board.insert(idx-1, player)
            break

    print_board()

def check_winner():
    if(board[0] == board[1] == board[2]):
        return (f"_____ The Winner is : '{board[0]}' :) _____")
    elif(board[3] == board[4] == board[5]):
        return (f"_____ The Winner is : '{board[3]}' :) _____")
    elif(board[6] == board[7] == board[8]):
        return (f"_____ The Winner is : '{board[6]}' :) _____")
    elif(board[0] == board[3] == board[6]):
        return (f"_____ The Winner is : '{board[0]}' :) _____")
    elif(board[1] == board[4] == board[7]):
        return (f"_____ The Winner is : '{board[1]}' :) _____")
    elif(board[2] == board[5] == board[8]):
        return (f"_____ The Winner is : '{board[2]}' :) _____")
    elif(board[0] == board[4] == board[8]):
        return (f"_____ The Winner is : '{board[0]}' :) _____")
    elif(board[2] == board[4] == board[6]):
        return (f"_____ The Winner is : '{board[2]}' :) _____")