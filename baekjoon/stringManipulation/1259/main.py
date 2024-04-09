import sys

isPalindrome = []
while True:
  pre_index = 0
  string_number = sys.stdin.readline().strip()
  if string_number == "0":
    break
  post_index = len(string_number) - 1
  while pre_index < post_index:
    if string_number[pre_index] != string_number[post_index]:
      isPalindrome.append('no')
      break
    pre_index += 1
    post_index -= 1
  if pre_index >= post_index:
    isPalindrome.append('yes')

for answer in isPalindrome:
  print(answer)
