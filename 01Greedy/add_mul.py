'''각 자리 숫자(0부터 9)로만 이루어진 문자열 S가 주어졌을 때, 왼쪽부터
오른쪽으로 하나씩 모든 숫자를 확인하며 x또는 +연산자를 넣어 가장 큰 수를 구하는 프로그램
모든 연산은 왼쪽에서부터 순서대로 이루어진다.'''
#1이하의 수의 경우, 더하는 것이 결과가 크게 나온다
data=input()
result=int(data[0]) #첫 번째 문자를 숫자로 변경
for i in range(1,len(data)):# 두 수 중 하나라도 1이하라면, 더하기 연산
    num=int(data[i])
    if(num<=1 or result<=1):
        result+=num
    else: result*=num
print(result)