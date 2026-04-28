def solution(start, before, after):
  # 코딩 테스트 전용 입력문.
  # start = int(input())
  # before = int(input())
  # after = int(input())

  money = start
  month = 1
  while money < 70:
    money += before
    month += 1
  while money < 100:
    money += after
    month += 1
  print(month)

  # 테스트 드라이버 실행용 리턴문.
  return month