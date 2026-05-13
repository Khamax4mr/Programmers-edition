def solution(array):
  assert 1 <= len(array) <= 100
  assert all(0 <= e <= 100000 for e in array)

  return sum(str(e).count("7") for e in array)