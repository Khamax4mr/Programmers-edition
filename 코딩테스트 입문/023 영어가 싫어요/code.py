def solution(numbers):
  assert numbers.lower()
  assert 1 <= len(numbers) <= 50

  tokens = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
  for n, word in enumerate(tokens):
    numbers = numbers.replace(word, str(n))

  return int(numbers)