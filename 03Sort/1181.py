#단어정렬
#N개 단어 들어오면
#1.길이 오름차순
#2.길이 같으면 사전순
from sys import stdin
input = stdin.readline
n = int(input())
arr = [input().rstrip() for _ in range(n)]
arr = list(set(arr))
arr.sort(key=lambda x:(len(x),x))

for i in arr:
    print(i)

