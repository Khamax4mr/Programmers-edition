def solution(lines):
  assert len(lines) == 3
  assert all(len(line) == 2 and -100 <= line[0] < line[1] <= 100 for line in lines)

  filled = [set(range(line[0], line[1])) for line in lines]
  return len((filled[0] & filled[1]) | (filled[1] & filled[2]) | (filled[0] & filled[2]))