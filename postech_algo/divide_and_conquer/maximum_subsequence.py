tests = int(input())

for test in range(tests):
  input()
  numbers = input().split(" ")
  numbers = [int(number) for number in numbers]

  minimum = min(numbers)

  max_slice = numbers[0]
  max_end = numbers[0]

  for number in numbers[1:]:
    max_end = max(number, max_end + number)
    max_slice = max(max_end, max_slice)

  print(max_slice)
