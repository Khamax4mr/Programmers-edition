def solution(keyinput, board):
  dir = {"up": (0, 1), "down": (0, -1), "left": (-1, 0), "right": (1, 0)}
  assert 0 <= len(keyinput) <= 50
  assert all(key in dir.keys() for key in keyinput)
  assert len(board) == 2
  assert 1 <= board[0] <= 99 and board[0] % 2
  assert 1 <= board[1] <= 99 and board[1] % 2

  pos, scope = [0, 0], [board[0]//2, board[1]//2]
  for key in keyinput:
    pos[0] = max(-scope[0], min(pos[0] + dir[key][0], scope[0]))
    pos[1] = max(-scope[1], min(pos[1] + dir[key][1], scope[1]))
  return pos