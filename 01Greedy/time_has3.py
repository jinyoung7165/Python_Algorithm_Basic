'''
정수 N이 입력되면 00시 00분 00초부터 N시 59분 59초까지의 모든 시각 중에서 3이 하나라도 포함되는 모든 경우의 수를 구하는 프로그램
'''
#가능한 모든 시각의 경우를 하나씩 모두 세서 풀 수 있는 완전 탐색 유형
n=int(input())
count=0
for i in range(n+1): #0시부터 n시까지
    for j in range(60): #분
        for k in range(60): #초
            if '3' in str(i)+str(j)+str(k): #시분초 문자열 안에 3이 포함되어 있는지
                count+=1
print(count)
