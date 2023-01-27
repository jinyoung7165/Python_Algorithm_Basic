#BinaryTree Preorder, Inorder Traversal
#트리의 전위, 중위 순회 결과를 입력값으로 받아 이진 트리를 구축하라
#전위:[3,9,20,15,7]
#중위:[9,3,15,20,7]
#전위순회의 첫번째 노드: 중위순회를 반으로 나누는 루트 노드
# 105. Construct Binary Tree from Preorder and Inorder Traversal
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        #preo의 맨 처음이 루트 -> inorder를 반으로 쪼갬
        #분할 정복
        if inorder: #쪼개진 inorder트리가 존재하면
            root = preorder.pop(0) #첫번째 원소가 루트(pop(0)-> preorder[1:] 말고 preorder 전잘)
            idx = inorder.index(root) #inorder를 나누는 인덱스
            node = TreeNode(inorder[idx]) #해당 값을 가진 노드

            node.left = self.buildTree(preorder, inorder[:idx])
            node.right = self.buildTree(preorder, inorder[idx+1:])

            return node