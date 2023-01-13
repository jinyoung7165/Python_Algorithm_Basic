#Redundant Connection-> 무방향 그래프. cycle 만드는 마지막 간선 찾아라
#multiple answers ->return the answer that occurs last in the input.
#union find 로 바꾸기 O(n)
class Solution(object):
    def findRedundantConnection(self, edges):
        graph = collections.defaultdict(list)
        result = []
        def dfs(u, v): #u->v 이동 가능하면 true
            if u not in visited:
                visited.add(u)
                if u == v: return True #연결된 unit일 때
                for next in graph[u]:
                    if dfs(next, v): return True
            return False
        
        # 두 노드 전에 이미 나왔고, 서로 연결된 unit일 때 result에 추가
        for x, y in edges:
            visited = set()
            if x in graph and y in graph and dfs(x, y):
                result.append([x,y])
            graph[x].append(y)
            graph[y].append(x)
        return result.pop() if result else []
#union find O(n)
#무방향 그래프 내 사이클 판별에 서로소 집합 이용
#각 간선 하나씩 확인, 두 노드의 루트 확인
#루트노드가 서로 다르면 합집합 연산
#루트노드가 같다면 사이클이 발생한 것
# 특정 원소가 속한 집합을 찾기
class Solution(object):
    def findRedundantConnection(self, edges):
        graph = collections.defaultdict(list)
        result = []
        v = len(edges)
                    
        parent = [0] * (v + 1) # 부모 테이블 초기화하기

        # 부모 테이블상에서, 부모를 자기 자신으로 초기화
        for i in range(1, v + 1):
            parent[i] = i

        # 특정 원소가 속한 집합의 루트 노드를 찾아나감
        def find_parent(x):
            # 루트 노드가 아니라면, 루트 노드를 찾을 때까지 재귀적으로 호출
            if parent[x] != x:
                parent[x] = find_parent(parent[x]) #부모의 부모를 찾음
            return parent[x] # 루트 노드 리턴

        # 두 원소가 속한 집합을 합치기(두 노드를 간선으로 이어줌)
        def union_parent(a, b):
            a = find_parent(a) #부모 노드의 루트 리턴
            b = find_parent(b)
            if a < b: # 번호가 작은 노드를 부모로 가리키게 함
                parent[b] = a #b->a
            else:
                parent[a] = b #a->b

        for a, b in edges:
            # 사이클이 발생한 경우 종료
            if find_parent(a) == find_parent(b): #부모가 같으면 이미 같은 집합에 있는 노드임
                return [a, b]
            # 사이클이 발생하지 않았다면 합집합(Union) 연산 수행
            else:
                union_parent(a, b)