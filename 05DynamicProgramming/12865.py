#n개의 물건. 무게 w, 가치 v를 가짐
#총 k무게까지 가능
#가장 높은 가치의 합 구하라
#d[i][j]는 i번째 물건 까지 살펴보았을 때, 허용 무게가 j인 배낭의 최대 가치
#if j < weight : d[i][j] = d[i-1][j] (현재 배낭의 허용 무게보다 클 때, 물건을 넣지 않는다)
#else 넣을 수 있을 때: d[i][j] = max(d[i-1][j](걍 안넣고 그대로), d[i-1][j-weight]+value(넣은 item의 무게만큼 가방의 수용무게 뺌+ item의 가치))
n, k = map(int, input().split())

thing = [[0,0]]
d = [[0]*(k+1) for _ in range(n+1)]

for i in range(n):
    thing.append(list(map(int, input().split())))

for i in range(1, n+1):
    for j in range(1, k+1):
        w = thing[i][0]
        v = thing[i][1]
        
        if w > j: #못 넣음
            d[i][j] = d[i-1][j] #총 가치가 이전 아이템까지 봤을 때랑 같음
        else: #넣을 수 있음
            d[i][j] = max(d[i-1][j], d[i-1][j-w] + v)
            #안 넣거나, 넣었을 때의 가치 중 큰 것
print(d[n][k]) #가방이 k만큼 수용가능할 때, 최대 가치