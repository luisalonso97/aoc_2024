"""
Day 4: Ceres Search
"""

import sys
import os
import numpy as np

sys.path.append(os.path.abspath(".."))

import utils.file_reader as fr

def extract_chrs_from_submatrix(matrix):
  coords = ((0,0), (0,2), (1,1), (2,0), (2,2),)
  chars = []
  for coord in coords:
    x, y = coord
    chars.append(matrix[x, y])
  return "".join(chars)

def check_sub_matrix(sub_matrix):
  VALID_STRINGS = ("MSAMS", "SSAMM", "SMASM", "MMASS",)
  ch_str = extract_chrs_from_submatrix(sub_matrix)
  return True if ch_str in VALID_STRINGS else False

if __name__ == "__main__":
  puzzle_data = fr.read_file("../puzzle_inputs/04.dat")
  puzzle_data = np.array([list(line) for line in puzzle_data])

  N = len(puzzle_data)

  n_x_mas = 0

  for y in range(1, N - 1):
    for x in range(1, N - 1):
      if puzzle_data[x, y] == "A":
        if check_sub_matrix(puzzle_data[x - 1:x + 2, y - 1: y + 2]):
          n_x_mas += 1

print(n_x_mas)
