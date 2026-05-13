def count_k(n, k):
  count = 0

  for i in range(0, len(str(n))):
    p = 10**i
    high, low = n // (p*10), n % p
    cur = (n // p) % 10

    if k == 0 and high == 0: break
    else:
      count += (high - (k == 0)) * p
      if cur > k: count += p
      elif cur == k: count += low + 1

  return count


def solution(i, j, k):
  assert 1 <= i < j <= 100000
  assert 0 <= k <= 9
  
  return count_k(j, k) - count_k(i-1, k)