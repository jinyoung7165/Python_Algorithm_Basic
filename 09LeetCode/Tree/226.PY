#Invert BinaryTree
import collections


def invertTree(self, node):
    if node:
        node.left, node.right = self.invertTree(node.right), self.invertTree(node.left)
        return node
    return None

def invertTreeBFS(self, root):
    queue = collections.deque([root])
    
    while queue:
        node = queue.popleft()
        
        if node:
            node.left, node.right = node.right, node.left
            
            queue.append(node.left)
            queue.append(node.right)
            
    return root