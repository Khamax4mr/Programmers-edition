def solution(id_pw, db):
  assert len(id_pw) == 2

  id, pw = id_pw
  assert 1 <= len(id) <= 15 and id.isalnum()
  assert 1 <= len(pw) <= 6 and pw.isdigit()
  assert 1 <= len(db) <= 10
  assert all(len(data) == 2 for data in db)
  
  if id_pw in db: return "login"
  elif id in [data[0] for data in db]: return "wrong pw"
  else: return "fail"