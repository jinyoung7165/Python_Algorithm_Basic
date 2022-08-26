#영역 구하기
#주어진 직사각형 좌표를 1로 만들고
#i,j로 그냥 끊길때까지 너비 증가, 끊기면 새로운 덩어리
from sys import stdin, setrecursionlimit
setrecursionlimit(100001)
input = stdin.readline
m, n, k = map(int, input().split())
graph = [[0]* n for _ in range(m)]
for _ in range(k):
    x1, y1, x2, y2 = map(int, input().split())
    for j in range(y1, y2):
        for k in range(x1, x2):
            graph[j][k] = 1
            
width = [0]  #너비 배열
count = 0 #덩어리 개수
def dfs(x, y, i): #i:몇번째 덩어리인지
    if 0 <= x < m and 0 <= y < n:
        if graph[x][y] == 1: return False
        width[i] += 1
        graph[x][y]= 1
        dfs(x-1, y, i)
        dfs(x, y-1, i)
        dfs(x+1, y, i)
        dfs(x, y+1, i)
        return True
    return False
    
for i in range(m):
    for j in range(n):
        if dfs(i, j, count) == True:
            count += 1
            width.append(0)
print(count)
width.sort()
if width[0] == 0: del width[0]
print(*width)
        