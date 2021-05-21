n=int(input())
arr=list(map(int,input().split()))
arr.reverse()  #순서를 뒤집어 LIS알고리즘 사용
dp=[1]*n  #오름차순 수열의 길이 저장
#주어진 arr: 15,11,4,8,5,2,4
#i번째 원소까지 내림차순 개수 (8>5,5>2)
#     dp[i]: 1, 2,3,3,4,5,5
#가장 긴 오름차순 수열 알고리즘
# 가장 긴 증가하는 부분 수열(LIS) 알고리즘 수행
for i in range(1, n): #전체 원소
    for j in range(0, i):  #해당 원소까지의 내림차순 개수를 기록
        if arr[j] < arr[i]:  #해당 원소보다 더 작은 원소가 더 앞쪽에 있으면
            dp[i] = max(dp[i], dp[j] + 1)

# 열외해야 하는 병사의 최소 수를 출력
print(n - max(dp))
'''
if arr= 12/321/789 이라면,
reverse->98712321
dp       11112321
max(dp)=3 오름차순
n-max(dp)=5명 열외하면 내림차순 완성'''
