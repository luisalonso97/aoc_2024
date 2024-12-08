"""
Day 5: Print Queue
"""

import sys
import os
import functools as ft
from pipe import map as pmap
from collections import defaultdict

sys.path.append(os.path.abspath(".."))

import utils.file_reader as fr

def ans_reduce(rules, a, x):
  for i in range(1, len(x)):
    for j in range(0, i):
      if x[i] not in rules[x[j]]:
        return a
  return a + x[len(x) // 2]

def create_rules_dict(rules):
  rules_dict = defaultdict(list)
  for rule in rules:
    before, after = rule
    rules_dict[before].append(after)
  return rules_dict

def parse_data(data):
  rules = list(
    data[0:data.index("")]
    | pmap(lambda x: x.split("|"))
    | pmap(lambda x: tuple(map(int, x)))
  )
  orders = list(
    data[data.index("") + 1::]
    | pmap(lambda x: x.split(","))
    | pmap(lambda x: list(map(int, x)))
  )
  return (rules, orders)

if __name__ == "__main__":
  puzzle_data = fr.read_file("../puzzle_inputs/05.dat")

  rules, orders = parse_data(puzzle_data)

  rules_dict = create_rules_dict(rules)

  answer = ft.reduce(
    ft.partial(ans_reduce, rules_dict),
    orders, 0
  )

  print(answer)
