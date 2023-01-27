#Max Depth of Binary Tree
#DFS
import collections

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root == None: return 0
        queue = collections.deque([root]) #root노드 삽입
        count = 0
        while queue:
            count += 1 #한 층 존재함
            for _ in range(len(queue)): #삽입된 노드만큼("한 층"의 모든 노드들: 정이진트리면 최대 4개). 상하좌우처럼 왼오, 왼오 탐색한다고 생각
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return count #BFS반복 횟수 = 깊이