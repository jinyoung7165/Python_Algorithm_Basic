import collections


def findMinHeightTrees(n, edges): #find root that makes min height
    if n <= 1: return [0]
    
    graph = collections.defaultdict(list)
    for i, j in edges:
        graph[i].append(j)
        graph[j].append(i)
        
    leaves = [] #리프노드
    for i in range(n+1):
        if len(graph[i]) == 1: #연결이 1개일 때 리프
            leaves.append(i)
        
    while n > 2: #전체 노드가 짝수일 땐 루트가 2개, 홀수일 땐 루트가 1개
        n -= len(leaves) #전체 노드에서 리프 노드들을 제거하고 루트만 남길 것
        new_leaves = []
        for leaf in leaves:
            neighbor = graph[leaf].pop()
            graph[neighbor].remove(leaf) #리프노드와 연결된 노드에서 리프노드를 떼 버림
            
            if len(graph[neighbor]) == 1: #해당 노드와 연결된 노드가 하나일 때, 새로운 리프가 됨
                new_leaves.append(neighbor)
                
        leaves = new_leaves
        
    return leaves #남은 노드가 루트이다