n=int(input())
arr=[] #n개의 정수 입력받아 리스트에 저장
for i in range(n):
    arr.append(int(input()))
arr=sorted(arr,reverse=True)
for i in arr:
    print(i,end='')