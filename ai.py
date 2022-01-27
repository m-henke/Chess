import random
import copy


# A pawn is worth 1
# A knight is worth 3
# A bishop is worth 3
# A rook is worth 5
# A queen is worth 9
# The king is worth 90 (infinitely valuable)

# if ai goes first move pawn at board[6][3] 2 spaces


def get_possible_moves(board, color):
    pawn_moves = []
    knight_moves = []
    rook_moves = []
    bishop_moves = []
    queen_moves = []
    king_moves = []
    for x in range(8):
        for y in range(8):
            if board[x][y] != 0:
                if board[x][y].color == color:
                    choices = board[x][y].get_moves(board)
                    move = choices, [x, y]
                    if len(move[0]) != 0:
                        if board[x][y].letter == 'P':
                            pawn_moves.append(move)
                        elif board[x][y].letter == 'N':
                            knight_moves.append(move)
                        elif board[x][y].letter == 'R':
                            rook_moves.append(move)
                        elif board[x][y].letter == 'B':
                            bishop_moves.append(move)
                        elif board[x][y].letter == 'Q':
                            queen_moves.append(move)
                        elif board[x][y].letter == 'K':
                            king_moves.append(move)
    return pawn_moves, knight_moves, rook_moves, bishop_moves, queen_moves, king_moves


def swap(board, clicks):
    cur_x, cur_y = clicks[0][0], clicks[0][1]
    swp_x, swp_y = clicks[1][0], clicks[1][1]
    temp = board[cur_x][cur_y]
    board[cur_x][cur_y] = board[swp_x][swp_y]
    board[swp_x][swp_y] = temp
    return board


def is_attack(location, color, board):
    if board[location[0]][location[1]] == 0:
        return board
    elif board[location[0]][location[1]].color != color:
        board[location[0]][location[1]] = 0
        return board
    return board


def make_move(board, choice, color):
    board = is_attack([choice[1][0], choice[1][1]], color, board)
    return swap(board, choice)


def evaluate_move(board_org, choice, color):
    piece_worth = {'P': 1, 'N': 3, 'B': 3, 'R': 5, 'Q': 9, 'K': 90}
    move_worth = 0
    board = make_move(board_org, choice, color)
    for x in range(8):
        for y in range(8):
            if board[x][y] != 0:
                if board[x][y].color != color:
                    move_worth += piece_worth[board[x][y].letter]
    return move_worth


def get_piece_moves(pieces):
    all_moves = []
    for piece in pieces:
        cur = piece[1]
        for move in piece[0]:
            all_moves.append([cur, move])
    return all_moves


# picks a random move
def pick_random_move(board, color):
    # pawn, knight, rook, bishop, queen, king
    choices = get_possible_moves(board, color)
    while True:
        randx = random.randint(0, 5)
        if len(choices[randx]) != 0:
            randy = random.randint(0, len(choices[randx]) - 1)
            randz = random.randint(0, len(choices[randx][randy][0]) - 1)
            return choices[randx][randy][1], choices[randx][randy][0][randz]


# if an attack or attacks were made it picks the one that takes the most valuable piece,
# if no attacks were made it picks a random move
def pick_move(board, color):
    # pawn, knight, rook, bishop, queen, king
    choices = get_possible_moves(board, color)
    all_moves = []
    max_val = 129
    for x in range(len(choices)):
        if len(choices[x]) != 0:
            all_moves += get_piece_moves(choices[x])
    for x in range(len(all_moves)):
        score = evaluate_move(copy.deepcopy(board), all_moves[x], color)
        if score < 129:
            max_val = score
        all_moves[x].append(score)
    if max_val == 129:
        return pick_random_move(board, color)
    else:
        all_moves.sort(key=lambda all_moves: all_moves[2])
        return all_moves[0]
