#백준 7568 - 덩치
#다른 사람보다 키, 몸무게 모두 커야 덩치 더 크다
#등수: 자신보다 더 큰 덩치의 사람들 수+1
#A:1, B,C,D:2(1+1), E:5(4+1)
#입력된 사람의 덩치 등수를 나열하라
from sys import stdin
input=stdin.readline
n=int(input()) #전체 사람 수
dung,result=[],[]
for _ in range(n):
    dung.append(list(map(int,input().split()))) #[키,몸무게]

for i in range(n):
    count=0 #자신보다 큰 덩치
    for j in range(n):
        if dung[i][0]<dung[j][0] and dung[i][1]<dung[j][1]:
            count+=1
    result.append(count+1) #등수는 자신보다 큰 덩치 수+1

print(*result)