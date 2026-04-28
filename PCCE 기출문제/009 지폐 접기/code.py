def solution(wallet, bill):
  assert len(wallet) == 2
  assert len(bill) == 2
  assert 10 <= wallet[0] <= 100
  assert 10 <= wallet[1] <= 100
  assert 10 <= bill[0] <= 2000
  assert 10 <= bill[1] <= 2000

  wallet_w, wallet_h = sorted(wallet)
  bill_w, bill_h = sorted(bill)
  fold = 0

  while wallet_w < bill_w or wallet_h < bill_h:
    bill_h //= 2
    fold += 1
    if bill_w <= bill_h: continue
    bill_w, bill_h = bill_h, bill_w

  return fold