def solution(array):
  assert 1 <= len(array) <= 100
  assert all(0 <= n <= 1000 for n in array)

  max_n = max(array)
  return [max_n, array.index(max_n)]