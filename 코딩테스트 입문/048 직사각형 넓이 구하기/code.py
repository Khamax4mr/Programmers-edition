def solution(dots):
  assert len(dots) == 4
  assert all(len(dot) == 2 and -256 < dot[0] < 256 and -256 < dot[1] < 256 for dot in dots)

  x0, xm, _, x1 = sorted([dot[0] for dot in dots])
  y0, ym, _, y1 = sorted([dot[1] for dot in dots])
  area = (x1 - x0) * (y1 - y0)
  return area // (1 if x0 == xm or y0 == ym else 2)