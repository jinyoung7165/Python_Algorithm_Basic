#백준 - 5052
#전화번호의 부분집합이 다른 전화번호의 접두어면 안된다
#최적이진코드-허프만과 유사
#한 번호가 다른 번호의 접두어면 NO출력
from sys import stdin
input=stdin.readline
for _ in range(int(input())):#테스트케이스
    tel=[]
    for i in range(int(input())):#총 몇 개의 번호 입력
        tel.append(input().rstrip())#string으로 들어감
    tel.sort()
    i=0
    while i<len(tel)-1:
        if tel[i] in tel[i+1][0:len(tel[i])]:#딱 그 길이만큼 검사해야함(123,9123경우 대비)
            print('NO')
            break
        i+=1
    if(i==len(tel)-1):print('YES')
if "abc" in "abcde":
    print("YES")
if "123" in "1234":
    print("YES")
