def solution(cipher, code):
  assert 1 <= code <= len(cipher) <= 1000

  return "".join(cipher[i] for i in range(code-1, len(cipher), code))