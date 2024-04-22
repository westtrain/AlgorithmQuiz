import sys

answer_list = []
while True:
  num1, num2 = list(map(int, sys.stdin.readline().split()))
  if num1 == 0 and num2 == 0:
    break
  if num1 > num2:
    answer_list.append('Yes')
  else:
    answer_list.append('No')
for answer in answer_list:
  print(answer)
