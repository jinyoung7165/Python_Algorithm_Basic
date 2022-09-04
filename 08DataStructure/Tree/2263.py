#트리의 순회
#n개의 정점 이진트리(1-n)
#inorder, postorder 주어졌을 때 preorder를 구하라
#후위순회의 마지막 노드: 중위순회를 반으로 나누는 루트 노드
#슬라이싱 -> 늘 새 배열을 만듦 -> 메모리 초과
#inorder에서 root idx찾고 postorder에서 똑같이 좌우 개수!를 나누는 기준이 됨
#preorder->root출력 후 왼쪽부터 내려가야 함
from sys import stdin, setrecursionlimit
input = stdin.readline
setrecursionlimit(1000000)

n = int(input())
inorder = list(map(int, input().split()))
postorder = list(map(int, input().split()))

index_inorder = [[] for _ in range(n+1)] #원소->index담음
for i in range(n):
    index_inorder[inorder[i]] = i

def preorder(instart, inend, poststart, postend):
    if instart > inend or poststart > postend: return
    root = postorder[postend]
    root_index = index_inorder[root]
    print(root, end = ' ')
    
    left = root_index - instart #왼쪽 트리 노드의 개수
    right = inend - root_index #오른쪽 트리 노드의 개수
    
    preorder(instart, root_index-1, poststart, poststart+left-1) #왼쪽으로 내려감 
    preorder(root_index+1, inend, postend-right, postend-1) #오른쪽으로 내려감(postend-1:맨마지막이 루트라 포함x)
#postorder의 index범위까지 root_index-1로 지정하면 무한루프 걸림.틀림    
#inorder만 index를 반으로 나눠주는 것이고 postorder의 경우 개수를 나눠줌    
preorder(0, n-1, 0, n-1) #노드말고 인덱스의 범위를 전달


''' -> 슬라이싱 = 새 배열 생성 -> 메모리 초과
def order(inorder, postorder):
    if postorder == inorder:  #자식 1개인 루트의 모임
        return reversed(postorder)
    
    root = [postorder[-1]] #post의 맨마지막이 루트임
    root_index = inorder.index(root)
    
    root.append(order(inorder[:root_index], postorder[:root_index])) #왼쪽으로 내려감
    root.append(order(inorder[root_index+1:], postorder[root_index:-1])) #오른쪽으로 내려감
    return root

print(*order(inorder, postorder))
'''