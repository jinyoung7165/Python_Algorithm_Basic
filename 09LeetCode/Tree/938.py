#bst가 주어졌을 때 L이상 R이하의 값을 지닌 노드의 합
#root = [10,5,13,3,7,null,18] , L=7, R=15   -> 32
def rangesumBST(root,L,R): #재귀 브루트포스(L-R 사이면 반환)
    if not root:
        return 0
    
    return (root.val if L<=root.val<=R else 0) + rangesumBST(root.left, L, R) + rangesumBST(root.right
                                                                                            , L, R)
def rangesumBST(root,L,R): #가지치기
    def dfs(node):
        if not node:
            return 0
        if node.val <L: #왼쪽편은 볼 것도 없다
            return dfs(node.right)
        elif node.val >R: #오른편은 볼 것도 없다
            return dfs(node.left)
        return node.val + dfs(node.left) + dfs(node.right)
    return dfs(root)

def rangesumBST(root,L,R): #재귀->stack반복
    stack, sum = [root], 0
    while stack: #유효한 노드만 stack에 넣음
        node = stack.pop()
        if node:
            if node.val > L:
                stack.append(node.left)
            if node.val < R:
                stack.append(node.right)    
            if L<=node.val<=R:
                sum += node.val
    return sum

def rangesumBST(root, L, R): #BFS 큐로. pop(0)은 O(n). pop()은 O(1)
    stack, sum = [root], 0
    while stack:
        node = stack.pop(0)
        if node:
            if node.val > L:
                stack.append(node.left)
            if node.val < R:
                stack.append(node.right)    
            if L<=node.val<=R:
                sum += node.val
    return sum    