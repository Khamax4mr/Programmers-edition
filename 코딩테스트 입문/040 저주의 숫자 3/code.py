def solution(n):
  assert 1 <= n <= 100

  pure_n = 0
  for _ in range(n):
    pure_n += 1
    while pure_n % 3 == 0 or "3" in str(pure_n): pure_n += 1

  return pure_n