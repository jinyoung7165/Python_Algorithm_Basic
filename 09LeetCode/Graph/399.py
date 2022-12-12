class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        #query의 원소 중 하나라도 eq에 없으면 -1.0
        graph = defaultdict(list)
        
        for eq, v in zip(equations, values): #index같은 애들끼리 묶음
            x, y = eq 
            graph[x].append([y, v]) #x->y로 가는 가중치 v
            graph[y].append([x, 1/v]) #x<-y로 가는 가중치 1/v

        result = []
        
        for start, end in queries: #start->end 도달이 목적. (flag=False)도달x 시 -1.0 append
            if start not in graph or end not in graph:
                result.append(-1.0) ##query의 원소 중 하나라도 eq에 없으면 -1.0
                continue
            if start == end:
                result.append(1.0) #등록된 수 중 같으면 1.0(values에 0.0없음 전제)
                continue
            queue = deque([])
            queue.append([start, 1.0]) #start부터 가보자. 간선 값 누적 곱셈할 거라 1.0
            visited = {start}
            flag = False #end 도착하면 True

            while queue: #start부터 간선타고 이동 -> 결국 end에 도착. start로부터 여러 지점 중복 거치는 것 visited로 건너뛰기
                node, cur_val = queue.popleft() #현재 거친 노드, 누적 값
                if node == end: #start->end도착 가능
                    result.append(cur_val)
                    flag = True
                    break

                for next_node, val in graph[node]: 
                    #현재 노드에서 갈 수 있는 곳이 많으면 queue에 append 
                    # -> end도착 후에 queue가 차 있을 수 있음. queries마다 queue초기화해야 함
                    if next_node in visited: #이미 방문한 곳이면
                        continue
                    visited.add(next_node)
                    queue.append([next_node, cur_val*val]) #다음노드로 가기 위한 간선 값 누적(a/c=a/b*b/c)
            if not flag: #start->end에 도달 못 함
                result.append(-1.0)

        return result