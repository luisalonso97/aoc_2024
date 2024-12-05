"""
Day 3: Mull It Over
"""

import sys
import os
import re
import functools as ft

sys.path.append(os.path.abspath(".."))

import utils.file_reader as fr

def mul_line(line):
  return ft.reduce(lambda a, x: a + (x[0] * x[1]), line, 0)

def ans_reduce(a, x):
  return a + mul_line(x)

def cast_pair_toi(p):
  return tuple(int(e) for e in p)

def cast_line_toi(line):
  return [cast_pair_toi(p) for p in line]

if __name__ == "__main__":
  parse_exp = re.compile(r"mul\((\d{1,3}),(\d{1,3})\)")
  puzzle_data = fr.read_file("../puzzle_inputs/03.dat", parse_exp, re.findall)

  casted_input = list(map(cast_line_toi, puzzle_data))

  pzzl_ans = ft.reduce(ans_reduce, casted_input, 0)

  print(pzzl_ans)
