import sys

N, M, B = map(int, sys.stdin.readline().strip().split())
matrix = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

num_dic = {}
for y in range(N):
    for x in range(M):
        height = matrix[y][x]
        if height in num_dic:
            num_dic[height] += 1
        else:
            num_dic[height] = 1

def checkAllCase(target_height, num_dic, B):
    time = 0
    blocks = B
    for height, count in num_dic.items():
        if height > target_height:
            time += (height - target_height) * 2 * count
            blocks += (height - target_height) * count
        elif height < target_height:
            time += (target_height - height) * count
            blocks -= (target_height - height) * count
    return (time, blocks >= 0) 

best_time = sys.maxsize
best_height = 0

for target_height in range(min(num_dic), max(num_dic) + 1):
    time, is_possible = checkAllCase(target_height, num_dic, B)
    if is_possible and (time < best_time or (time == best_time and target_height > best_height)):
        best_time = time
        best_height = target_height

print(best_time, best_height)
