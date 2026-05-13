def solution(num, k):
  assert 0 <= num <= 1000000
  assert 0 <= k < 10

  return str(num).find(str(k)) + (str(k) in str(num))