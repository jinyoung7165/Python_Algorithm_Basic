'''너비 우선 탐색, 큐 자료구조
1. 탐색 시작 노드를 큐에 삽입하고 방문
2. 큐에서 노드를 꺼낸 뒤에 해당 노드의 인접 노드 중 방문하지 않은 노드를 모두 큐에 삽입하고 방문
3. 2번 불가할 때까지 반복
'''
from collections import deque

def bfs(graph,start,visited):
    que=deque([start])
    visited[start]=True #현재 노드를 방문 처리
    while que: #큐가 빌 때까지 반복
        v=que.popleft() #맨 앞에서 원소 뽑아 출력
        print(v,end='')
        for i in graph[v]:
            if not visited[i]: #인접한 노드 확인
                que.append(i) #방문하지 않은 원소를 큐에 삽입
                visited[i]=True

graph=[
    [], #0번 노드는 미사용(1부터 출발)
    [2,3,8], #1번노드는 2,3,8과 연결
    [1,7], #2번 노드는 1,7과 연결
    [1,4,5], #3번 노드정보
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]
visited=[False]*9

bfs(graph,1,visited)
