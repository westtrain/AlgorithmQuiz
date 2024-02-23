n = input()
num = int(n)

if num < 5:
  print("PREDAJA")

names = []
result = ''
i = 0
j = 4

while i < num:
  names.append(input())
  i += 1
names.sort()
i = 0
while i <= num:
  if j > num:
    break
  if names[i][0] == names[j][0]:
    result += names[i][0]
    i += 5
    j += 5
  else:
    i += 1
    j += 1

if len(result) == 0:
    result = "PREDAJA"

print(result)
