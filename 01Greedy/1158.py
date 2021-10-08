#백준 1158 - 요세푸스 문제
#1-n번까지 n명의 사람이 원을 이루며, k 주어짐
#순서대로 'k번째' 사람을 제거
#한 사람이 제거되면 남은 사람들로 이뤄진 원을 따라 반복
#사람이 제거되는 순서를(n,k)요세푸스 순열
#(7,3)요세푸스 순열은 <3,6,2,7,5,1,4>
from sys import stdin
input=stdin.readline
list,result=[],[]
n,k=map(int,input().split())
for i in range(n):
    list.append(str(i+1))
idx=k-1 #인덱스는 0부터 시작

for i in range(n):#n명의 사람
    if len(list)-1>=idx: #idx접근 가능
        temp=list.pop(idx)
        result.append(temp)
        idx+=k-1
    else:#한 바퀴 돌 때
        idx=idx%len(list)
        temp=list.pop(idx)
        result.append(temp)
        idx+=k-1 #다음 인덱스부터 k-1개

print("<"+", ".join(result)+">")