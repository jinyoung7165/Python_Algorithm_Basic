#두 배열a,b는 n개의 원소로 구성
#최대 k번 바꿔치기 연산 수행
#배열a의 모든 원소의 합이 최댓값 출력

n,k=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
a.sort()
b.sort(reverse=True)
for i in range(k):
    if a[i]<b[i]:
        a[i],b[i]=b[i],a[i]
    else:
        break
print(sum(a))