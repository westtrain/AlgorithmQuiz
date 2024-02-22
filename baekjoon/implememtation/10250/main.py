import sys

T = int(sys.stdin.readline())
for _ in range(T):
    H, W, N = map(int, sys.stdin.readline().split())
    
    floor = N % H
    room = N // H + 1
    
    if floor == 0: 
        floor = H
        room -= 1  
    
    print(f'{floor * 100 + room}'


# 1차 시도
import sys

answer_arr = []
T = int(sys.stdin.readline())
for _ in range(T):
  H, W, N = map(int, sys.stdin.readline().split())
  room_number_arr = []
  for j in range(1, W + 1):
    for i in range(1, H + 1):
      room_num = i * 100 + j
      room_number_arr.append(room_num)
      if len(room_number_arr) == N:
        break
    if len(room_number_arr) == N:
      break
  answer_arr.append(room_number_arr[N - 1])
for ans in answer_arr:
  print(ans))
