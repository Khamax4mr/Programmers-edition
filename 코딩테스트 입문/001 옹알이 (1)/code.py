from re import compile

def solution(babbling):
  words = ("aya", "ye", "woo", "ma")
  assert 1 <= len(babbling) <= 100
  assert all(1 <= len(b) <= 15 and b.islower() and
             not any(b.count(word) > 1 for word in words)
             for b in babbling)

  pattern = compile("^(" + "|".join(words) + ")+$")
  return sum(pattern.match(b) is not None for b in babbling)