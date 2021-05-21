d=[0]*100  #한 번 계산된 결과를 메모하기 위한 리스트 초기화

#피보나치 수열을 재귀함수로 구현(탑다운.하향식)
def fibo(x):
    if x==1 or x==2:
        return 1
    if d[x]!=0:  #이미 계산한 적 있는 문제면 그대로 반환
        return d[x]
    d[x]=fibo(x-1)+fibo(x-2)  #아직 계산하지 않은 문제라면 점화식에 따라 결과 반환
    return d[x]
print(fibo(99))

#O(n)