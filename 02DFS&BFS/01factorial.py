#반복문
def factorial_itetative(n):
    result=1
    for i in range(1,n+1): # 1부터 n 곱하기
        result*=i
    return result

#재귀함수
def factorial_recursive(n):
    if n<=1:
        return 1
    return n*factorial_recursive(n-1) # n*(n-1)

print(factorial_itetative(5))
print(factorial_recursive(5))