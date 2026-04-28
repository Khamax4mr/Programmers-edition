def solution(mats, park):
  assert 1 <= len(mats) <= 10
  assert all(1 <= mat <= 20 for mat in mats)
  assert len(mats) == len(set(mats))
  assert 1 <= len(park) <= 50
  assert all(1 <= len(line) <= 50 for line in park)

  r, c = len(park), len(park[0])
  dp = [[0 for _ in range(c)] for _ in range(r)]

  for i in range(r):
    for j in range(c):
      if park[i][j] != "-1": continue
      elif i * j == 0: dp[i][j] = 1
      else: dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])+1

  mat_cands = mats + [-1]
  return max(mat for mat in mat_cands if mat <= max(map(max, dp)))