#백준 11047 -동전0
#동전 N종류, 총 K원 만들려고 할 때 필요한 동전의 최솟값
from sys import stdin
input=stdin.readline
n,k=map(int,input().split())
value=[] #동전 종류.오름차순으로 주어짐
for i in range(n):
    value.append(int(input()))
#남은 동전들 선택 o,x ->가능한 최대개수-> 그 다음 단위

min=0 #모든 동전 단위 고려했을 때 최소 동전 개수
left=k #남은 총 금액
for i in range(n-1,-1,-1):
    if(left==0): break
    if(left>=value[i]): 
        min+=left//value[i]
        left=left%value[i]
    
print(min)