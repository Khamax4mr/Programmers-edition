def solution(s1, s2):
  assert 1 <= len(s1) == len(set(s1)) <= 100
  assert 1 <= len(s2) == len(set(s2)) <= 100
  assert all(1 <= len(s) <= 10 and s.islower() for s in s1)
  assert all(1 <= len(s) <= 10 and s.islower() for s in s2)

  return len(set(s1) & set(s2))