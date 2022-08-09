#Max Depth of Binary Tree
#DFS
import collections


def maxDepth(self, root):
    if root == None:
        return 0

    queue = collections.deque([root])
    depth = 0
    
    while queue:
        depth += 1
        #추출 노드의 자식 노드 삽입
        for _ in range(len(queue)):
            root = queue.popleft()
            if root.left:
                queue.append(root.left)
            if root.right:
                queue.append(root.right)
    return depth #BFS반복 횟수 = 길이