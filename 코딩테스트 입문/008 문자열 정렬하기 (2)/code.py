def solution(my_string):
  assert 0 < len(my_string) < 100

  return "".join(sorted(my_string.lower()))