#Number of provinces
#isConnected[i][j] = 1 if the ith city and the jth city are directly connected, and isConnected[i][j] = 0
# province 개수
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        visited = set() #양방향이므로 다시 방문x 위함
        n = len(isConnected)
        count = 0
        for node in range(n):
            if node not in visited:
                count += 1 #하나의 province 방문
                next_node_list = [i for i, v in enumerate(isConnected[node]) if i != node and v == 1] #현재노드와 연결된 노드

                while next_node_list:
                    next_node = next_node_list.pop()
                    if next_node in visited: continue
                    visited.add(next_node) #방문
                    next_node_list.extend([i for i, v in enumerate(isConnected[next_node]) if i != node and v == 1]) #다음 연결된 곳을 추가해나감
        return count
    
'''
재귀 DFS - 아주 조금 느림
'''
class Solution(object):
    def findCircleNum(self, M):
        visited = [False for _ in range(len(M))]
        count = 0
        for i in range(len(M)):
            if not visited[i]: #방문하지 않았으면 타고 내려가라
                count += 1
                self.dfs(M, i, visited)
        return count
                
    def dfs(self, M, index, visited): #현재 노드랑 지나온 길 전달
        visited[index] = True
        for i in range(0, len(M)):
            if i == index: continue #자신이면 pass
            if not visited[i] and M[index][i] == 1: #방문하지 않았고 도달가능하면 타고 내려가라
                self.dfs(M, i, visited)