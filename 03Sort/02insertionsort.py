#앞쪽 원소는 이미 정렬됐다고 가정하고, 현재 원소를 앞쪽 원소의 앞에 넣을지, 뒤에 넣을지를 판단
arr=[7,5,9,0,3,1,6,2,4,8]
for i in range(1,len(arr)):
    for j in range(i,0,-1):#i부터 1까지 1씩 감소
        if arr[j]<arr[j-1]:#왼쪽 원소보다 자신이 작으면
            arr[j],arr[j-1]=arr[j-1],arr[j] # 위치를 바꿈
        else:break #자기보다 작은 데이터를 만나면 멈춤
print(arr)