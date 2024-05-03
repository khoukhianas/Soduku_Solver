import tkinter as tk
import random

def is_valid(board):
    invalid_cells = set()
    for i in range(9):
        ligne = set()
        col = set()
        sgrid = set() 

        for j in range(9):
            if board[i][j] == ' ':
                invalid_cells.add((i, j))

            if board[i][j] != ' ' and board[i][j] in ligne:
                invalid_cells.add((i, j))
            ligne.add(board[i][j])

            if board[j][i] != ' ' and board[j][i] in col:
                invalid_cells.add((j, i))
            col.add(board[j][i])

            row_index = 3 * (i // 3)
            col_index = 3 * (i % 3)
            if board[row_index + j // 3][col_index + j % 3] != ' ' and board[row_index + j // 3][col_index + j % 3] in sgrid:
                invalid_cells.add((row_index + j // 3, col_index + j % 3))
            sgrid.add(board[row_index + j // 3][col_index + j % 3])

    return len(invalid_cells) == 0, invalid_cells


def check_validity():
    sudoku_board = []
    for i in range(9):
        row = []
        for j in range(9):
            cell_value = widgets_de_saisie[i][j].get()
            if cell_value.isdigit() and 1 <= int(cell_value) <= 9:
                row.append(int(cell_value))
            else:
                row.append(' ')
        sudoku_board.append(row)

    is_valid_board, invalid_cells = is_valid(sudoku_board)

    if is_valid_board:
        resultat.config(text="Le Sudoku est valide.", fg="green")
    else:
        resultat.config(text="Le Sudoku n'est pas valide.", fg="red")
        for i in range(9):
            for j in range(9):
                if (i, j) in invalid_cells:
                    widgets_de_saisie[i][j].config(bg="red")
                else:
                    widgets_de_saisie[i][j].config(bg="white")


def clear_board():
    for i in range(9):
        for j in range(9):
            widgets_de_saisie[i][j].delete(0, 'end')
            widgets_de_saisie[i][j].config(bg="white")


def load_example():
    example_board = [
        [5, 3, 4, 6, 7, 8, 9, 1, 2],
        [6, 7, 2, 1, 9, 5, 3, 4, 8],
        [1, 9, 8, 3, 4, 2, 5, 6, 7],
        [8, 5, 9, 7, 6, 1, 4, 2, 3],
        [4, 2, 6, 8, 5, 3, 7, 9, 1],
        [7, 1, 3, 9, 2, 4, 8, 5, 6],
        [9, 6, 1, 5, 3, 7, 2, 8, 4],
        [2, 8, 7, 4, 1, 9, 6, 3, 5],
        [3, 4, 5, 2, 8, 6, 1, 7, 9]
    ]

    clear_board()
    for i in range(9):
        for j in range(9):
            widgets_de_saisie[i][j].insert(0, str(example_board[i][j]))

def on_value_change(event):
    # Fonction appelée lorsqu'une valeur dans un champ de saisie change
    check_validity()


master = tk.Tk()
master.title("Sudoku")

widgets_de_saisie = []
for i in range(9):
    widgets_de_ligne = []
    for j in range(9):
        saisie = tk.Entry(master, width=4)
        saisie.grid(row=i, column=j)
        saisie.bind('<KeyRelease>', on_value_change)  # Lier l'événement de relâchement de touche à la fonction on_value_change
        widgets_de_ligne.append(saisie)
    widgets_de_saisie.append(widgets_de_ligne)

check_button = tk.Button(master, text="Vérifier", command=check_validity)
check_button.grid(row=9, columnspan=9)

load_example_button = tk.Button(master, text="Charger exemple", command=load_example)
load_example_button.grid(row=11, columnspan=9)

resultat = tk.Label(master, text="")
resultat.grid(row=12, columnspan=11)

sudoku_board = [[' ' for _ in range(9)] for _ in range(9)]

master.mainloop()
