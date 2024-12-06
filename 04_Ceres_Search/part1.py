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

def diag_walk(N):
  for a in range(N):
    for b in range (a + 1):
      yield a - b, b
  for a in range(N - 1):
    for b in range(N - a - 1):
      yield N - b - 1, b + 1 + a

def build_diagonals(walk, N):
  diagonals = []
  aux_len = len(walk)
  for take in range(N):
    diagonals.append(walk[0:take + 1])
    diagonals.append(walk[aux_len - take - 1:aux_len])
    walk = walk[take + 1:aux_len - take - 1]
    aux_len = len(walk)
  return diagonals

def build_diag_strs(diagonals, data):
  def concat_lkp(a, coord):
    x, y = coord
    return a + data[x, y]
  return [
    ft.reduce(concat_lkp, diagonal, "")
    for diagonal in diagonals
  ]

def find_xmas(x):
  # Regex search
  SEARCH = r"(?=(XMAS)|(SAMX))"
  find = re.compile(SEARCH)
  return len(find.findall("".join(x)))

if __name__ == "__main__":
  puzzle_data = fr.read_file("../puzzle_inputs/04.dat")
  puzzle_data = np.array([list(line) for line in puzzle_data])

  N = len(puzzle_data)

  # Create the diagonal strings
  diagonal_walk = np.array(list(diag_walk(N)))
  diagonals = build_diagonals(diagonal_walk, N)
  diagonals = diagonals[0:len(diagonals) - 1] # Remove unnecesary elements
  diagonals_strings = \
    build_diag_strs(diagonals, puzzle_data) + \
    build_diag_strs(diagonals, np.flip(puzzle_data, axis = 1))
  
  # Create the flat strings
  flat_strings = np.concatenate((puzzle_data, np.rot90(puzzle_data, k = -1)))

  reduce_matches = lambda a, x: a + find_xmas(x)
  pzzl_ans = sum([
    ft.reduce(reduce_matches, flat_strings, 0),
    ft.reduce(reduce_matches, diagonals_strings, 0),
  ])

  print(pzzl_ans)
