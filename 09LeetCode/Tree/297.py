#Serilaze and Deserialize Binary Tree
#트리->배열->str. 자식이 없으면 #으로 채움. 0번째 원소는 #으로
#BFS
import collections

class Codec:
    def serialize(self, root):
        queue = collections.deque([root])
        result = ['#']
        while queue:
            node = queue.popleft()
            if node:
                queue.append(node.left)
                queue.append(node.right)        
                result.append(str(node.val)) #현재의 노드 삽입
            else:
                result.append('#')
                
        return ' '.join(result)
    
    def deserialize(self, data): #str->트리
        nodes = data.split() #str->배열
        
        root = TreeNode(int(nodes[1])) #루트
        queue = collections.deque([root])
        index = 2 #다음 배열 원소 : level1의 맨왼쪽 자식
        while queue:
            node = queue.popleft()
            if nodes[index] != '#': #왼쪽 자식 노드가 존재할 때
                node.left = TreeNode(nodes[index]) #tree에 이어주고
                queue.append(node.left)
                
            index += 1 #배열의 다음 원소(오른쪽에 노드 있는지 볼 것)
            
            if nodes[index] != '#': #오른쪽 자식 노드가 존재할 때
                node.right = TreeNode(nodes[index]) #tree에 이어주고
                queue.append(node.right) 
                
            index += 1
            
        return root