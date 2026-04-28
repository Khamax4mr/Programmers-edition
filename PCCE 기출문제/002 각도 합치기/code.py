def solution(angle1, angle2):
  sum_angle = (angle1 + angle2) % 360
  print(sum_angle)

  # 테스트 드라이버 실행용 리턴문.
  return sum_angle