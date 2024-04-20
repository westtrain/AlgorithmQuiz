import sys
import math

A, B, V = map(int, sys.stdin.readline().split())
days = math.ceil((V - B) / (A - B))

print(days)

'''
로직 설명:
마지막 날은 미끄러지지 않으므로, V - B 만큼만 올라가면 됩니다.
매일 A - B 만큼 실제로 "순수하게" 올라갑니다.
(V - B)를 (A - B)로 나눈 값이 실제 필요한 일수가 됩니다.
math.ceil을 사용하여 올림 처리를 함으로써, 부분적인 날도 전체 하루로 계산합니다.
'''
