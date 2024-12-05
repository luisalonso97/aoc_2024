"""
Day 3: Mull It Over
"""

import sys
import os
import re
import functools as ft

sys.path.append(os.path.abspath(".."))

import utils.file_reader as fr

def mul_line(a, x):
  MUL_1   = 0
  MUL_2   = 1
  DO_EX   = 2
  DONT_EX = 3

  acc, flag = a

  if x[DO_EX] == "do()":
    flag = True
  elif x[DONT_EX] == "don't()":
    flag = False
  else:
    if flag:
      mul_a = int(x[MUL_1])
      mul_b = int(x[MUL_2])
      acc += mul_a * mul_b
  return [acc, flag]

def ans_reduce(a, x):
  a = ft.reduce(mul_line, x, a)
  return a

if __name__ == "__main__":
  parse_exp = re.compile(r"mul\((?P<mul_1>\d{1,3}),(?P<mul_2>\d{1,3})\)|(?P<do_flg>do\(\))|(?P<dont_flg>don't\(\))")
  puzzle_data = fr.read_file("../puzzle_inputs/03.dat", parse_exp, re.findall)

  pzzl_ans = ft.reduce(ans_reduce, puzzle_data, [0, True])

  print(pzzl_ans[0])
