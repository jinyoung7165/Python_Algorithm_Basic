# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#Balanced Binary Tree 균형 이진 트리인지 판단하라
#모든 노드의 SubTree간 높이(리프로부터 측정) 차가 1 이하여야 함
#재귀호출로 left,right 훑으며 리프까지 내려감-> 리프노드부터 루트노드까지 훑으며 -1 나온 순간부터 isBalanced False
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def check(root):
            if not root: #리프노드의 left, right 노드의 경우 0
                return 0
            left = check(root.left) #재귀호출로 리프까지 내려감
            right = check(root.right)
            
            #서브트리간 abs(높이 차)가 1이상이면 isBalanced가 -1리턴, 아래 서브트리로부터 올라오는 과정에서 -1 나온 순간부터 루트까지 올라가는 과정에 쭉 -1리턴
            if left == -1 or right == -1 or abs(left - right) > 1:
                return -1
            
            return max(left, right) + 1 #서브트리간 높이 차가 1 이하면 높이 큰 애 + 1이 두 서브트리를 가진 노드의 높이가 됨, ex:리프노드의 경우 left, right가 0이기 때문에 높이가 1
        return check(root) != -1