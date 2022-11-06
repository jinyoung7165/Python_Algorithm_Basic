#Gas Station
#원형으로 경로 연결된 주유소
#각 주유소는 gas[i]만큼 기름을 보유, 다음 주유소로 이동하는데 cost[i] 필요
#기름이 부족하면 이동할 수 없다고 할 때 모든 주유소를 방문할 수 있는 출발점 인덱스 구하라
#출발점 유일. 존재하지 않을 때 -1 출력
#gas[1,2,3,4,5] cost[3,4,5,1,2] 인덱스3->4->0..이동 시 기름0까지 소모, 모두 순회 가능
#전체 기름 양보다 전체 비용이 크면 순회 불가능-출발점 유일 조건 실패. False
#어차피 가능한 출발지점은 하나이기 때문에 안되는 지점을 모두 빼면 남는 것이 정답이 됨 O(n)
def canComplete(gas, cost):
    if sum(gas) < sum(cost): return -1
    
    start, fuel = 0, 0
    for i in range(len(gas)):
        #출발점이 안되는 지점 판별
        if gas[i] + fuel < cost[i]:
            start = i + 1
            fuel = 0
        else:
            fuel += gas[i] - cost[i]
    return start