def solution(code):
  last_four_words = code[-4:]

  if last_four_words == "_eye":
    print("Ophthalmologyc")
    return "Ophthalmologyc" # 테스트 드라이버 실행용 리턴문.
  elif last_four_words == "head":
    print("Neurosurgery")
    return "Neurosurgery"   # 테스트 드라이버 실행용 리턴문.
  elif last_four_words == "infl":
    print("Orthopedics")
    return "Orthopedics"    # 테스트 드라이버 실행용 리턴문.
  elif last_four_words == "skin":
    print("Dermatology")
    return "Dermatology"    # 테스트 드라이버 실행용 리턴문.
  else:
    print("direct recommendation")
    return "direct recommendation"  # 테스트 드라이버 실행용 리턴문.