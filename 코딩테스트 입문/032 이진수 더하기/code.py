from re import fullmatch

def solution(bin1, bin2):
  pattern = r"0|1[01]*"
  assert 1 <= len(bin1) <= 10
  assert 1 <= len(bin2) <= 10
  assert fullmatch(pattern, bin1) and fullmatch(pattern, bin2)

  return format(int(bin1, 2) + int(bin2, 2), 'b')