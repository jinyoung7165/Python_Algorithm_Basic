#리프노드란 자식의 개수가 0
#트리가 주어지면 노드 하나를 지운다
#노드를 지우면 그 노드의 모든 자손까지 제거됨
#남은 트리에서 리프 노드 개수를 구하라
from collections import defaultdict
from sys import stdin
input = stdin.readline

n = int(input()) #노드의 개수
parents = list(map(int, input().split())) #부모 번호
delete = int(input()) #지울 노드 번호

count = 0

def dfs(node):
    global count
    if not graph[node] and node != -1: count += 1
    while graph[node]:
        next = graph[node].pop()
        dfs(next)
    


graph = defaultdict(list)
#루트노드가 0번이라는 보장 없음
for i in range(n):
    if i == delete: continue
    graph[parents[i]].append(i)

parent = parents[delete] #삭제할 노드의 부모
dfs(-1)
print(count)