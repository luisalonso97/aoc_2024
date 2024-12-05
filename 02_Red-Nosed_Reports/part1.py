"""
Day 2: Red-Nosed Reports
"""

import sys
import os
import re
import functools as ft

sys.path.append(os.path.abspath(".."))

import utils.file_reader as fr

def is_safe_inc(xa, xb):
  if 1 <= abs(xb - xa) <= 3:
    return True
  return False

def is_safe_sym(xa, xb):
  return 1 if (xb - xa) > 0 else -1

def is_valid(xs):
  sym_check = None
  for ix in range(len(xs) - 1):
    curr_n = xs[ix]
    next_n = xs[ix + 1]
    if not sym_check:
      sym_check = is_safe_sym(curr_n, next_n)
    if (not is_safe_inc(curr_n, next_n)) or \
      (sym_check != is_safe_sym(curr_n, next_n)):
      return ix
  return -1

def ans_reduce(a, x):
  return a + 1 if is_valid(x) == -1 else a

if __name__ == "__main__":
  parse_exp = re.compile(r"(\d+)+")
  puzzle_data = fr.read_file("../puzzle_inputs/02.dat", parse_exp, re.findall)

  for i, l in enumerate(puzzle_data):
    puzzle_data[i] = list(map(int, l))

  puzzl_ans = ft.reduce(ans_reduce, puzzle_data, 0)

  print(puzzl_ans)
