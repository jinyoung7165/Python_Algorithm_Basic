#백준 2606 - 바이러스
#한 컴터가 바이러스에 걸리면 연결된 모든 컴터에 전파
#1번 컴이 바이러스에 걸렸을 때 1번 컴을 통해 바이러스에 걸리는 컴터의 수 출력
#순서 상관없이 연결만 되면 감염이라 DFS
from sys import stdin
input = stdin.readline

n = int(input()) #컴퓨터 수
c = int(input()) #연결된 쌍 수

graph = [[0]*n for _ in range(n)]
for i in range(c):
    a,b = map(int, input().split())
    graph[a-1].append(b-1)
    graph[b-1].append(a-1) #a,b 서로 연결
    
visited = [False]*n

def dfs(graph,v,visited):
    visited[v]=True #현재 노드를 방문 처리
    for i in graph[v]: #현재 노드와 연결된 다른 노드를 재귀적으로 방문
        if not visited[i]:
            dfs(graph,i,visited)
            
dfs(graph,0,visited)
count=[i for i in visited if i == True]
print(len(count)-1)
