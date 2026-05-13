def solution(sides):
  assert all(1 <= line <= 1000 and str(line).isdigit() for line in sides)
  assert len(sides) == 3

  a, b, c = sorted(sides)
  return 2 - (a + b > c)