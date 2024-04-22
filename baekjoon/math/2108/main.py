import sys

N = int(sys.stdin.readline().strip())

num_arr = []
num_dic = {}
frequncy_num_arr = []
frequncy_num = 0
exist_num = 0

for _ in range(N):
  input_number = int(sys.stdin.readline().strip())
  num_arr.append(input_number)
  if input_number in num_dic:
    num_dic[input_number] += 1
  else:
    num_dic[input_number] = 1
    
num_arr.sort()

print(round(sum(num_arr)/N))
print(num_arr[N//2])

frequncy_num = max(num_dic.values())
for key, value in num_dic.items():
  if value == frequncy_num:
    frequncy_num_arr.append(key)
frequncy_num_arr.sort()

exist_num = frequncy_num_arr[1] if len(frequncy_num_arr) > 1 else frequncy_num_arr[-1]

print(exist_num)
print(num_arr[-1] - num_arr[0])
