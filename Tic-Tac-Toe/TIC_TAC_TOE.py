# TIC_TAC_TOE GAME
from random import randrange

def display_board(board):
    print('+-------' * 3, '+', sep='')
    for row in range(3):
        print('|       ' * 3, '|', sep='')
        for col in range(3):
            print("|   " + str(board[row][col]) + "   ", end='')
        print('|')
        print('|       ' * 3, '|', sep='')
        print('+-------' * 3, '+', sep='')


def enter_move(board):
    ok = False
    while not ok:
        move = input('Enter your move (1–9): ')
        ok = move.isdigit() and 1 <= int(move) <= 9
        if not ok:
            print('❌ Invalid input – please enter a number between 1 and 9.')
            continue
        move = int(move) - 1
        row = move // 3
        col = move % 3
        if board[row][col] in ['O', 'X']:
            print('⚠️ That cell is already occupied! Try again.')
            ok = False
            continue
        ok = True
    board[row][col] = 'O'


def make_list_of_free_fields(board):
    free = []
    for row in range(3):
        for col in range(3):
            if board[row][col] not in ['O', 'X']:
                free.append((row, col))
    return free


def victory_for(board, sgn):
    if sgn == 'X':
        who = 'me'
    elif sgn == 'O':
        who = 'you'
    else:
        who = None

    # Rows and Columns
    for rc in range(3):
        if board[rc][0] == sgn and board[rc][1] == sgn and board[rc][2] == sgn:
            return who
        if board[0][rc] == sgn and board[1][rc] == sgn and board[2][rc] == sgn:
            return who

    # Diagonals
    if board[0][0] == sgn and board[1][1] == sgn and board[2][2] == sgn:
        return who
    if board[0][2] == sgn and board[1][1] == sgn and board[2][0] == sgn:
        return who

    return None


def draw_move(board):
    free = make_list_of_free_fields(board)
    cnt = len(free)
    if cnt > 0:
        row, col = free[randrange(cnt)]
        board[row][col] = 'X'


# --- Main Game ---
board = [[3 * j + i + 1 for i in range(3)] for j in range(3)]
human_turn = True
victor = None

while True:
    display_board(board)
    free = make_list_of_free_fields(board)
    if not free:
        break

    if human_turn:
        enter_move(board)
        victor = victory_for(board, 'O')
    else:
        draw_move(board)
        victor = victory_for(board, 'X')

    if victor is not None:
        break
    human_turn = not human_turn

# --- Game Result ---
display_board(board)
if victor == 'you':
    print('🎉 You won the game!')
elif victor == 'me':
    print('🤖 I won the game!')
else:
    print('😐 It’s a tie!')
