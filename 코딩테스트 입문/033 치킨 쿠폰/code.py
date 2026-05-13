def solution(chicken):
  assert str(chicken).isdigit()
  assert 0 <= chicken <= 1000000

  bonus_value = sum(1/(10**(i+1)) for i in range(len(str(chicken))))
  return int(chicken * bonus_value)