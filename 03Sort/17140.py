#3x3이차원 배열과 연산
#1초마다 연산
#행 수>=열 수 -> R연산: 모든 행의 수 정렬
#행 수<열 수 -> C연산: 모든 열의 수 정렬
#수 다음 등장 횟수를 넣어 (수 등장 수, 수) 순으로 정렬(x[1], x[0])
#행이나 열 크기가 100을 넘어가는 경우 처음 100개만 가져감
#100초가 지나도 A[r][c]=k가 안되면 -1출력
#A[r][c]에 들어있는 값아 k가 되기 위한 최소 시간
#Transpose: 행<->열 전치 list(map(list, zip(*board)))
from sys import stdin

input = stdin.readline

def R(arr):
    longest = 0 #가장 긴 리스트의 길이
    
    for i, row in enumerate(arr):
        
        counter = {j: row.count(j) for j in row if j!=0} #각 수의 등장 횟수
        #if counter.get(0): del counter[0] #0은 제외
        
        counter = list(counter.items())
        counter.sort(key = lambda x: (x[1], x[0]))
        
        if len(counter) > 50: counter = counter[:50] #횟수, 수 두 개가 graph에 표시->쌍이 50개 넘으면 안됨
        arr[i] = []
        for x, y in counter:
            arr[i].append(x)
            arr[i].append(y)
        
        longest = max(longest, len(arr[i]))
    
    for row in arr: #가장 긴 리스트에 맞춰 0추가
        if len(row) < longest:
            row.extend([0]*(longest - len(row)))
        
def main():
    r, c, k = map(int, input().split())
    graph = [list(map(int, input().split())) for _ in range(3)]

    result = 0 #시간
    if r <= len(graph) and c <= len(graph[0]) and graph[r-1][c-1] == k:
        return result #연산할 필요없이 이미 주어졌을 때
    
    while True:
        row_count, col_count = len(graph), len(graph[0])
        if row_count >= col_count: #R연산
            R(graph)
        else: #C연산
            graph = list(map(list, zip(*graph))) #Transpose
            R(graph)
            graph = list(map(list, zip(*graph))) #Transpose
            
        result += 1
        if result > 100: return -1 #100초 이상이면 탈락
        if r <= len(graph) and c <= len(graph[0]) and graph[r-1][c-1] == k:
            return result #연산할 필요없이 이미 주어졌을 때
        
print(main())