#기준 데이터를 설정하고, 그것보다 큰 데이터와 작은 데이터의 위치를 바꿈
#첫 번째 데이터를 기준(pivot) 데이터로 설정
#O(NlogN)
arr=[5,7,9,0,3,1,6,2,4,8]
def quick(arr,start,end):
    if start>=end:#원소가 1개인 경우 종료
        return
    pivot=start#피벗은 첫번째 원소
    left=start+1#두번째 원소부터 left
    right=end#가장 오른쪽
    while(left<=right):
        #왼쪽부터 피벗보다 큰 데이터를 찾을 때까지 반복
        while(left<=end and arr[left]<=arr[pivot]):
            left+=1
        #오른쪽부터 피벗보다 작은 데이터를 찾을 때까지 반복
        while(right>start and arr[right]>=arr[pivot]):
            right-=1
        if(left>right):#엇갈렸다면 작은데이터와 피벗을 교체
            arr[right],arr[pivot]=arr[pivot],arr[right]
        else:#엇갈리지 않았다면 작은데이터와 큰데이터를 교체
            arr[left],arr[right]=arr[right],arr[left]
    #분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬 수행
    quick(arr,start,right-1)
    quick(arr,right+1,end)
quick(arr,0,len(arr)-1)
print(arr)