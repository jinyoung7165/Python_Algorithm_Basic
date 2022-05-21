#0을 완료하기 위해선 1을 끝내야 한다는 것을 [0,1] 쌍으로 표현하는 n개의 코스
#n과 이 쌍들을 입력받았을 때 모든 코스가 완료 가능한지 판별하라
#2,[[1,0]] => true (0->1순으로 진행하면 된다)
#2,[[1,0],[0,1]] => false (1->0->1 불가. cycle이 있으면 일을 끝내지 못한다)
#3,[[0,1],[0,2],[1,2]] => true (2->0, 2->1->0)
#cycle인지 판별하는 문제
#이미 방문했는지 기록하는 set 필요
import collections

def canFinish(n, prereq):
    graph = collections.defaultdict(list)
    for x,y in prereq:
        graph[x].append(y)
        
    traced = set() #방문한 노드 저장
    visited = set() #무사통과한 노드 저장
    
    def dfs(i):
        if i in traced: return False #현재 노드 이미 방문함. cycle
        if i in visited: return True #이미 무사 통과한, cycle이 없는 노드
        
        traced.add(i)
        for y in graph[i]:
            if not dfs(y): return False #cycle 자식을 가질 때
        
        traced.remove(i) #해당노드를 이용한 모든 탐색 종료 후 방문했던 내역 삭제->또다른 자식 노드가 방문할 수 있게함
        visited.add(i) #무사통과한 노드다.
        return True

    for i in list(graph): #defaultdict key를 통한 반복 시 반복할 때마다 변함 ->list로 해결
        if not dfs(x): return False
    
    return True