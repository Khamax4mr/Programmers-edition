def solution(strlist):
  assert all(1 <= len(s) <= 100 for s in strlist)
  return [len(s) for s in strlist]