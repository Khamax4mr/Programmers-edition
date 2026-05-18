def solution(polynomial):
  coef = [0, 0]
  tokens = polynomial.replace(" + ", " ").split()

  for token in tokens:
    if token.endswith("x"):
      coef[1] += 1 if token == "x" else int(token[:-1])
    else:
      coef[0] += int(token)

  expr = []
  if coef[1]:
    expr.append(("" if coef[1] == 1 else str(coef[1])) + "x")
  if coef[0]:
    expr.append(str(coef[0]))
  return " + ".join(expr)