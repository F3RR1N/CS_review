# Sudoku Project
# Ryan Ferrin
# WPI CS5007 F19
# 10/30/2019
#
#  This code will open a given .csv file with a 9 X 9 table that represents a sudoku puzzle.
#  it will find the solution for the puzzle and return the solution and save a csv file of the solution
#  The given puzzle must have a valid solution i.e. no given errors

import numpy as np
from sys import argv

#  this function  uses numpy to open a given.csv and save as 2D array
def read_puzzle(filename):
    board = np.genfromtxt(filename, dtype=int, delimiter=';')

    # numpy reads empty cells as -1 for visual clarity change to 0
    for i in range(0, len(board)):
        for j in range(0, len(board[i])):
            if board[i][j] == -1:
                board[i][j] = 0

    return board


# function to create a more aesthetic board representation
def show_board(board):
    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print('--' * 10)
        for j in range(len(board)):
            if j % 3 == 0 and j != 0:
                print('|', end='')
            if j == 8:
                print(str(board[i][j]) + ' ')
            else:
                print(str(board[i][j]) + ' ', end='')


# this function finds the next unassigned element by fining zero values returns the position coordinates
def find_next(board):
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == 0:
                return i, j
    return None


#function to check if a value is valid given the rest of the board
def guess_value(board, value, position):
    # check row
    for j in range(len(board[0])):
        if board[position[0]][j] == value and position[1] != j:
            return False

    # check columnn
    for i in range(len(board[0])):
        if board[i][position[1]] == value and position[0] != i:
            return False

    # check block
    bloc_x = position[1] // 3
    bloc_y = position[0] // 3
    for i in range(bloc_y * 3, bloc_y * 3 + 3):
        for j in range(bloc_x * 3, bloc_x * 3 + 3):
            if board[i][j] == value and (i, j) != position:
                return False

    return True

# recursive function to find valid values this is a backtracking approach
def solve(board):
    # find the next open cell if no open cells solution is complete
    position = find_next(board)
    if not position:
        return True
    # try a value until solution is valid or an invalid value is found then backtrack
    for n in range(1, 10):
        if guess_value(board, n, position):
            board[position[0]][position[1]] = n
            if solve(board):
                return True
            board[position[0]][position[1]] = 0

    return False

# this function preserves the unsolved puzzle and generates a solved board saves the result to a given csv file
def sudoku_solution(board, filename):
    solved_puzzle = board * 1
    solve(solved_puzzle)
    np.savetxt(filename, solved_puzzle, delimiter=';')
    return solved_puzzle


def main():
    open_file = argv[1]
    save_file = argv[2]
    display = argv[3]
    puzzle = read_puzzle(open_file)
    solution = sudoku_solution(puzzle, save_file)
    print('solution saved to' + save_file )
    if display == 'True':
        print('unsolved puzzle board')
        print(show_board(puzzle))
        print('solved puzzle board')
        print(show_board(solution))

if __name__ == "__main__":
    main()
