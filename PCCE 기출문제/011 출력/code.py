def solution():
  string_msg = "Spring is beginning"
  int_val = 3
  string_val = "3"
  print(string_msg)
  print(int_val + 10)
  print(string_val + "10")

  # 테스트 드라이버 실행용 리턴문.
  return f"{string_msg}\n{int_val+10}\n{string_val}10".splitlines()