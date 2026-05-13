def solution(common):
  assert 2 <= len(common) <= 1000
  assert all(-1000 < n < 2000 and isinstance(n, int) for n in common)

  if common[0] + common[2] == common[1] * 2:
    return common[-1] + common[1] - common[0]
  else:
    return common[-1] * common[1] // common[0]