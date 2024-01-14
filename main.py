import tkinter as tk
from sudoku_solver_gui import SudokuSolverGUI

if __name__ == "__main__":
    root = tk.Tk()
    gui = SudokuSolverGUI(root)
    root.mainloop()
