def solution(s):
  assert 0 < len(s) < 1000
  assert s.islower()

  return "".join(sorted(i for i in set(s) if s.count(i) == 1))