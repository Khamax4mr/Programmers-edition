from math import gcd

def solution(a, b):
  assert str(a).isdigit() and str(b).isdigit()
  assert 0 < a <= 1000
  assert 0 < b <= 1000

  b //= gcd(a, b)
  while b % 2 == 0: b //= 2
  while b % 5 == 0: b //= 5

  return 2 - (b == 1)