#수 묶기
from sys import stdin
input = stdin.readline

n = int(input())

pos, neg = [], []

result = 0
 
for _ in range(n):
    i = int(input())
    
    if i == 1:
        result += i
    elif i < 1:
        neg.append(i)
    else:
        pos.append(i)
pos.sort(reverse=True)
neg.sort()

for i in range(0, len(pos)-1, 2):
    result += pos[i] * pos[i+1]
if len(pos) % 2 != 0:
    result += pos[-1]
    
for i in range(0, len(neg)-1, 2):
    result += neg[i] * neg[i+1]
if len(neg) % 2 != 0:
    result += neg[-1]
    
print(result)