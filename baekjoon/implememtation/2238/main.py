import sys

U, N = list(map(int, sys.stdin.readline().strip().split()))
bids = {}

for _ in range(N):
    name, price = sys.stdin.readline().strip().split()
    price = int(price)

    if price not in bids:
        bids[price] = [name]
    else:
        bids[price].append(name)

# 가장 적은 수의 사람이 제시한 가격 중 최소 가격 찾기
min_count = N + 1
min_price = 0
for price, names in bids.items():
    if 1 <= len(names) < min_count:
        min_count = len(names)
        min_price = price
    elif len(names) == min_count:
        min_price = min(min_price, price)

# 낙찰자 찾기
winner_name = bids[min_price][0]
print(winner_name, min_price)

