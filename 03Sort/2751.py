#백준 2751 - 수 정렬하기2
#N개의 수가 주어졌을 때, 오름차순으로 정렬
n = int(input())
arr = []
for _ in range(n):
    arr.append(int(input()))
for i in sorted(arr):
    print(i)