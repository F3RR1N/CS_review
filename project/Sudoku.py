# Sudoku Project
# Ryan Ferrin
# WPI CS5007 F19
# 10/30/2019
#
#  This code will open a .csv file with a 9 X 9 table that represents a sudoku puzzle.
#  it will find the solution for the puzzle and return the solution

import numpy as np

class Puzzle:
    def __init__(self, filename):
        self.filename = filename
        self.board = np.zeros((9, 9))
        boardArray =[]
        f = open(self.filename, 'r')
        for i in range(0, len(f.readline())):
            boardArray.append(f.readline().split(';'))
        for i in range(0,len(boardArray)):
            for j in range(0,len(boardArray[i])):
                boardArray[i][j] = boardArray[i][j].rstrip('\n')
                if boardArray[i][j] == '':
                    boardArray[i][j] = 0
                else:
                    boardArray[i][j] = int(boardArray[i][j])
        f.close()
        print(boardArray)
        print(len(boardArray))
        for i in range(0, len(self.board)):
            self.board[i, :] = boardArray[i]




puzzle1=Puzzle('sudoku1.csv')
print(puzzle1.board)
print(len(puzzle1.board))
