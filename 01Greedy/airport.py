#10775 - 공항
# 1-g 개의 게이트
# p개의 비행기
# 가장 높은 게이트로 도킹. 시간초과 때문에 union-find방식으로
#도킹시킬 수 있는 최대의 비행기 수 출력
import sys
input=sys.stdin.readline
answer=0
g=int(sys.stdin.readline())
p=int(sys.stdin.readline())
parent=[i for i in range(g+1)] #자기자신을 부모로 갖는 리스트
planes=[] #각 비행기별 도킹가능한 최대 게이트 번호
for _ in range(p): #i번째 비행기는 1<=g<=planes[i] 게이트에 도킹 가능
    planes.append(int(input()))

def find(x):#루트를 찾아가서 루트번호를 리턴
    if parent[x]==x: 
        return x
    parent[x]=find(parent[x])
    return parent[x]

for plane in planes: #일단 최대한 큰 게이트(plane)에 도킹하는 게 좋다.
    docking=find(plane)
    if docking==0: #0은 최종 루트노드
        break
    parent[docking]=parent[docking-1] #도킹 가능.앞 게이트와 union(숫자 작은 앞 게이트가 부모가 됨)
    answer+=1
print(answer)