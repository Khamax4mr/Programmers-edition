from re import sub

def solution(my_string):
  assert 1 <= len(my_string) <= 1000
  assert my_string.isalnum()

  pattern = r"[a-zA-Z]"
  return sum(map(int, list(sub(pattern, "", my_string).strip())))