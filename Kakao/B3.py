#캐시크기, 도시이름 배열
#입력 도시이름 배열 순서대로 처리 시 총 실행시간 구하라
#LRU(least Recently Used) 캐시 교체 알고리즘 - 가장 오래전 사용한 캐시 버림 -FIFO(Deque)
#cache hit-> 실행시간1
#cache miss-> 실행시간5
import collections

def solution(cacheSize, cities):
    elapsed = 0
    cache = collections.deque(maxlen=cacheSize) #큐의 최대크기 지정->넘치면 가장 이전 거 버림
    
    for c in cities:
        c = c.lower() #대소문자 구분x
        if c in cache: #cache hit -> 최근에 사용했으므로 뺐다가 다시 넣어줌
            cache.remove(c)
            cache.append(c)
            elapsed += 1
        else: #cache miss
            cache.append(c)
            elapsed += 5
    return elapsed

print(solution(3, ["jeju","pangyo","seoul","newyork","la","jeju","pangyo","seoul","newyork","la"])) #50
print(solution(3,["jeju","pangyo","seoul","jeju","pangyo","seoul","jeju","pangyo","seoul"])) #21
