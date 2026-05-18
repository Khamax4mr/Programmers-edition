def solution(n):
  assert 2 <= n <= 10000

  primes = []
  for i in range(2, n+1):
    if n in primes: break
    if n % i: continue
    while not n % i: n //= i
    primes.append(i)

  return primes