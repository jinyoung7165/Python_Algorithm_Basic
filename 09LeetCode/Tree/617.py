#Merge Two BinaryTrees
#중복되는 위치의 노드는 값을 합산
def mergeTrees(self, t1, t2):
    if t1 and t2: #같은 위치의 t1, t2 node
        node = TreeNode(t1.val, t2.val)
        node.left = self.mergeTrees(t1.left, t2.right)
        node.right = self.mergeTrees(t1.right, t2.right)
        return node #같은 위치의 노드 병합
    
    else: #하나의 위치에 동시에 존재하지 않음
        return t1 or t2 #두 트리 중 이 위치에는 하나의 노드만 존재 or 둘 다 없으면 None 반환