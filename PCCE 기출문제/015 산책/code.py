def solution(route):
  assert 1 <= len(route) <= 20
  assert all(pos in ["N", "S", "E", "W"] for pos in route)

  east, north = 0, 0
  for i in route:
    if i == "N": north += 1
    elif i == "S": north -= 1
    elif i == "E": east += 1
    elif i == "W": east -= 1
  return [east, north]