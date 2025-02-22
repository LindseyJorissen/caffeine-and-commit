def show_playboard(board):
    print(f"""  
    *_________________*   
    |  {board[0]}  |  {board[1]}  |  {board[2]}  |
    |_____|_____|_____|
    |  {board[3]}  |  {board[4]}  |  {board[5]}  |
    |_____|_____|_____|
    |  {board[6]}  |  {board[7]}  |  {board[8]}  |
    *_____|_____|_____*
""")

def do_turn(board, player_x_turns, player_o_turns, currentplayer_playerx):
    choice = check_choice(board)
    if currentplayer_playerx:
        player_x_turns.append(choice)
        board[choice] = "X"
    else:
        player_o_turns.append(choice)
        board[choice] = "O"
    show_playboard(board)
    return not currentplayer_playerx

def check_choice(board):
    valid_choice = False
    while not valid_choice:
        choice = int(input("Choose a box (0-8): "))
        if choice < 0 or choice > 8:
            print("Invalid input. Please choose a number between 0 and 8.")
        elif board[choice] == "X" or board[choice] == "O":
            print("Box already taken. Choose another box.")
        else:
            valid_choice = True
    return choice

def check_win(player_turns):
    winning_combos = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        [0, 4, 8], [2, 4, 6]]
    for combo in winning_combos:
        if all(cell in player_turns for cell in combo):
            return True
    return False


def main():
    win = False
    currentplayer_playerx = True
    board = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    player_x_turns = []
    player_o_turns = []
    print("Welcome to TIC TAC TOE! ")
    show_playboard(board)
    while not win:
        if currentplayer_playerx:
            print("Player X, it's your turn.")
        else:
            print("Player O, it's your turn.")
        currentplayer_playerx = do_turn(board, player_x_turns, player_o_turns, currentplayer_playerx)
        if check_win(player_x_turns):
            print("Congratulations, Player X has won!")
            win = True
        elif check_win(player_o_turns):
            print("Congratulations, Player O has won!")
            win = True
        elif len(player_x_turns) + len(player_o_turns) == 9:
            print("It's a tie!")
            win = True

if __name__ == '__main__':
    main()