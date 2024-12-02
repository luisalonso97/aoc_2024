import re

def read_file(f_name, parse_exp=None):
  with open(f_name) as f:
    lines = [line.rstrip() for line in f]
  if parse_exp:
    lines = map(parse_exp.match, lines)
    lines = list(map(lambda x: x.groups(), lines))
  return lines
