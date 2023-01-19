# All Paths From Source to Target
# BFS <-> DFS 생각해보기
#방향성 비순환 그래프 0 -> n - 1 도달할 수 있는 모든 path return
#제일 빠르지만 메모리 좀 먹음
class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        result = []
        n = len(graph)
        disable = set()
        que = collections.deque([])
        que.append((0, [0]))
        while que:
            node, path = que.popleft()
            if node in disable: continue
            if node == n-1: #도착
                result.append(path)
                continue
            flag = False
            for next in graph[node]:
                if next not in path:#다음에 갈 곳 있으면
                    que.append((next, path+[next]))
                    flag = True
            if not flag: disable.add(node)

        return result
#빠르고 메모리 절약 good    
class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        target = len(graph) - 1 #n-1 나올 때까지 찾아라
        paths, targets = [[0]], []
        while paths:
            path = paths.pop(0) #현재 경로
            edges = graph[path[-1]] #현재 경로에서 마지막 노드가 갈 수 있는 후보 노드 집합
            if not edges: #갈 수 있는 경로 없음
                continue
            for edge in edges: #마지막 노드로부터 뻗어나갈 수 있을 때
                if edge==target: #목적지 도착
                    targets.append(path+[edge]) #결과에 적음
                else:
                    paths = [path+[edge]] + paths #덧셈 순서 이게 제일 빠르다. 가장 최신으로 탐색할 다음 노드 삽입
        return targets 