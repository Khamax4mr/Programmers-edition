def solution(wallet, bill):
  assert len(wallet) == 2
  assert len(bill) == 2
  assert 10 <= wallet[0] <= 100
  assert 10 <= wallet[1] <= 100
  assert 10 <= bill[0] <= 2000
  assert 10 <= bill[1] <= 2000

  wallet, bill = sorted(wallet), sorted(bill)
  fold = 0

  while wallet[0] < bill[0] or wallet[1] < bill[1]:
    bill[1] //= 2
    bill = sorted(bill)
    fold += 1

  return fold