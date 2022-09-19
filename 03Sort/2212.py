#센서 n 개. 최대 k개의 집중국
#각 집중국의 수신영역 길이(0가능)의 합 최소화
#k=n일 때, 집중국을 센서위치에 세우면 됨
#주어진 센서들을 k개의 구역으로 나눠야 함
#인접 센서 간의 거리(간선) 배열에서 큰 값 k-1개를 제거
from sys import stdin
input = stdin.readline

def main():
    n = int(input())
    k = int(input())
    graph = [int(i) for i in input().split()]

    if n <= k:
        return 0
    graph.sort()
    dist = []
    for i in range(1, n):
        dist.append(graph[i] - graph[i-1])
    dist.sort(reverse=True)
    
    return sum(dist[k-1:]) #간선 중 큰 거 k-1개를 뺌(0~k)
    
    
print(main())