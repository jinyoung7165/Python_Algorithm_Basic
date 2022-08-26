#치킨 TOP N
#N개의 치킨 수치를 무작위로 놓고->N/2명이 2개의 치킨을 선택해 정렬
#N/8->N/16명이 정렬하다가 마지막 사람이 두 개의 정렬된 그룹을 합병
#현재 단계에서 k명의 회원이 정렬을 진행할 때 결과를 출력
n = int(input())
arr = list(map(int, input().split()))
k = int(input())

for i in range(0, n-n//k + 1, n//k):
    arr[i:i+n//k] = sorted(arr[i:i+n//k])
print(*arr)