"""
Day 4: Ceres Search
"""

import sys
import os
import re
import functools as ft

sys.path.append(os.path.abspath(".."))

import utils.file_reader as fr


if __name__ == "__main__":
  parse_exp = re.compile(r".*")
  puzzle_data = fr.read_file("../puzzle_inputs/04.dat", parse_exp)

  print(puzzle_data)


  # pzzl_ans = ft.reduce(ans_reduce, casted_input, 0)

  # print(pzzl_ans)
