#BinaryTree Preorder, Inorder Traversal
#트리의 전위, 중위 순회 결과를 입력값으로 받아 이진 트리를 구축하라
#전위:[3,9,20,15,7]
#중위:[9,3,15,20,7]
#전위순회의 첫번째 노드: 중위순회를 반으로 나누는 루트 노드

def buildTree(preorder, inorder):
    if inorder:
        index = inorder.index(preorder.pop(0)) #루트노드의 인덱스
        
        node = TreeNode(inorder[index]) #루트노드
        node.left = buildTree(preorder, inorder[0:index]) #왼쪽 서브트리
        node.right = buildTree(preorder, inorder[index+1:]) #오른쪽 서브트리
        
        return node