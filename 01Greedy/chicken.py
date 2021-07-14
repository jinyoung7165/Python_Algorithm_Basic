#빈(0),집(1),치킨(2)
#집과 가장 가까운 치킨집 사이의 거리. |r1-r2| + |c1-c2|
#치킨집 중에서 최대 M개를 고르고. 어떻게 고르면, 도시의 치킨 거리가 가장 작게 될지
#n:도시크기(n*n) m:놔둘치킨집의 개수
from itertools import combinations
import sys
n,m=map(int,input().split())
maps,house,chicken=[],[],[]
for _ in range(n):
    maps.append(list(map(int,input().split())))
for i in range(n):
    for j in range(n):
        if(maps[i][j]==1):
            house.append([i,j])
        if (maps[i][j]==2):
            chicken.append([i,j])

dlist=[sys.maxsize]*len(house)
mindistance=sys.maxsize
for com in combinations(chicken,m):#치킨집 조합별
    for c in com: #각 치킨집
        i=0
        for h in house:
            dlist[i]=min(dlist[i],abs(h[0]-c[0])+abs(h[1]-c[1]))
            i+=1
    mindistance=min(mindistance,sum(dlist))
    dlist=[sys.maxsize]*len(house)
print(mindistance)