def solution(numlist, n):
  assert 1 <= n <= 10000
  assert 1 <= len(numlist) == len(set(numlist)) <= 100
  assert all(1 <= num <= 10000 for num in numlist)

  return sorted(numlist, key=lambda x: (abs(x - n), -x))