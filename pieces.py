def get_bishop_moves(board, loc, color):
    x, y = loc[0], loc[1]
    available_moves = []
    while x > 0 and y > 0:
        x -= 1
        y -= 1
        if board[x][y] == 0 or board[x][y].color != color:
            available_moves.append([x, y])
            if board[x][y] != 0:
                break
        else:
            break
    x, y = loc[0], loc[1]
    while x > 0 and y < 7:
        x -= 1
        y += 1
        if board[x][y] == 0 or board[x][y].color != color:
            available_moves.append([x, y])
            if board[x][y] != 0:
                break
        else:
            break
    x, y = loc[0], loc[1]
    while x < 7 and y > 0:
        x += 1
        y -= 1
        if board[x][y] == 0 or board[x][y].color != color:
            available_moves.append([x, y])
            if board[x][y] != 0:
                break
        else:
            break
    x, y = loc[0], loc[1]
    while x < 7 and y < 7:
        x += 1
        y += 1
        if board[x][y] == 0 or board[x][y].color != color:
            available_moves.append([x, y])
            if board[x][y] != 0:
                break
        else:
            break
    return available_moves


def get_rook_moves(board, loc, color):
    x, y = loc[0], loc[1]
    available_moves = []
    while x > 0:
        x -= 1
        if board[x][y] == 0 or board[x][y].color != color:
            available_moves.append([x, y])
            if board[x][y] != 0:
                break
        else:
            break
    x, y = loc[0], loc[1]
    while x < 7:
        x += 1
        if board[x][y] == 0 or board[x][y].color != color:
            available_moves.append([x, y])
            if board[x][y] != 0:
                break
        else:
            break
    x, y = loc[0], loc[1]
    while y > 0:
        y -= 1
        if board[x][y] == 0 or board[x][y].color != color:
            available_moves.append([x, y])
            if board[x][y] != 0:
                break
        else:
            break
    x, y = loc[0], loc[1]
    while y < 7:
        y += 1
        if board[x][y] == 0 or board[x][y].color != color:
            available_moves.append([x, y])
            if board[x][y] != 0:
                break
        else:
            break
    return available_moves


def get_king_moves(board, loc, color):
    available_moves = []
    x, y = loc[0] - 1, loc[1] - 1
    for i in range(3):
        for j in range(3):
            if x < 0 or x > 7:
                pass
            else:
                if board[x][y + j] == 0 or board[x][y + j].color != color:
                    available_moves.append([x, y + j])
        x += 1
    return available_moves


def get_queen_moves(board, loc, color):
    return get_rook_moves(board, loc, color) + get_bishop_moves(board, loc, color)


def get_knight_moves(board, loc, color):
    available_locs = []
    for x in range(4):
        if x < 2:
            if loc[0] + (x + 1) < 8:
                if x == 0:
                    if loc[1] + 2 < 8:
                        if board[loc[0] + (x + 1)][loc[1] + 2] == 0 \
                                or board[loc[0] + (x + 1)][loc[1] + 2].color != color:
                            available_locs.append([loc[0] + (x + 1), loc[1] + 2])
                    if loc[1] - 2 > -1:
                        if board[loc[0] + (x + 1)][loc[1] - 2] == 0 \
                                or board[loc[0] + (x + 1)][loc[1] - 2].color != color:
                            available_locs.append([loc[0] + (x + 1), loc[1] - 2])
                else:
                    if loc[1] + 1 < 8:
                        if board[loc[0] + (x + 1)][loc[1] + 1] == 0 \
                                or board[loc[0] + (x + 1)][loc[1] + 1].color != color:
                            available_locs.append([loc[0] + (x + 1), loc[1] + 1])
                    if loc[1] - 1 > -1:
                        if board[loc[0] + (x + 1)][loc[1] - 1] == 0 \
                                or board[loc[0] + (x + 1)][loc[1] - 1].color != color:
                            available_locs.append([loc[0] + (x + 1), loc[1] - 1])
        else:
            if loc[0] - (x - 1) > -1:
                if x == 2:
                    if loc[1] + 2 < 8:
                        if board[loc[0] - (x - 1)][loc[1] + 2] == 0 \
                                or board[loc[0] - (x - 1)][loc[1] + 2].color != color:
                            available_locs.append([loc[0] - (x - 1), loc[1] + 2])
                    if loc[1] - 2 > -1:
                        if board[loc[0] - (x - 1)][loc[1] - 2] == 0 \
                                or board[loc[0] - (x - 1)][loc[1] - 2].color != color:
                            available_locs.append([loc[0] - (x - 1), loc[1] - 2])
                else:
                    if loc[1] + 1 < 8:
                        if board[loc[0] - (x - 1)][loc[1] + 1] == 0 \
                                or board[loc[0] - (x - 1)][loc[1] + 1].color != color:
                            available_locs.append([loc[0] - (x - 1), loc[1] + 1])
                    if loc[1] - 1 > -1:
                        if board[loc[0] - (x - 1)][loc[1] - 1] == 0 or \
                                board[loc[0] - (x - 1)][loc[1] - 1].color != color:
                            available_locs.append([loc[0] - (x - 1), loc[1] - 1])
    return available_locs


def get_pawn_moves(board, loc, color, moved):
    available_moves = []
    x, y = loc[0], loc[1]
    if color == 'white':
        if x > 0 and 0 <= y <= 7:
            if y > 0:
                if board[x - 1][y - 1] != 0:
                    if board[x - 1][y - 1].color != color:
                        available_moves.append([x - 1, y - 1])
            if y < 7:
                if board[x - 1][y + 1] != 0:
                    if board[x - 1][y + 1].color != color:
                        available_moves.append([x - 1, y + 1])
    else:
        if x < 7 and 0 <= y <= 7:
            if y > 0:
                if board[x + 1][y - 1] != 0:
                    if board[x + 1][y - 1].color != color:
                        available_moves.append([x + 1, y - 1])
            if y < 7:
                if board[x + 1][y + 1] != 0:
                    if board[x + 1][y + 1].color != color:
                        available_moves.append([x + 1, y + 1])
    if moved:
        if color == 'white':
            if x > 0:
                if board[x - 1][y] == 0:
                    available_moves.append([x - 1, y])
        else:
            if x < 7:
                if board[x + 1][y] == 0:
                    available_moves.append([x + 1, y])
    else:
        if color == 'white':
            if x >= 0:
                if board[x - 1][y] == 0:
                    available_moves.append([x - 1, y])
                    if board[x - 2][y] == 0:
                        available_moves.append([x - 2, y])
        else:
            if x <= 7:
                if board[x + 1][y] == 0:
                    available_moves.append([x + 1, y])
                    if board[x + 2][y] == 0:
                        available_moves.append([x + 2, y])
    return available_moves


class King:
    def __init__(self, color):
        self.color = color
        self.letter = 'K'
        self.loc = [-1, -1]
        if color == 'black':
            self.sprite = 'sprites/buk.svg'
            self.alt_sprite = 'sprites/brk.svg'
        else:
            self.sprite = 'sprites/wrk.svg'
            self.alt_sprite = 'sprites/wuk.svg'

    def is_legal_move(self, location, board):
        if self.loc[0] != -1 and self.loc[1] != -1:
            moves = get_king_moves(board, self.loc, self.color)
            if location in moves:
                return True
        return False

    def get_moves(self, board):
        return get_king_moves(board, self.loc, self.color)


class Queen:
    def __init__(self, color):
        self.color = color
        self.letter = 'Q'
        self.loc = [-1, -1]
        if color == 'black':
            self.sprite = 'sprites/buq.svg'
            self.alt_sprite = 'sprites/brq.svg'
        else:
            self.sprite = 'sprites/wrq.svg'
            self.alt_sprite = 'sprites/wuq.svg'

    def is_legal_move(self, location, board):
        if self.loc[0] != -1 and self.loc[1] != -1:
            moves = get_queen_moves(board, self.loc, self.color)
            if location in moves:
                return True
        return False

    def get_moves(self, board):
        return get_queen_moves(board, self.loc, self.color)


class Rook:
    def __init__(self, color):
        self.color = color
        self.letter = 'R'
        self.loc = [-1, -1]
        if color == 'black':
            self.sprite = 'sprites/bur.svg'
            self.alt_sprite = 'sprites/brr.svg'
        else:
            self.sprite = 'sprites/wrr.svg'
            self.alt_sprite = 'sprites/wur.svg'

    def is_legal_move(self, location, board):
        if self.loc[0] != -1 and self.loc[1] != -1:
            moves = get_rook_moves(board, self.loc, self.color)
            if location in moves:
                return True
        return False

    def get_moves(self, board):
        return get_rook_moves(board, self.loc, self.color)


class Bishop:
    def __init__(self, color):
        self.color = color
        self.letter = 'B'
        self.loc = [-1, -1]
        if color == 'black':
            self.sprite = 'sprites/bub.svg'
            self.alt_sprite = 'sprites/brb.svg'
        else:
            self.sprite = 'sprites/wrb.svg'
            self.alt_sprite = 'sprites/wub.svg'

    def is_legal_move(self, location, board):
        if self.loc[0] != -1 and self.loc[1] != -1:
            moves = get_bishop_moves(board, self.loc, self.color)
            if location in moves:
                return True
        return False

    def get_moves(self, board):
        return get_bishop_moves(board, self.loc, self.color)


class Knight:
    def __init__(self, color):
        self.color = color
        self.letter = 'N'
        self.loc = [-1, -1]
        if color == 'black':
            self.sprite = 'sprites/bun.svg'
            self.alt_sprite = 'sprites/brn.svg'
        else:
            self.sprite = 'sprites/wrn.svg'
            self.alt_sprite = 'sprites/wun.svg'

    def is_legal_move(self, location, board):
        if self.loc[0] != -1 and self.loc[1] != -1:
            moves = get_knight_moves(board, self.loc, self.color)
            if location in moves:
                return True
        return False

    def get_moves(self, board):
        return get_knight_moves(board, self.loc, self.color)


class Pawn:
    def __init__(self, color):
        self.moved = False
        self.color = color
        self.letter = 'P'
        self.loc = [-1, -1]
        if color == 'black':
            self.sprite = 'sprites/bup.svg'
            self.alt_sprite = 'sprites/brp.svg'
        else:
            self.sprite = 'sprites/wrp.svg'
            self.alt_sprite = 'sprites/wup.svg'

    def is_legal_move(self, location, board):
        if self.loc[0] != -1 and self.loc[1] != -1:
            moves = get_pawn_moves(board, self.loc, self.color, self.moved)
            if location in moves:
                self.moved = True
                return True
        return False

    def get_moves(self, board):
        return get_pawn_moves(board, self.loc, self.color, self.moved)
