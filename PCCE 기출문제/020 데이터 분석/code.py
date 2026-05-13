def solution(data, ext, val_ext, sort_by):
  key = ["code", "date", "maximum", "remain"]
  assert 1 <= len(data) <= 500
  assert all((1 <= line[0] <= 100000) and (20000101 <= line[1] <= 29991231) and
             (1 <= line[3] <= line[2] <= 10000) for line in data)
  assert ext in key
  assert sort_by in key
  assert (ext != "code") or (1 <= val_ext <= 100000)
  assert (ext != "date") or (20000101 <= val_ext <= 29991231)
  assert (ext != "maximum") or (1 <= val_ext <= 10000)
  assert (ext != "remain") or (1 <= val_ext <= 10000)

  id = {item: i for i, item in enumerate(key)}
  return sorted([line for line in data if line[id[ext]] < val_ext], key=lambda x: x[id[sort_by]])