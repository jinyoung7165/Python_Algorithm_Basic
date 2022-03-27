#백준 1939 - 중량제한
#n개의 섬으로 이뤄진 나라. 몇 개의 섬 사이에는 다리가 설치되어 있어 차들이 다닐 수 있다
#중량제한을 초과하는 양의 물품이 다리를 건너면 안됨
#한 번의 이동에서 옮길 수 있는 물품들의 중량의 최댓값을 구하는 프로그램
#두 섬 사이에 여러 개의 다리도 존재 가능. 양방향
from collections import deque
from sys import stdin
input = stdin.readline

def bs():
    n, m = map(int, input().split()) #섬, 다리 수
    bridge = [[] for _ in range(n+1)]
    low, high = 1, 0  #가능한 무게의 최소, 최대
    for _ in range(m): #a-b, 중량제한 c 다리
        a, b, c = map(int, input().split())
        bridge[a].append([b, c])
        bridge[b].append([a, c])
        if c > high: high = c #가능한 무게의 최댓값
        
    start, end = map(int, input().split())
    
    while low <= high: #가능한 무게를 mid로
        mid = (low + high) // 2
        if bfs(mid, start, end, bridge): low = mid + 1 #가능하면 더 큰 mid 찾자
        else: high = mid - 1
        
    print(high)
    
def bfs(weight, start, end, bridge):
    que = deque()
    que.append(start)
    visited = set()
    visited.add(start)

    while que:
        x = que.popleft() #현재 위치
        if x == end: #마지막 지점에 도착
            return True
        for y, w in bridge[x]:
            if y not in visited and w >= weight: #원하는 mid보다 다리의 수용무게가 커야 건널 수 있음
                que.append(y)
                visited.add(y)
            
    return False

bs()