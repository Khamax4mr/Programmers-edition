def solution(my_string, num1, num2):
  assert 1 < len(my_string) < 100
  assert 0 <= num1 < len(my_string)
  assert 0 <= num2 < len(my_string)
  assert num1 != num2

  tokens = list(my_string)
  tokens[num1], tokens[num2] = tokens[num2], tokens[num1]
  return "".join(tokens)