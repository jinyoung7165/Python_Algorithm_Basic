#1~n 정수 배열 p를 오름차순으로 정렬
#1.p[i]는 배열의 i번째 원소를 나타냄
#2.p[i],p[i+1],..p[n-1]중 가장 작은 숫자(p[j]) 찾기
#3.만약 i랑 j가 다르면 p[i], p[j] swap
#4.i에 1을 더함
#->i가 n보다 작으면 2번 단계로 돌아감
#->i==n이면 알고리즘 종료
#if p=[2,5,3,1,4]
#해당 위치의 값이 몇 번 바뀌었는지 배열에 담아 return
def solution(p):
    n = len(p)
    arr = [0 for _ in range(n)]
    if (p == sorted(p)): return arr
    for i in range(n-1):
        minv = min(p[i+1:])
        if minv < p[i]:
            small = p.index(minv)
            arr[i] += 1
            arr[small] += 1
            p[i], p[small] = p[small], p[i]
    return arr

print(solution([2,5,3,1,4]))
print(solution([2,3,4,5,6,1]))
#print(solution([1,2,3,4,5]))