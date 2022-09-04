#백준 1991 트리 순회
#이진 트리를 입력 받아 전위,중위,후위 결과를 출력
#항상 A가 루트
from collections import defaultdict
from sys import stdin
input = stdin.readline

n = int(input()) #노드 개수
graph = defaultdict(list)

for _ in range(n):
    a, b, c = input().split()
    graph[a].append(b)
    graph[a].append(c)

def preorder(node, result):
    if node and node != '.':
        result.append(node)
        preorder(graph[node][0], result)
        preorder(graph[node][1], result)
    return result

def inorder(node, result):
    if node and node != '.':
        inorder(graph[node][0], result)
        result.append(node)
        inorder(graph[node][1], result)
    return result

def postorder(node, result):
    if node and node != '.':
        postorder(graph[node][0], result)
        postorder(graph[node][1], result)
        result.append(node)
    return result

print(''.join(preorder('A', [])))
print(''.join(inorder('A', [])))
print(''.join(postorder('A', [])))