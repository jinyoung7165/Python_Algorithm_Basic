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
result=list(combinations(chicken,m)) #치킨집 중에서 선택

mindistance=sys.maxsize #어느 치킨집 조합과의 거리가 가장 짧았는지
#특정 조합을 선택해서 집과의 거리를 구해야하므로 치킨집이 가장 바깥 반복문에서 선택되어야한다
for k in result: #특정 치킨집 조합과의 거리
    distance=0 #모든 집의 치킨 거리의 합
    for h in house: #해당 집과의 치킨 거리
        temp=sys.maxsize  #해당 집과 가장 가까운 치킨집 거리 임시저장
        for t in k:#특정 조합의 특정 치킨집을 돌며 
            temp=min(temp,abs(h[0]-t[0])+abs(h[1]-t[1])) #이전의 치킨집과 비교해서 치킨거리
        distance+=temp #전체 집의 치킨거리 기록
    mindistance=min(mindistance,distance) #해당 치킨집조합과의 도시 치킨집거리
print(mindistance)
