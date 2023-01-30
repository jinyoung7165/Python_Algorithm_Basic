#Invert BinaryTree
import collections


def invertTree(self, node):
    if node:
        node.left, node.right = self.invertTree(node.right), self.invertTree(node.left)
        return node
    return None

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTreeBFS(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        que = collections.deque([root])
        
        while que:
            node = que.popleft()
            if node:
                node.right, node.left = node.left, node.right
                que.append(node.right) #다음 볼 서브트리 루트를 현재 노드의 right라고 생각
                que.append(node.left) #다음 볼 서브트리 루트를 현재 노드의 left라고 생각
        
        return root