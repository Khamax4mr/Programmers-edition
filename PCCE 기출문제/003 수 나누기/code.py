def solution(number):
  answer = 0
  while number:
    answer += number % 100
    number //= 100
  print(answer)

  # 테스트 드라이버 실행용 리턴문.
  return answer