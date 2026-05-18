def solution(board):
  n = len(board)
  assert all(len(line) == n and all(e in [0, 1] for e in line) for line in board)

  scope = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
  for y, line in enumerate(board):
    for x, _ in enumerate(line):
      if board[y][x] != 1: continue
      for i, j in scope:
        if not 0 <= y+i < n or not 0 <= x+j < n: continue
        if board[y+i][x+j]: continue
        board[y+i][x+j] = 2
  
  return sum(line.count(0) for line in board)