#전체 수 n을 입력 받아 k개의 조합을 리턴하라
#n=4, k=2
#[[2,4], [3,4], [2,3], [1,2], [1,3], [1,4]]
from itertools import combinations

def comb(n=4, k=2):
    return list(map(list,combinations(range(1,5), 2)))

print(comb())