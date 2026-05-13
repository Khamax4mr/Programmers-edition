def solution(dots):
  assert len(dots) == 4
  assert all(str(abs(x)).isdigit() and str(abs(y)).isdigit() for x, y in dots)

  a, b, c, d = dots
  grad1 = (a[0]-b[0]) / (a[1]-b[1]) == (c[0]-d[0]) / (c[1]-d[1])
  grad2 = (a[0]-c[0]) / (a[1]-c[1]) == (b[0]-d[0]) / (b[1]-d[1])
  grad3 = (a[0]-d[0]) / (a[1]-d[1]) == (b[0]-c[0]) / (b[1]-c[1])
  return int(grad1 or grad2 or grad3)