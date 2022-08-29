#BST의 각 노드를 자신보다 더 큰 값을 가진 노드들+자신의 합으로 만들어라
#[4,1,6,0,2,5,7,null,null,null,3,null,null,null,8]
#[30,36,21,36,35,26,15,null,null,null,33,null,null,null,8]
#자신을 포함한 우측 자식 노드의 합을 구하면 됨
#root->맨 오른쪽 리프->부모->왼쪽:중위 순회

val = 0
def bstToGst(root):
    if root:
        bstToGst(root.right)
        val += root.val #전체합 누적
        root.val = val #자신 갱신
        bstToGst(root.left)
    return root