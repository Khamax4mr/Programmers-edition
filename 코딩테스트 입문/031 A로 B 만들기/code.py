def solution(before, after):
  assert 0 < len(before) == len(after) < 1000
  assert before.islower() and after.islower()

  return sorted(before) == sorted(after)