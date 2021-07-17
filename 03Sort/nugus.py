#백준 - 1764
#듣x,보x=>듣보x 수, 명단구해라
# N, M
from sys import stdin
input=stdin.readline
n,m=map(int,input().split())
N,M=[],[]
for _ in range(n):
    N.append(input().rstrip())
for _ in range(m):
    M.append(input().rstrip())
N.sort()
M.sort()
result=[]
idx=0
for i in N:#삽입정렬 느낌
        while(idx<m and M[idx]<=i):
            if(M[idx]==i):
                result.append(i)
                break
            idx+=1
print(len(result))
for i in result:
    print(i)