def solution(year, age_type):
  # 코딩 테스트 전용 입력문.
  # year = int(input())
  # age_type = input()

  if age_type == "Korea":
    answer = 2030 - year + 1
  elif age_type == "Year":
    answer = 2030 - year
  print(answer)

  # 테스트 드라이버 실행용 리턴문.
  return answer