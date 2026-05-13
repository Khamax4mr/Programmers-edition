def solution(quiz):
  assert 1 <= len(quiz) <= 10

  return ["O" if eval(expr.replace("=", "==")) else "X" for expr in quiz]