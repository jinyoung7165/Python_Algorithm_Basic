#N과 M
#n,m주어졌을 때 1-N까지 수 중에서 중복없이 M개를 고른 수열을 모두 구하라
#사전순 증가하는 순으로 출력
from itertools import permutations

n, m = map(int, input().split())

'''
result = list(map(list,permutations(range(1, n+1),m)))

for i in result:
    for j in i:
        print(j, end=' ')
    print()
위의 풀이보다 dfs가 더 빠름
'''   
s = []

def dfs():
    if len(s) == m:
        print(' '.join(map(str, s)))
        return
    
    for i in range(1, n+1):
        if i not in s: 
            s.append(i)
            dfs()
            s.pop()
dfs()