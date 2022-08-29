#Min차이 Between BST nodes
#root  =[4,2,6,1,3,null,null] ->1
#[10,4,15,1,8,null,null] -> 2(10-8)
#중간 노드 기준 계속 왼쪽 노드 타고 내려가면 값의 차이가 커짐
#중간 노드의 왼쪽 자식->계속 오른쪽 타고 내려가면 값의 차이가 적어짐
#중간 노드의 오른쪽 자식->계속 왼쪽 타고 내려가면 값의 차이가 작아짐
#중위순회 구현하면 됨
import sys

prev = -sys.maxsize
result = sys.maxsize

def minDiffBST(root):
    if root.left:
        minDiffBST(root.left) #맨왼쪽으로 내려감
        
    result = min(result, root.val - prev)
    prev = root.val #중간 노드의 값 저장
    
    if root.right: #왼쪽 자식의 맨 오른쪽 자식으로 내려감
        minDiffBST(root.right)
    
    return result

def minDiffBST(root):
    prev = -sys.maxsize
    result = sys.maxsize
    
    stack = []
    node = root
    
    while stack or node:
        while node:
            stack.append(node)
            node = node.left #맨왼쪽으로 내려감
            
        node = stack.pop()
        result = min(result, node.val - prev)
        prev = node.val #중간 노드의 값 저장
        
        node = node.right
        
    return result