"""
Day 1: Historian Hysteria
"""

import sys
import os
import re

sys.path.append(os.path.abspath(".."))

import functools as ft
import utils.file_reader as fr

def get_similarity_score(a, x):
  if x in a:
    a[x] = a[x] + 1
  else:
    a[x] = 1
  return a

def ans_reduce(r_dict, a, x):
  if x in r_dict:
    return a + (r_dict[x] * x)
  return a

if __name__ == "__main__":
  parse_exp = re.compile(r"^(\d+)\s+(\d+)$")
  puzzle_data = fr.read_file("../puzzle_inputs/01.dat", parse_exp)

  puzzle_data = list(map(lambda x: x.groups(), puzzle_data))

  l_col = sorted(list(map(lambda x: int(x[0]), puzzle_data)))
  r_col = sorted(list(map(lambda x: int(x[1]), puzzle_data)))

  r_dict = ft.reduce(get_similarity_score, r_col, {})

  ans_reduce = ft.partial(ans_reduce, r_dict)

  pzzl_ans = ft.reduce(ans_reduce, l_col, 0)

  print(pzzl_ans)
