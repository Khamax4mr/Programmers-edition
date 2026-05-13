from math import sqrt

def solution(n):
  assert 1 <= n <= 1000000

  return 2 - sqrt(n).is_integer()