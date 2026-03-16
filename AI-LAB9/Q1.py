import math
board = [" " for _ in range(9)]
nodes_explored = 0

def print_board():
    print(board[0], "|", board[1], "|", board[2])
    print("--+---+--")
    print(board[3], "|", board[4], "|", board[5])
    print("--+---+--")
    print(board[6], "|", board[7], "|", board[8])

def check_winner(b, player):
    win_states = [
        [0,1,2],[3,4,5],[6,7,8],
        [0,3,6],[1,4,7],[2,5,8],
        [0,4,8],[2,4,6]
    ]
    
    for state in win_states:
        if b[state[0]] == b[state[1]] == b[state[2]] == player:
            return True
    return False

def is_full(b):
    return " " not in b

def minimax(b, depth, is_max):
    global nodes_explored
    nodes_explored += 1

    if check_winner(b, "O"):
        return 1
    if check_winner(b, "X"):
        return -1
    if is_full(b):
        return 0

    if is_max:
        best = -math.inf
        for i in range(9):
            if b[i] == " ":
                b[i] = "O"
                val = minimax(b, depth+1, False)
                b[i] = " "
                best = max(best, val)
        return best
    else:
        best = math.inf
        for i in range(9):
            if b[i] == " ":
                b[i] = "X"
                val = minimax(b, depth+1, True)
                b[i] = " "
                best = min(best, val)
        return best

def best_move():
    best_val = -math.inf
    move = -1

    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            move_val = minimax(board, 0, False)
            board[i] = " "

            if move_val > best_val:
                best_val = move_val
                move = i
    return move

def play():
    print("Tic Tac Toe (Minimax AI)")
    print_board()

    while True:
        player = int(input("Enter position (0-8): "))
        if board[player] == " ":
            board[player] = "X"
        else:
            print("Invalid move")
            continue

        if check_winner(board,"X"):
            print_board()
            print("Player wins!")
            break

        if is_full(board):
            print_board()
            print("Draw!")
            break

        ai_move = best_move()
        board[ai_move] = "O"

        print("\nAI Move:")
        print_board()

        if check_winner(board,"O"):
            print("AI wins!")
            break

        if is_full(board):
            print("Draw!")
            break

play()
print("Nodes explored:", nodes_explored)