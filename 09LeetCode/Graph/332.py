#일정 재구성
#[출발지, 목적지]로 구성된 항공권 목록을 통해 JFK에서 출발하는 여행 일정을 구하라
#여러 일정이 있는 경우 사전 어휘 순으로 방문
#[["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]
#=> ["JFK","MUC","LHR","SFO","SJC"]
#[["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
#=> ["JFK","ATL","JFK","SFO","ATL","SFO"]  사전 순에 맞게 하나의 결과
import collections

tickets =[["JFK","KUL"],["JFK","NRT"],["NRT","JFK"]]
def findItinerary(tickets):
    graph = collections.defaultdict(list) #출발지에 따른 목적지 여러 개일 수 있다
    for a,b in sorted(tickets): #사전순에 맞게 정렬해 출발지에 대한 목적지 딕셔너리
        graph[a].append(b)
    
    route = []
    
    def dfs(a):
        while graph[a]: #a로부터 갈 수 있는 목적지가 있으면
            dfs(graph[a].pop(0)) #첫번째 목적지를 넘기며 pop했기 때문에 재방문하지 않는다
        route.append(a) #a로 이동
    dfs("JFK")
    return route[::-1]


#pop(0):O(n)->리스트 크면 시간 복잡도 크다 =>pop():O(1)으로 바꿔보자!
def findItinerary(tickets):
    graph = collections.defaultdict(list) #출발지에 따른 목적지 여러 개일 수 있다
    for a,b in sorted(tickets, reverse=True): #사전 역순 정렬해 출발지에 대한 목적지 딕셔너리
        graph[a].append(b)
    
    route = []
    
    def dfs(a):
        while graph[a]: #a로부터 갈 수 있는 목적지가 있으면
            dfs(graph[a].pop()) #첫번째 목적지를 넘기며 pop했기 때문에 재방문하지 않는다
        route.append(a) #a로 이동
    dfs("JFK")
    return route[::-1]


print(findItinerary(tickets))