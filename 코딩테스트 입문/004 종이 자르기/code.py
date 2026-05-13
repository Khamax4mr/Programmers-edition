def solution(m, n):
  assert 0 < m < 100
  assert 0 < n < 100

  m, n = max(m, n), min(m, n)
  return (m-1) + (n-1)*m