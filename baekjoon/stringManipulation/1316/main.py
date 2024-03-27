import sys

N = int(sys.stdin.readline().strip())
strs = [sys.stdin.readline().strip() for _ in range(N)]
count = 0

for word in strs:
    last_seen = {}
    is_group_word = True
    for i, char in enumerate(word):
        if char in last_seen and last_seen[char] != i - 1:
            is_group_word = False
            break
        last_seen[char] = i
    if is_group_word:
        count += 1

print(count)
