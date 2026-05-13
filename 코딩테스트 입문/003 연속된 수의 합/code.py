def solution(num, total):
  assert 1 <= num <= 100
  assert 0 <= total <= 1000
  assert num % 2 == 0 or not total % num
  assert num % 2 == 1 or total % num

  base = total // num - num//2 + (total % num > 0)
  return [base + i for i in range(num)]