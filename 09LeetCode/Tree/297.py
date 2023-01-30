# Serialize and Deserialize Binary Tree
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#트리->배열->str. 자식이 없으면 #으로 채움. 0번째 원소는 #으로
class Codec:

    def serialize(self, root): #tree->str
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        result = []
        que = collections.deque([root])
        while que:
            node = que.popleft()
            if node:
                result.append(str(node.val))
                que.append(node.left)
                que.append(node.right)
            else:
                result.append("#") #빈 배열(root가 None)이어도 '#'

        return ' '.join(result)

    def deserialize(self, data): #str->tree
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        node_list = data.split(' ')
        if node_list[0] == '#': return None
        root = TreeNode(int(node_list[0]))
        que = collections.deque([root])
        idx = 1 #루트 다음 원소의 인덱스 붙일 것
        while que:
            node = que.popleft() #현재 서브트리의 루트
            if node_list[idx] != '#': #왼쪽 자식 존재
                node.left = TreeNode(int(node_list[idx]))
                que.append(node.left)
            idx += 1 #다음 원소 볼 것
            if node_list[idx] != '#': #오른쪽 자식 존재
                node.right = TreeNode(int(node_list[idx]))
                que.append(node.right)
            idx += 1 #다음 원소 볼 것(serilaize시 자식 None이라도 양 옆 더함 + 중심노드None이면 실행x =>idx 초과 안 함)
        return root