def solution(str1, str2):
  assert 1 <= len(str1) <= 100
  assert 1 <= len(str2) <= 100
  assert str1.isalnum() and str2.isalnum()

  return 2 - (str2 in str1)