import pieces as piece
import pygame
import ai


WIDTH, HEIGHT = 600, 600
ROWS, COLS = 8, 8
SQUARE_SIZE = WIDTH // COLS

# rgb
LIGHT = (252, 213, 106)
DARK = (231, 178, 34)
RED = (255, 0, 0)
GREEN = (2, 228, 24)
GREY = (124, 120, 119)


class Chess:
    def __init__(self, player_color):
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.num_moves = 0
        self.num_p1 = 16
        self.p1_king = True
        self.p2_king = True
        self.num_p2 = 16
        self.turn = 'white'
        self.player_color = player_color
        self.move_sound = pygame.mixer.Sound("sounds/move_sound.mp3")
        self.move_sound.set_volume(.3)
        self.clicks = []
        self.move_made = False
        self.board = [[piece.Rook('black'), piece.Knight('black'), piece.Bishop('black'), piece.King('black'),
                       piece.Queen('black'), piece.Bishop('black'), piece.Knight('black'), piece.Rook('black')],
                      [piece.Pawn('black'), piece.Pawn('black'), piece.Pawn('black'), piece.Pawn('black'),
                       piece.Pawn('black'), piece.Pawn('black'), piece.Pawn('black'), piece.Pawn('black')],
                      [0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0],
                      [piece.Pawn('white'), piece.Pawn('white'), piece.Pawn('white'), piece.Pawn('white'),
                       piece.Pawn('white'), piece.Pawn('white'), piece.Pawn('white'), piece.Pawn('white')],
                      [piece.Rook('white'), piece.Knight('white'), piece.Bishop('white'), piece.King('white'),
                       piece.Queen('white'), piece.Bishop('white'), piece.Knight('white'), piece.Rook('white')]]

    def update_locs(self):
        for x in range(8):
            for y in range(8):
                if self.board[x][y] != 0:
                    self.board[x][y].loc = [x, y]

    def draw_squares(self):
        self.screen.fill(LIGHT)
        for row in range(ROWS):
            for col in range(row % 2, COLS, 2):
                pygame.draw.rect(self.screen, DARK,
                                 (row * SQUARE_SIZE, col * SQUARE_SIZE,
                                  SQUARE_SIZE, SQUARE_SIZE))

    def draw_sprites(self):
        for x in range(8):
            for y in range(8):
                if self.board[x][y] != 0:
                    if (self.board[x][y].color == 'black' and x > 3) \
                            or (self.board[x][y].color == 'white' and x < 4):
                        sprite = pygame.image.load(self.board[x][y].alt_sprite)
                    else:
                        sprite = pygame.image.load(self.board[x][y].sprite)
                    self.screen.blit(sprite, ((y * SQUARE_SIZE), (x * SQUARE_SIZE)))

    def show_moves(self):
        x, y = self.clicks[0][0], self.clicks[0][1]
        moves = self.board[x][y].get_moves(self.board)
        s = pygame.Surface((SQUARE_SIZE, SQUARE_SIZE))
        s.set_alpha(75)
        s.fill(GREY)
        self.screen.blit(s, (y * SQUARE_SIZE, x * SQUARE_SIZE))
        for i in range(len(moves)):
            if self.board[moves[i][0]][moves[i][1]] == 0:
                s.fill(GREEN)
            elif self.board[x][y].color == self.board[moves[i][0]][moves[i][1]]:
                s.fill(GREEN)
            else:
                s.fill(RED)
            self.screen.blit(s, (moves[i][1] * SQUARE_SIZE, moves[i][0] * SQUARE_SIZE))

    def update(self):
        self.draw_squares()
        if len(self.clicks) == 1:
            self.show_moves()
        self.draw_sprites()
        self.update_locs()
        if self.move_made:
            pygame.mixer.Sound.play(self.move_sound)
            self.move_made = False
        pygame.display.update()

    def swap(self):
        cur_x, cur_y = self.clicks[0][0], self.clicks[0][1]
        swp_x, swp_y = self.clicks[1][0], self.clicks[1][1]
        temp = self.board[cur_x][cur_y]
        self.board[cur_x][cur_y] = self.board[swp_x][swp_y]
        self.board[swp_x][swp_y] = temp

    def game_over(self):
        bk_found = wk_found = False
        for x in range(8):
            for y in range(8):
                if self.board[x][y] != 0 and self.board[x][y].letter == 'K':
                    if self.board[x][y].color == 'black':
                        bk_found = True
                    elif self.board[x][y].color == 'white':
                        wk_found = True
        self.p1_king = wk_found
        self.p2_king = wk_found
        if bk_found and wk_found:
            return False
        return True

    # noinspection PyTypeChecker
    def is_attack(self, location):
        if self.board[location[0]][location[1]] == 0:
            return False
        if self.board[location[0]][location[1]].color == 'white':
            self.num_p1 -= 1
            self.board[location[0]][location[1]] = 0
        elif self.board[location[0]][location[1]].color == 'black':
            self.num_p2 -= 1
            self.board[location[0]][location[1]] = 0

    def update_clicks(self, row, col):
        if len(self.clicks) == 0:
            if self.board[row][col] != 0:
                if self.turn == self.board[row][col].color:
                    self.clicks.append([row, col])
        else:
            self.clicks.append([row, col])

    def make_move(self):
        if len(self.clicks) == 2:
            # player moved a piece
            if self.board[self.clicks[0][0]][self.clicks[0][1]].is_legal_move(
                    [self.clicks[1][0], self.clicks[1][1]], self.board):
                self.num_moves += 1
                self.is_attack([self.clicks[1][0], self.clicks[1][1]])
                self.swap()
                self.turn = 'black' if self.turn == 'white' else 'white'
                self.move_made = True
            self.clicks = []

    def run(self):
        pygame.display.set_caption("Chess")
        done = False
        clock = pygame.time.Clock()
        self.update_locs()
        while not done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
                if self.turn == self.player_color:
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        pos = pygame.mouse.get_pos()
                        row, col = get_row_col_from_mouse(pos)
                        self.update_clicks(row, col)
                        self.make_move()
                else:
                    color = 'black' if self.player_color == 'white' else 'white'
                    # somewhere in here its messing up the whole board
                    move = ai.pick_move(self.board, color)
                    self.clicks.append(move[0])
                    self.clicks.append(move[1])
                    self.make_move()
                    self.turn = self.player_color
                self.update()
                if self.game_over():
                    done = True
                    if self.p1_king:
                        print('White Won!')
                    else:
                        print('Black Won!')
                    print('White had', self.num_p1, 'pieces remaining')
                    print('Black had', self.num_p2, 'pieces remaining')
                    print('There were', self.num_moves, 'moves made this game')
            clock.tick(60)
        pygame.mixer.quit()
        pygame.quit()


def get_row_col_from_mouse(pos):
    x, y = pos
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE
    return row, col


if __name__ == '__main__':
    pygame.init()
    pygame.mixer.init()
    print('What color would you like to be?')
    player_color = int(input("1) White\n2) Black\n> "))
    player_color = 'white' if player_color == 1 else 'black'
    game = Chess(player_color)
    game.run()
