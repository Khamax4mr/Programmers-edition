from re import compile

def solution(spell, dic):
  assert 1 <= len(spell) <= 100
  assert all(len(c) == 1 and c.islower() for c in spell)
  assert 1 <= len(dic) <= 10
  assert all(1 <= len(word) <= 11 for word in dic)
  assert len(spell) == len(set(spell))
  assert len(dic) == len(set(dic))

  pattern = compile("^[" + "".join(spell) + "]{" + str(len(spell)) + "}$")
  return 2 - any(len(word) == len(set(word)) and pattern.match(word) is not None for word in dic)