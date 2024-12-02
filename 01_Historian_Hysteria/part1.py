import sys, os, re
sys.path.append(os.path.abspath(".."))

import functools as ft
import utils.file_reader as fr

parse_exp = re.compile("^(\d+)\s+(\d+)$")
puzzle_data = fr.read_file("../puzzle_inputs/01.dat", parse_exp)

l_col = sorted(list(map(lambda x: int(x[0]), puzzle_data)))
r_col = sorted(list(map(lambda x: int(x[1]), puzzle_data)))

def ans_reduce(a, x):
  print(f"{a} + abs({l_col[x]} - {r_col[x]}) = {a + abs(l_col[x] - r_col[x])}")
  return a + abs(l_col[x] - r_col[x])

pzzl_ans = ft.reduce(ans_reduce, range(len(l_col)), 0)

print(pzzl_ans)