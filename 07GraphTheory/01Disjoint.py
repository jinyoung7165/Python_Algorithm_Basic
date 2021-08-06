#특정 원소가 속한 집합 찾기
def find(parent,x): #x의 가장 루트를 parent테이블에서 찾아간다
    if parent[x]!=x:#루트노드를 찾을 때까지 재귀호출
        parent[x]= find(parent,parent[x]) #부모 테이블에 루트노드 갱신
    return parent[x]

#두 원소가 속한 집합을 합치기
def union(parent,a,b):
    a=find(parent,a)
    b=find(parent,b)
    if a<b:
        parent[b]=a
    else:
        parent[a]=b
#노드의 개수와 간선(union연산)의 개수 입력
v,e=map(int,input().split())
parent=[0]*(v+1) #부모 테이블 초기화

#부모 테이블 상에서 부모를 자기 자신으로 초기화
for i in range(1,v+1):
    parent[i]=i

#union연산 수행
for i in range(e):
    a,b=map(int,input().split())
    union(parent,a,b)

#각 원소가 속한 집합 출력
print("각 원소가 속한 집합: ",end='')
for i in range(1,v+1):
    print(find(parent,i),end='')
print()

#부모 테이블 내용 출력
print("부모 테이블: ",end='')
for i in range(1,v+1):
    print(parent[i],end='')
