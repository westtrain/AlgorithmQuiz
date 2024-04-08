import sys

N = int(sys.stdin.readline().strip())

users = {}
for _ in range(N):
  age, name = sys.stdin.readline().strip().split()
  age = int(age)
  if age in users:
    users[age].append(name)
  else:
    users[age] = [name]
result = sorted(users.items())
for key, value in result:
  for name in value:
    print(key, name)
