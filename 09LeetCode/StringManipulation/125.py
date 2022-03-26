#주어진 문자열이 팰린드롬인지 확인. 대소문자 구분x. 영문자, 숫자만 대상
#뒤집어도 똑같은 말
from sys import stdin
from collections import deque
import re

def palindrome():
    str = deque()
    input = stdin.readline()

    for i in input:
        if i.isalnum():
            str.append(i.lower())

    while len(str) > 1:
        if str.pop() != str.popleft(): #리스트의 [-i-1]보다 시간복잡도 좋음
            return False

    return True
    
print(palindrome())

#더 빠른 정규식 필터 -> 슬라이싱
def palindrome():
    input = stdin.readline().lower()

    input = re.sub('[^a-z0-9]','',input) #불필요한 문자 제거
    
    return input == input[::-1] #문자열 거꾸로 뒤집은 거랑 비교