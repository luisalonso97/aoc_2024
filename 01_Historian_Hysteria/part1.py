"""
Day 1: Historian Hysteria
"""

import sys
import os
import re

sys.path.append(os.path.abspath(".."))

import functools as ft
import utils.file_reader as fr

def ans_reduce(l_col, r_col, a, x):
  return a + abs(l_col[x] - r_col[x])

if __name__ == "__main__":
  parse_exp = re.compile(r"^(\d+)\s+(\d+)$")
  puzzle_data = fr.read_file("../puzzle_inputs/01.dat", parse_exp)

  puzzle_data = list(map(lambda x: x.groups(), puzzle_data))

  l_col = sorted(list(map(lambda x: int(x[0]), puzzle_data)))
  r_col = sorted(list(map(lambda x: int(x[1]), puzzle_data)))

  ans_reduce = ft.partial(ans_reduce, l_col, r_col)

  pzzl_ans = ft.reduce(ans_reduce, range(len(l_col)), 0)

  print(pzzl_ans)
