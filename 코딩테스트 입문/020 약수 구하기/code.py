from math import isqrt

def solution(n):
  assert 1 <= n <= 10000

  divisor = set()
  for i in range(1, isqrt(n)+1):
    if n % i: continue
    divisor.add(i)
    divisor.add(n // i)
  return sorted(list(divisor))