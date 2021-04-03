#특정 위치의 집에 한 개의 안테나 설치
#안테나로부터 모든 집까지의 거리의 합이 최소
#동일한 위치에 여러집 존재 가능
n = int(input())
a = list(map(int, input().split()))
a.sort()

# 중간값(median)을 출력
print(a[(n - 1) // 2])