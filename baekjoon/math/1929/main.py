import sys

# 소수 판별 함수
def is_prime(num):
  if num <= 1:  # 1 이하의 수는 소수가 아님
     return False
  if num <= 3:  # 2와 3은 소수
     return True
  if num % 2 == 0 or num % 3 == 0:  # 2나 3으로 나누어 떨어지면 소수가 아님
     return False
  i = 5
  while i * i <= num:  # 제곱근까지만 확인
    if num % i == 0 or num % (i + 2) == 0:
     return False
    i += 6
  return True

M, N = list(map(int, sys.stdin.readline().split()))
for i in range(M, N + 1):
  if is_prime(i):
    print(i)
