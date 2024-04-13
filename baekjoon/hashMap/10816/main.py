import sys
from collections import Counter

N = int(sys.stdin.readline().strip())
deck = list(map(int, sys.stdin.readline().strip().split()))

M = int(sys.stdin.readline().strip())
player_card_number = list(map(int, sys.stdin.readline().strip().split()))

deck_counts = Counter(deck)

for player_number in player_card_number:
    print(deck_counts[player_number], end=' ')
print()
