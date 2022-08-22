#Balanced Binary Tree 균형 이진 트리인지 판단하라
#모든 노드의 SubTree간 높이 차가 1 이하여야 함

def isBalanced(self, root):
    def check(root):
        if not root: return -1
        left = isBalanced(root.left)
        right = isBalanced(root.right)
        
        if left == -1 or right == -1 or abs(left - right) > 1:
            return -1 #균형 안맞음
        return max(left, right) + 1 #depth증가    
           
        
    return check(root) != -1