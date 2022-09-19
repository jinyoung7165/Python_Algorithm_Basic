#ATM 최적 머지 패턴
from sys import stdin
input = stdin.readline

n = int(input())
p = [int(i) for i in input().split()]

p.sort()
for i in range(1, len(p)):
    p[i] += p[i-1]
    
print(sum(p))