def solution(my_string):
  assert 1 <= len(my_string) <= 110

  return "".join(dict.fromkeys(my_string))