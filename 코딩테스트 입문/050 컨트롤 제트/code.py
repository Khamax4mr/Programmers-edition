def solution(s):
  assert 1 <= len(s) <= 200
  assert s[0] != "Z"

  total = 0
  for i in range(len(s := s.split())):
    total += int(s[i]) if s[i] != "Z" else -int(s[i-1])
  return total