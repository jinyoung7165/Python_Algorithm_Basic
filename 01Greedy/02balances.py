#백준 2437 - 저울
#각 무게를 가진 추들이 주어졌을 때, 해당 추들로 만들 수 없는 양의 정수 중 최솟값
#추를 추가할 때마다 해당 추 무게만큼 측정가능범위의 시작,끝 달라짐
#추를 추가한 새로운 범위와 이전 범위가 겹치지 않으면 측정할 수 없는 값이 생긴 것
from sys import exc_info, stdin
input=stdin.readline
n=int(input()) #추의 개수
arr=list(map(int,input().split()))
arr.sort()
s=[0]*n
if arr[0]>1: #가장 작은 수가 1 이상일 때, 1 표현 불가
    print(1)
    exit()
s[0]=arr[0]
for i in range(1,n): #누적합 구해서 범위 겹치는지 확인
    s[i]=s[i-1]+arr[i] #누적합
    if arr[i]-s[i-1]>1: #뒷 범위의 시작(해당 추를 추가.0+arr[i])이 앞 범위의 끝보다 1이상 크면,앞 범위 마지막+1부터 측정 불가
        print(s[i-1]+1)
        exit()
print(s[n-1]+1) #측정불가 구간이 없었다면, 모든 누적합+1부터 측정 불가