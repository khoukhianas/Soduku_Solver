# Soduku_Solver GUI

This Python GUI application allows you to input and validate Sudoku puzzles. You can check if the Sudoku board is valid or load an example puzzle to solve.

# Features
Sudoku Input: Enter numbers into the grid to form a Sudoku puzzle.

Validation: Check if the entered Sudoku puzzle is valid.

Example Load: Load a pre-defined Sudoku puzzle for testing.

Real-time Validation: Automatically validate the Sudoku puzzle as you input numbers.

# Prerequisites

Python 3.x

tkinter library (standard with Python)

# Installation

Clone or download the sudoku_solver_gui.py script.

Open a terminal or command prompt.

Navigate to the directory containing sudoku_solver_gui.py.

Run the script using:

python sudoku_solver_gui.py

# Usage

Sudoku Input:

Click on any cell in the grid and type a number (1-9) to fill the cell.

Use the keyboard to navigate between cells.

The puzzle will automatically validate as you type.

# Validation:

Click the "Vérifier" button to validate the current state of the Sudoku puzzle.

Invalid cells will be highlighted in red.

# Load Example:

Click the "Charger exemple" button to load a pre-defined Sudoku puzzle.

The example puzzle will replace any existing input.

# Instructions
Entering Numbers:

Click on a cell in the grid.

Type a number (1-9) on your keyboard.

Press Enter or move to the next cell.

# Notes
Ensure valid Sudoku rules:

Each row, column, and 3x3 subgrid must contain unique numbers from 1 to 9.

Only numbers between 1 and 9 are accepted as valid entries.

Real-time validation helps in identifying errors while inputting.
