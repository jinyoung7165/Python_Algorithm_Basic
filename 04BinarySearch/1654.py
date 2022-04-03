#백준 1654 - 랜선 자르기
#K개의 랜선을 N개의 같은 길이의 선으로.
#만들 수 있는 최대 랜선의 길이
from sys import stdin
input = stdin.readline
k, n = map(int, input().split())
length = []
for _  in range(k):
    length.append(int(input()))
length.sort()    
left, right = 1, max(length)
result = 0

while(left <= right):
    mid = (left + right) // 2
    count = 0
    for i in length:
        count += (i // mid)
    if count >= n: #충족
        result = max(result, mid)
        left = mid + 1
    else:
        right = mid - 1
print(result)