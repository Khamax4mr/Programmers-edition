def solution(my_str, n):
  assert 1 <= n <= len(my_str) <= 100
  assert my_str.isalnum()

  return [my_str[i:i+n] for i in range(0, len(my_str), n)]