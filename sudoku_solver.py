import time

class SudokuSolver:
    def __init__(self):
        self.board = [[0 for _ in range(9)] for _ in range(9)]
        self.moves = []
        self.steps = 0
        self.start_time = None

    def is_safe(self, row, col, num):
        # Check if the number is safe to place in the cell
        return self.is_safe_row(row, num) and \
               self.is_safe_col(col, num) and \
               self.is_safe_box(row - row % 3, col - col % 3, num)

    def is_safe_row(self, row, num):
        # Check if the number is safe in the row
        return num not in self.board[row]

    def is_safe_col(self, col, num):
        # Check if the number is safe in the column
        return num not in [self.board[row][col] for row in range(9)]

    def is_safe_box(self, start_row, start_col, num):
        # Check if the number is safe in the 3x3 box
        return num not in [self.board[start_row + i][start_col + j] for i in range(3) for j in range(3)]

    def find_empty_cell(self):
        # Find the first empty cell in the Sudoku grid
        for row in range(9):
            for col in range(9):
                if self.board[row][col] == 0:
                    return row, col
        return None, None

    def solve(self):
        row, col = self.find_empty_cell()
        if row is None:  # Puzzle is solved
            return True

        for num in range(1, 10):
            if self.is_safe(row, col, num):
                self.board[row][col] = num
                self.moves.append((row, col, num))
                self.steps += 1

                if self.solve():
                    return True

                self.board[row][col] = 0
                self.moves.append((row, col, 0))  # Backtrack
                self.steps += 1

        return False

    def solve_sudoku(self):
        self.start_time = time.time()
        self.steps = 0
        self.moves.clear()
        if self.solve():
            return True
        return False

    def get_board(self):
        return self.board

    def get_moves(self):
        return self.moves

    def get_steps(self):
        return self.steps

    def get_solve_time(self):
        return time.time() - self.start_time

    def clear_board(self):
        self.board = [[0 for _ in range(9)] for _ in range(9)]

    def set_cell(self, row, col, num):
        self.board[row][col] = num
