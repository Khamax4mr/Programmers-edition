def solution(storage, num):
  assert 1 <= len(storage) <= 30
  assert 1 <= len(num) <= 30
  assert len(storage) == len(num)
  assert all(1 <= len(item) <= 30 for item in storage)
  assert all(1 <= n <= 20 for n in num)
  assert len({storage[i] for i, v in enumerate(num) if v == max(num)}) == 1

  clean_storage, clean_num = [], []
  for i in range(len(storage)):
    if storage[i] in clean_storage:
      pos = clean_storage.index(storage[i])
      clean_num[pos] += num[i]
    else:
      clean_storage.append(storage[i])
      clean_num.append(num[i])

  max_num = max(clean_num)
  answer = clean_storage[clean_num.index(max_num)]
  return answer