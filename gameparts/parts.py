class Board:
    def __init__(self, field_size=3):
        self.field_size = field_size
        self.board = [[' ' for _ in range(self.field_size)] for _ in range(self.field_size)]

    def make_move(self, row, col, player):
        from gameparts.exceptions import FieldIndexError
        if 0 <= row < self.field_size and 0 <= col < self.field_size:
            if self.board[row][col] == ' ':
                self.board[row][col] = player
            else:
                raise ValueError('Клетка уже занята!')
        else:
            raise FieldIndexError()

    def display(self):
        for row in self.board:
            print('|'.join(row))
            print('-' * (2 * self.field_size - 1))

    def is_board_full(self):
        # Цикл проходится по всем строкам игрового поля.
        for i in range(self.field_size):
            # А потом по всем столбцам.
            for j in range(self.field_size):
                # Если находит свободную ячейку...
                if self.board[i][j] == ' ':
                    # ...игра продолжается.
                    return False
        # Иначе - ничья!
        return True

    def check_win(self, player):
        # Проверка по горизонталям и вертикалям
        for i in range(self.field_size):
            if (all([self.board[i][j] == player for j in range(self.field_size)]) or
                    all([self.board[j][i] == player for j in range(self.field_size)])):
                return True

        # Проверка по диагоналям
        if (all([self.board[i][i] == player for i in range(self.field_size)]) or
                all([self.board[i][self.field_size - 1 - i] == player for i in range(self.field_size)])):
            return True

        return False