'''큰 수의 법칙
숫자로 이루어진 배열, 주어진 수들을 M번 더하여 가장 큰 수를 만들자
배열의 특정한 인덱스에 해당하는 수가 연속해서 K번을 초과해 더해질 수 없다.
배열의 크기 N, 더하기 연산 수 M, K가 주어질 때 결과
'''
n,m,k=map(int,input().split())
arr=list(map(int,input().split()))
arr.sort(reverse=True)
result=0
count=0
totalcount=0
i=0
'''while(totalcount<m):
    result+=arr[i]
    count+=1
    totalcount+=1
    if(arr[i-1]>arr[i] and i!=0):
        i-=1
        count=0
    if(count==k):
        if(i==0):i=1
        else:i=0
        count=0
'''
repeat=(m//(k+1))
remainder=m%(k+1)
if(arr[0]==arr[1]):
    result=m*arr[0]
else:
    if(m%(k+1)!=0):
        result=repeat*(arr[0]*k+arr[1])+remainder*arr[0]
    else:
        result=repeat*(arr[0]*k+arr[1])

print(result)