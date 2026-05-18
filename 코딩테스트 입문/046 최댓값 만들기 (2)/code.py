def solution(numbers):
  assert 2 <= len(numbers) <= 100
  assert all(-10000 <= n <= 10000 for n in numbers)
  
  pos = sorted([n for n in numbers if n >= 0], reverse=True)
  neg = sorted([n for n in numbers if n <= 0], reverse=True)

  cands = []
  if len(pos) >= 2: cands.append(pos[0] * pos[1])
  if len(neg) >= 2: cands.append(neg[0] * neg[1])
  if pos and neg: cands.append(pos[0] * neg[0])
  return max(cands)