def solution(sides):
  assert len(sides) == 2
  assert all(1 <= side <= 1000 and str(side).isdigit() for side in sides)

  return 2 * min(sides) - 1