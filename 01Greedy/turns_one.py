'''
어떠한 수 N이 1이 될 때까지 다음 두 과정을 수행
두 번째 연산은 N이 K의 배수일 때만 가능
1. N에서 1을 뺀다
2. N을 K로 나눈다
N과 K가 주어질 때 N이 1이 될 때까지 1번 또는 2번 과정을 수행해야하는 최소 횟수를 구해라
'''
#2이상의 K로 나누는 것이 1을 빼는 작업보다 더 빠르게 N을 감소시킬 수 있다. 
n,k=map(int,input().split())
result=0
while True:
    target=(n//k)*k  #target은 항상 k의 배수
    result+=(n-target)  #
    n=target
    if n<k:  #n이 k보다 작을 때 반복문 탈출(더 이상 나눌 수 없음)
        break
    result+=1
    n//=k #k로 나누기

result+=n-1  #마지막으로 남은 수에 대해 1씩 빼기
print(result)