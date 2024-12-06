"""
Day 4: Ceres Search
"""

import sys
import os
import re
import functools as ft
import numpy as np

sys.path.append(os.path.abspath(".."))

import utils.file_reader as fr

def diag_walk(N=140):
  for a in range(N):
    for b in range (a + 1):
      yield a - b, b
  for a in range(N - 1):
    for b in range(N - a - 1):
      yield N - b - 1, b + 1 + a


if __name__ == "__main__":
  parse_exp = re.compile(r".*")
  puzzle_data = fr.read_file("../puzzle_inputs/04.dat")

  puzzle_data = np.array([list(l) for l in puzzle_data])

  SEARCH = "(?=(XMAS)|(SAMX))"

  # Input matrix is always squared
  # Columns
  N = len(puzzle_data[0])
  # Rows
  M = N

  find = re.compile(SEARCH)

  # Horizontal matches
  HORIZONTAL_MATCHES = 0
  VERTICAL_MATCHES = 0
  DIAGONAL_FW_MATCHES = 0
  DIAGONAL_BW_MATCHES = 0

  for line in puzzle_data:
    matches = find.finditer("".join(line))
    HORIZONTAL_MATCHES += len(list(matches))
  print(f"HZM: {HORIZONTAL_MATCHES}")

  for column in range(N):
    vertical = "".join([line[column] for line in puzzle_data])
    matches = find.finditer(vertical)
    VERTICAL_MATCHES += len(list(matches))
  print(f"VTM: {VERTICAL_MATCHES}")

  N_OF_DIAGS = M + N - 1
  print("N_OF_DIAGS", N_OF_DIAGS)

  diagonal_coordinates = list(diag_walk(N))
  diagonals = []
  aux_len = len(diagonal_coordinates)
  for take in range(N):
    diagonals.append(diagonal_coordinates[0:take + 1])
    diagonals.append(diagonal_coordinates[aux_len - take - 1:aux_len])
    diagonal_coordinates = diagonal_coordinates[take + 1:aux_len - take - 1]
    aux_len = len(diagonal_coordinates)

  diagonals = diagonals[0:len(diagonals) - 1]

  diagonal_strings = [
    ft.reduce(lambda a, x: a + puzzle_data[x[0]][x[1]], d, "")
    for d
    in diagonals
  ]

  for s in diagonal_strings:
    matches = find.findall(s)
    DIAGONAL_FW_MATCHES += len(matches)
  print(f"DFW: {DIAGONAL_FW_MATCHES}")

  flip_puzzle_data = np.flip(puzzle_data, axis=1)

  diagonal_strings_bw = [
    ft.reduce(lambda a, x: a + flip_puzzle_data[x[0]][x[1]], d, "")
    for d
    in diagonals
  ]

  for s in diagonal_strings_bw:
    matches = find.findall(s)
    DIAGONAL_BW_MATCHES += len(matches)
  print(f"DBW: {DIAGONAL_BW_MATCHES}")

  pzzl_ans = ft.reduce(lambda a, x: a + x, [HORIZONTAL_MATCHES, VERTICAL_MATCHES, DIAGONAL_FW_MATCHES, DIAGONAL_BW_MATCHES], 0)

  print(pzzl_ans) # 2483
