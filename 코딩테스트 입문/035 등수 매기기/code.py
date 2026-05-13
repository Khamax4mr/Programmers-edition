def solution(score):
  assert 1 <= len(score) <= 10
  assert all(len(s) == 2 and 0 <= s[0] <= 100 and 0 <= s[1] <= 100 for s in score)

  total = [s[0]+s[1] for s in score]
  rank = {}
  for i, s in enumerate(sorted(total, reverse=True), 1):
    if s in rank: continue
    rank[s] = i

  return [rank[s] for s in total]