#정렬되지 않은 데이터 중 가장 작은 데이터를 맨 앞으로
arr=[7,5,9,0,3,1,6,2,4,8]
for i in range(len(arr)):
    min_index=i#가장 작은원소의 인덱스
    for j in range(i+1,len(arr)):
        if arr[min_index]>arr[j]: #이후의 원소가 더 작으면
            min_index=j
        arr[i],arr[min_index]=arr[min_index],arr[i]#서로 위치를 바꿈
print(arr)