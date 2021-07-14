#1541 - 잃어버린 괄호.
#55-50+40=>55-90=-35 최소!
#-후 -나올 때가지 괄호로 묶어 최종결과에서 뺀다
arr=input().split('-') #-기준으로 나눔
result=0
for i in arr[0].split('+'): #+로 연결된 숫자들 더함
    result+=int(i) #초기값
for i in arr[1:]: #-앞 뒤의 식 배열
    for j in i.split('+'): #+로 연결된 숫자들 최종적으로 뺀다
        result-=int(j)
print(result)


