def solution(numbers, our_score, score_list):
  assert 1 <= len(numbers) <= 10
  assert 1 <= len(our_score) <= 10
  assert 2 <= len(score_list) <= 31
  assert len(set(numbers)) == len(numbers) == len(our_score)
  assert all(1 <= n <= 31 for n in numbers)
  assert all(0 <= score <= 100 for score in our_score)
  assert all(0 <= score <= 100 for score in score_list)

  answer = []
  for i in range(len(numbers)):
    if our_score[i] == score_list[numbers[i]-1]:
      answer.append("Same")
    else:
      answer.append("Different")
  return answer