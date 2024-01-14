# sudoku_solver_DSA
This repository contains a Python application that allows users to solve Sudoku puzzles interactively using a graphical user interface (GUI). The Sudoku solving algorithm is based on backtracking, and the GUI is built using Tkinter, a Python library for creating GUI applications
Functionality
The Sudoku Solver GUI application provides the following features:

Interactive Sudoku Board: Users can input their unsolved Sudoku puzzle directly into the GUI using the provided 9x9 grid of input cells.

Constraint Checking: The application ensures that the entered values adhere to the Sudoku puzzle rules, i.e., each row, column, and 3x3 box contains distinct numbers from 1 to 9.

Solve Button: Upon pressing the "Solve" button, the application uses a backtracking algorithm to find the solution to the input Sudoku puzzle.

Solution Visualization: Once a solution is found, the GUI displays the solved Sudoku puzzle and highlights the moves made by the backtracking algorithm.

Moves Visualization: Users can view the sequence of moves made by the algorithm by clicking the "Show Moves" button. The moves are displayed in pages for better readability.

Exit Button: The "Exit" button allows users to close the application.

Data Structures and Algorithms (DSA)
Backtracking Algorithm
The core of the Sudoku Solver is the backtracking algorithm. Backtracking is a systematic way of searching for a solution to a problem by incrementally building candidates and abandoning those that cannot lead to a valid solution. In the context of the Sudoku puzzle, the backtracking algorithm explores possible values for each cell and tries to fill the puzzle one step at a time, backtracking when a conflict arises. The algorithm ensures that every number placed on the board is valid and eventually finds a valid solution or determines that there is no solution.

The SudokuSolver class contains the backtracking algorithm, implemented in the solve method. The algorithm recursively tries different values for each empty cell (cell with value 0), following the Sudoku rules, and backtracks when a contradiction is encountered.

Time and Space Complexity
The time complexity of the backtracking algorithm for solving an N x N Sudoku puzzle is exponential and can be represented as O(N^(N^2)). However, in practice, due to the constraints of the Sudoku puzzle (9x9 grid), the algorithm terminates quickly after finding a valid solution or determining there is no solution.

The space complexity of the backtracking algorithm is O(N^2) as it needs to store the Sudoku board, which is represented as a 2D array of size N x N.

Object-Oriented Programming (OOPS)
The code follows the Object-Oriented Programming paradigm to promote modularity and readability. The relevant functionalities are encapsulated within the SudokuSolver and SudokuSolverGUI classes. By using classes, we achieve better organization and separation of concerns, making it easier to maintain and extend the codebase.

Tkinter Properties Used
The Tkinter library is utilized to create the GUI for the Sudoku Solver application. The following Tkinter properties and features are used in the implementation:

tk.Tk and tk.Toplevel: These classes are used to create the main application window and additional popup windows for displaying the solved Sudoku and moves.

tk.Entry: Represents the input cells of the Sudoku board, where users can type in their puzzle.

tk.Button: Creates buttons for "Solve," "Exit," and "Show Moves" actions.

tk.Label: Used to display the Sudoku puzzle, solved puzzle, and moves in the GUI.

bind method: This is used to handle keypress events for the input cells, ensuring that only one character (digit) is allowed per cell and automatically moving to the next cell.

Dependencies
The application requires Python 3 and the Tkinter library, which is included in the standard library for Python 3. No additional external dependencies are needed.

How to Use
Clone the repository to your local machine.

Run the main.py script using Python 3.

A GUI window will appear with a 9x9 grid for input.

Enter the unsolved Sudoku puzzle by typing numbers into the cells. Use the "Backspace" key to clear a cell.

Press the "Solve" button to find the solution to the puzzle.

If a solution is found, a new window will appear displaying the solved puzzle and the moves made by the algorithm.

Optionally, click the "Show Moves" button to view the moves made by the backtracking algorithm.

To exit the application, press the "Exit" button.

Conclusion
The Sudoku Solver GUI with backtracking algorithm is a useful tool for interactively solving Sudoku puzzles. It demonstrates the application of data structures and algorithms (DSA) principles, specifically the backtracking algorithm, to efficiently solve complex puzzles. The code follows the principles of Object-Oriented Programming (OOPS) and utilizes Tkinter properties to create an intuitive and user-friendly graphical interface.

Feel free to use, modify, and distribute this application as needed, and have fun solving Sudoku puzzles with the help of this GUI! If you encounter any issues or have suggestions for improvements, please feel free to raise an issue or submit a pull request. Happy Sudoku solving!
