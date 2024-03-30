import sys

S = sys.stdin.readline().strip()
count = {'0': 0, '1': 0}

# Check the first character and initialize the count.
current_char = S[0]
count[current_char] += 1

# Iterate through the string starting from the second character.
for char in S[1:]:
    # Only increment the count if the current character is different from the last one.
    if char != current_char:
        count[char] += 1
        current_char = char

# The answer is the minimum of the two counts.
answer = min(count.values())
print(answer)

