#Course Schedule 2
#모든 course 끝내기 위한 순서 나열하라. 불가능하면 [] 리턴
#2, [[1,0]] -> [0,1] 0 이후에 1 나와야 함
#4, [[1,0],[2,0],[3,1],[3,2]] -> [0,2,1,3] 0 이후에 1,2 나와야 함, 1,2 이후에 3 나와야 함
from ast import List
import collections

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        required = [0] * numCourses #x를 듣기 위한 선수강 과목 수
        graph = collections.defaultdict(list)

        for x, y in prerequisites:
            graph[y].append(x) #y이후에 x들어야 함
            required[x] += 1 #x를 듣기 위한 선수강 수+1
        
        que = collections.deque([])
        for i in range(numCourses):
            if required[i] == 0: #필요한 선수강 과목이 없을 때 냅다 듣기
                que.append(i)
        
        path = []
        while que:
            cur = que.popleft()
            path.append(cur)
            for next in graph[cur]:
                required[next] -= 1
                if required[next] == 0: #선수강 다 들음
                    que.append(next)
        if len(path) == numCourses:
            return path
        else:  return []

#시간 효율적, 메모리 사용량 같음.topologySort 위상정렬 방식
#방향성 비순환 그래프.indegree:노드로 들어오는 간선 수
#in이 0인 모든 노드를 큐에 넣음
#큐가 빌 때까지 반복
#  1) 큐에서 원소를 꺼내 노드에서 나가는 간선을 그래프에서 제거
#  2) 새롭게 in이 0이 된 노드를 큐에 넣음
#각 노드가 큐에 들어온 순서가 결과임
class Solution:
    def findOrder(self, numCourses, prerequisites):
        indegree = [0] * numCourses
        result = []

        graph = collections.defaultdict(list)

        for x, y in prerequisites:
            graph[y].append(x) #y이후에 x들어야 함(y->x 이동 가능)
            indegree[x] += 1 #x에 대한 진입차수 1증가

        queue = collections.deque(v for v in range(numCourses) if indegree[v] == 0) #독립적인 노드일 때 삽입
        while queue:
            vertex = queue.popleft()
            result.append(vertex)
            for neighbor in graph[vertex]:
                indegree[neighbor] -= 1 # neighbor를 듣기 위한 준비 vertex 하나 제거
                if indegree[neighbor] == 0: #더이상 진입차수 없을 때 방문 가능
                    queue.append(neighbor)

        return result if len(result) == numCourses else []