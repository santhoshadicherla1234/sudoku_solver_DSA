import tkinter as tk
from tkinter import ttk
import time
from sudoku_solver import SudokuSolver

class SudokuSolverGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Sudoku Solver")

        self.solver = SudokuSolver()

        self.entry_board = [[None for _ in range(9)] for _ in range(9)]

        self.create_widgets()

    def create_widgets(self):
        for i in range(9):
            for j in range(9):
                self.entry_board[i][j] = tk.Entry(self.root, width=3, font=('Arial', 20))
                self.entry_board[i][j].grid(row=i, column=j)
                # Bind each entry to the handle_entry_keypress method
                self.entry_board[i][j].bind("<KeyRelease>", lambda event, r=i, c=j: self.handle_entry_keypress(event, r, c))

        solve_button = tk.Button(self.root, text="Solve", command=self.solve_sudoku)
        solve_button.grid(row=9, column=4)

        exit_button = tk.Button(self.root, text="Exit", command=self.root.quit)
        exit_button.grid(row=10, column=4)

    def handle_entry_keypress(self, event, row, col):
        # Limit the user input to one character (number) in each cell
        value = self.entry_board[row][col].get()
        if value.isdigit():
            # Ensure only the last entered digit remains in the cell
            self.entry_board[row][col].delete(0, tk.END)
            self.entry_board[row][col].insert(0, value[-1])
        else:
            # Clear the cell if the user enters non-digit characters
            self.entry_board[row][col].delete(0, tk.END)

        # Automatically move to the next cell
        if col < 8:
            self.entry_board[row][col + 1].focus()
        elif row < 8:
            self.entry_board[row + 1][0].focus()

    def solve_sudoku(self):
        unsolved_puzzle = [[0 if not self.entry_board[i][j].get() else int(self.entry_board[i][j].get()) for j in range(9)] for i in range(9)]
        self.solver.clear_board()

        for i in range(9):
            for j in range(9):
                value = self.entry_board[i][j].get()
                if value.isdigit():
                    self.solver.set_cell(i, j, int(value))
                else:
                    self.solver.set_cell(i, j, 0)

        if self.solver.solve_sudoku():
            self.show_sudoku_and_moves(unsolved_puzzle)
        else:
            self.show_error("No solution found!")

    def show_sudoku_and_moves(self, unsolved_puzzle):
        # Create a new window to display Sudoku and moves
        puzzle_moves_window = tk.Toplevel(self.root)
        puzzle_moves_window.title("Sudoku and Moves")

        unsolved_frame = tk.LabelFrame(puzzle_moves_window, text="Unsolved Sudoku", padx=10, pady=10)
        unsolved_frame.grid(row=0, column=0, padx=10, pady=10)

        solved_frame = tk.LabelFrame(puzzle_moves_window, text="Solved Sudoku", padx=10, pady=10)
        solved_frame.grid(row=0, column=1, padx=10, pady=10)

        for i in range(9):
            for j in range(9):
                tk.Label(unsolved_frame, text=str(unsolved_puzzle[i][j]), font=('Arial', 20)).grid(row=i, column=j)
                tk.Label(solved_frame, text="", font=('Arial', 20)).grid(row=i, column=j)

        solved_board = self.solver.get_board()
        for i in range(9):
            for j in range(9):
                tk.Label(solved_frame, text=str(solved_board[i][j]), font=('Arial', 20)).grid(row=i, column=j)

        moves_label = tk.Label(puzzle_moves_window, text=f"Number of Moves: {self.solver.get_steps()}", font=('Arial', 14))
        moves_label.grid(row=1, column=0, columnspan=2)

        moves_button = tk.Button(puzzle_moves_window, text="Show Moves", command=lambda: self.show_moves(puzzle_moves_window))
        moves_button.grid(row=2, column=0, columnspan=2)

    def show_moves(self, parent_window):
        moves = self.solver.get_moves()
        moves_window = tk.Toplevel(parent_window)
        moves_window.title("Moves")

        notebook = ttk.Notebook(moves_window)
        notebook.pack()

        max_moves_per_page = 15
        total_pages = (len(moves) + max_moves_per_page - 1) // max_moves_per_page

        for page in range(total_pages):
            page_frame = tk.Frame(notebook)
            notebook.add(page_frame, text=f"Page {page + 1}")

            for i in range(page * max_moves_per_page, min((page + 1) * max_moves_per_page, len(moves))):
                row, col, num = moves[i]
                move_label = tk.Label(page_frame, text=f"Row: {row}, Col: {col}, Number: {num}", font=('Arial', 12))
                move_label.pack()

        if total_pages > 1:
            next_button = tk.Button(moves_window, text="Next", command=lambda: self.show_next_moves(notebook, total_pages))
            next_button.pack()

    def show_next_moves(self, notebook, total_pages):
        current_page = notebook.index("current")
        next_page = (current_page + 1) % total_pages
        notebook.select(next_page)

    def show_error(self, message):
        tk.messagebox.showerror("Error", message)

    def solve_another(self):
        # Clear the Sudoku board and close the solved window
        for i in range(9):
            for j in range(9):
                self.entry_board[i][j].delete(0, tk.END)

        self.solver.clear_board()
