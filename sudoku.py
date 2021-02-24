grid = [
  [5, 3, 0, 0, 7, 0, 0, 0, 0],
  [6, 0, 0, 1, 9, 5, 0, 0, 0],
  [0, 9, 8, 0, 0, 0, 0, 6, 0],
  [8, 0, 0, 0, 6, 0, 0, 0, 3],
  [4, 0, 0, 8, 0, 3, 0, 0, 1],
  [7, 0, 0, 0, 2, 0, 0, 0, 6],
  [0, 6, 0, 0, 0, 0, 2, 8, 0],
  [0, 0, 0, 4, 1, 9, 0, 0, 5],
  [0, 0, 0, 0, 8, 0, 0, 0, 0]]

import numpy as np  

# print(np.matrix(grid))


def possible_single(sudoku, y, x, n):
  for i in range(0, 9):
    if sudoku[y][i] == n:
      return False
  
  for i in range(0, 9):
    if sudoku[i][x] == n:
      return False 
  
  y_start = (y // 3) * 3
  x_start = (x // 3) * 3
  
  for i in range(0, 3):
    for j in range(0, 3):
      if sudoku[y_start + i][x_start + j] == n:
        return False
  
  return True


def solve(sudoku):
  for y in range(9):
    for x in range(9):
      if sudoku[y][x] == 0:
        for n in range(1, 10):
          if possible_single(sudoku, y, x, n):
            sudoku[y][x] = n
            solve(sudoku)
            sudoku[y][x] = 0
        return
  print(np.matrix(sudoku))
  # input("")


solve(grid)

# print(possible_single(4, 4, 6))