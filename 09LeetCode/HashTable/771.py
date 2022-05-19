#해시맵: O(1)
#딕셔너리{} . put(k, v), get(k), remove(key)
#J는 보석이며, S는 가진 돌이다. S에는 보석이 몇 개나 있을까?
#J="aA", S="aAAbbbb"  => 3개
from calendar import c
from collections import Counter
import collections

def newJewelsInStones(J = "aA", S = "aAAbbbb"):
    count = 0
    freqs = Counter(S)
    for i in J:
        count += freqs[i]
    
    return count
    
def newJewelsInStones(J = "aA", S = "aAAbbbb"): #시간 효율 더 좋음
    freqs = collections.defaultdict(int) #처음 키,값 넣을 때 0부터 초기화
    count = 0
    
    for char in S:
        freqs[char] += 1 #그냥 {}dict 사용시 에러
        
    for char in J:
        count += freqs[char]
        
    return count
   
def newJewelsInStones(J = "aA", S = "aAAbbbb"): #시간, 공간 효율 더 좋음. 파이썬 장점
    return sum(s in J for s in S) #S의 원소들에 대해 J에 속했을 때마다 True의 개수 더해줌