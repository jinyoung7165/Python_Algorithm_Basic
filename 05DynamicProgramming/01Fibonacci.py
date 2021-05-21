def fibo(x):
    if x==1 or x==2:
        return 1
    return fibo(x-1)+fibo(x-2)

print(fibo(4))

#시간효율 별로. 중복 호출 문제
#큰 문제를 작은 문제로 나눌 수 있음
#동일한 작은 문제를 반복적으로 해결 가능
#다이나믹 프로그래밍으로 풀어보자!(상향식/하향식)
#하향식: 재귀함수,한 번 계산한 결과를 메모리 공간에 메모(캐싱,메모이제이션)
#상향식: 보텀업 방식. DP테이블(리스트), 반복문
