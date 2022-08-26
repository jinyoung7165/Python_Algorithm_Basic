#로또 (집합S주어졌을 때, 전체 k개 중 6개 뽑는 경우 kC6)
#사전 순으로 출력하라(combintaions쓰지 말고 풀어보자)
from sys import stdin
input = stdin.readline
result = []

def dfs(depth, idx):
    
    if depth == 6: 
        print(*result)
        return
    
    for i in range(idx, k):
        result.append(S[i])
        dfs(depth+1, i+1)
        result.pop()

while True:
    array = list(map(int, input().split()))
    k = array[0]
    S = array[1:]
    
    if k == 0:
        exit()
    
    result = []
    
    dfs(0, 0) #depth(몇개 선택했는지), idx
        
    print()