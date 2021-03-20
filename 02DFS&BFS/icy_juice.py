'''
얼음 틀 세로 N , 가로 M
구멍이 뚫려있는 부분은 0, 그렇지 않은 부분은 1
한 번에 만들 수 있는 아이스크림 개수를 구하라
001
010
101
그래프로 연결 가능->dfs또는 bfs로 풀이 가능
<DFS>
1. 노드의 상하좌우를 살펴본 뒤 인접 노드 중 값이 0이면서 방문하지 않은 노드를 방문
2. 연결된 모든 지점을 방문하면서, 방문하지 않은 지점의 수를 카운트
'''
def dfs(x,y):
    if x<=-1 or x>=n or y<=-1 or y>=m:  #주어진 범위를 벗어나면 즉시종료
        return False
    if graph[x][y]==0: #현재 노드를 아직 방문하지 않았다면
        graph[x][y]=1 #방문 처리해서 다시는 방문할 수 없게 함
        dfs(x-1,y) #상하좌우 호출
        dfs(x,y-1)
        dfs(x+1,y)
        dfs(x,y+1)
        return True
    return False

n,m=map(int,input().split()) 
graph=[] #2차원 리스트 입력 받기
for i in range(n):
    graph.append(list(map(int,input())))
result=0
for i in range(n): #모든 노드에 음료수 채우기
    for j in range(m):
        if dfs(i,j)==True: #현재 위치에서 dfs수행.0->1로 채워지면 True가 됨
            result+=1
print(result)