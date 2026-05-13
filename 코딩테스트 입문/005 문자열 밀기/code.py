def solution(a, b):
  assert 0 < len(a) < 100
  assert 0 < len(b) < 100
  assert len(a) == len(b)

  return (b + b).find(a)