def solution(order):
  assert 1 <= order <= 1000000

  return sum(str(order).count(i) for i in ["3", "6", "9"])