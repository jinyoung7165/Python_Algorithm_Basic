#Longest Univalue Path
class Solution:
    result = 0
    def longetUnivaluePath(self, root):
        def dfs(node):
            if node is None:
                return 0
            #존재하지 않는 노드까지 탐색
            left = dfs(node.left)
            right = dfs(node.right)
            
            #현재 노드가 자식과 동일하면 거리 증가
            if node.left and node.left.val == node.val:
                left += 1
            else:
                left = 0
                
            if node.right and node.right.val == node.val:
                right += 1
            else:
                right = 0
                
            self.result = max(self.result, left + right)
            
            return max(left, right)
        
        dfs(root)
        return self.result