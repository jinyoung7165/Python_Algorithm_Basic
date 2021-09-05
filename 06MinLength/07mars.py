#ICPC - 화성 탐사
#탐사 기계가 존재하는 공간은 N x N. 각각의 칸을 지나기 위한 비용이 존재
#가장 왼쪽 칸에서 가장 오른쪽 아래 칸으로 이동하는 최소 비용을 출력
import heapq
from sys import stdin
input = stdin.readline
INF = int(1e9)
graph=[] #각 칸의 비용
d=[(-1,0),(1,0),(0,-1),(0,1)] #사방
n=int(input())
for i in range(n):#각 칸의 비용 입력
    graph.append(list(map(int, input().split())))

distance = [[INF] * n for _ in range(n)] # 최단 거리 테이블
q=[] #(최단거리,x,y) 저장
heapq.heappush(q,(graph[0][0],0,0)) #초기 칸을 지나기 위한 비용도 존재(graph[0][0])
distance[0][0]=graph[0][0]
while q:
    cost,x,y=heapq.heappop(q) #현재 노드의 비용, 좌표
    if distance[x][y]<cost:  #이미 방문한 노드면 무시
        continue
    #현재노드와 연결된 4방향의 노드 확인->현재 노드 거쳐 더 짧아지면 distance갱신 후 q에 넣음
    for i in range(4):
        nx=x+d[i][0]
        ny=y+d[i][1]
        # 맵의 범위를 벗어나는 경우 무시
        if nx < 0 or nx >= n or ny < 0 or ny >= n:
            continue
        dist=cost+graph[nx][ny] #현재 칸 경유해서 다음 칸 갈 경유 비용
        if (distance[nx][ny]>dist): #현재 칸 경유하면 더 작아질 때, 테이블 갱신 후 heappush
            distance[nx][ny]=dist
            heapq.heappush(q,(dist,nx,ny))

print(distance[n - 1][n - 1]) #가장 끝 칸의 비용 출력