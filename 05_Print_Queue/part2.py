"""
Day 5: Print Queue
"""

import sys
import os
import functools as ft
from pyllist import sllist

sys.path.append(os.path.abspath(".."))

import utils.file_reader as fr
from part1 import parse_data, ans_reduce, create_rules_dict

if __name__ == "__main__":
  puzzle_data = fr.read_file("../puzzle_inputs/05.dat")

  rules, orders = parse_data(puzzle_data)

  rules_dict = create_rules_dict(rules)

  def bad_ord_reduce(a, x):
    for i in range(1, len(x)):
      for j in range(0, i):
        if x[i] not in rules_dict[x[j]]:
          a.append(x)
          return a
    return a

  bad_orders = ft.reduce(
    bad_ord_reduce,
    orders, []
  )

  def fix_ord_reduce(a, x):
    fixed = sllist([x.pop(0)])
    while x != []:
      search = x.pop()
      for f in fixed.iternodes():
        if not search in rules_dict[f.value]:
          fixed.insertbefore(f, search)
          break
        elif search in rules_dict[f.value] and f == fixed.last:
          fixed.insertafter(f, search)
          break
    a.append(fixed)
    return a

  fixed_orders = ft.reduce(
    fix_ord_reduce,
    bad_orders, []
  )

  answer = ft.reduce(
    ft.partial(ans_reduce, rules_dict),
    fixed_orders, 0
  )

  print(answer)
