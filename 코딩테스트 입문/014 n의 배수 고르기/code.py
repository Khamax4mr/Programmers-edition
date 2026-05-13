def solution(n, numlist):
  assert 1 <= n <= 10000
  assert 1 <= len(numlist) <= 100
  assert all(1 <= num <= 100000 for num in numlist)

  return [num for num in numlist if not num % n]