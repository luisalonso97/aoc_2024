"""
Day 2: Red-Nosed Reports
"""

import sys
import os
import re
import functools as ft

sys.path.append(os.path.abspath(".."))

from part1 import is_valid
import utils.file_reader as fr

def ans_reduce(a, x):
  # First try to check if its valid
  first_try = is_valid(x)
  if first_try != -1:
    removed = [
      x[0:first_try - 1] + x[first_try::],
      x[0:first_try - 1] + x[first_try + 1::],
      x[0:first_try + 1] + x[first_try + 2::],
    ]
    # If it's not, then check subsets.
    # At most makes 3 loops.
    if ft.reduce(lambda a, x: a and is_valid(x) != -1,
      removed, True):
      return a
  return a + 1

if __name__ == "__main__":
  parse_exp = re.compile(r"(\d+)+")
  puzzle_data = fr.read_file("../puzzle_inputs/02.dat", parse_exp, re.findall)

  for i, l in enumerate(puzzle_data):
    puzzle_data[i] = list(map(int, l))
  puzzl_ans = ft.reduce(ans_reduce, puzzle_data, 0)

  print(puzzl_ans)
