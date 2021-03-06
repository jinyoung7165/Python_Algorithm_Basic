'''깊이 우선 탐색, 스택자료구조(혹은 재귀함수) 이용
1. 탐색 시작 노드를 스택에 삽입후 방문
2. 스택의 최상단 노드에 방문하지 않은 인접한 노드가 하나라도 있으면
그 노드를 스택에 넣고 방문
3. 2번 불가능할 때까지 반복(방문할 노드가 없으면 현재노드를 스택에서 꺼냄)
'''
def dfs(graph,v,visited):
    visited[v]=True #현재 노드를 방문 처리
    print(v,end='')
    for i in graph[v]: #현재 노드와 연결된 다른 노드를 재귀적으로 방문
        if not visited[i]:
            dfs(graph,i,visited)

graph=[ #각 노드의 연결정보를 표현
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
visited=[False]*9 #각 노드의 방문 정보

dfs(graph,1,visited)