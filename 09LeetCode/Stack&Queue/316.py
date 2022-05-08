#remove duplicate letters
#중복 문자 제외하고 사전식 순서로 나열하라
#bcabc->abc
#ebcabc->eabc (e중복 없기 때문에 위치 그대로)
##ebcabce->abce
#cbacdcbc->acbd
#중복제거.알파벳 순 문자열 정렬 -> 앞부분부터 접미사suffix를 분리해 확인
#전체 집합과 접미사 집합이 일치하면 분리 가능
#재귀 이용
import collections


def removeDuplicateLetters(s):
    for char in sorted(set(s)):
        suffix = s[s.index(char):]
        if set(s) == set(suffix): #전체 집합과 접미사 집합이 일치하면 분리
            return char + removeDuplicateLetters(suffix.replace(char, ''))
    return ''

print(removeDuplicateLetters('cbacdcbc'))

def removeDuplicateLettersStack(s):
    #현재 문자가 stack에 쌓여 있는 문자이고(이전보다 앞선), 뒤에 다시 붙일 문자가 남아있다면(counter가 1이상이라면), 쌓아둔 걸 꺼내서 없앰
    #counter: 문자별 개수를 셈
    counter, stack = collections.Counter(s), []
    for char in s:
        counter[char] -= 1 #하나 꺼냄
        if char in stack: continue #이미 처리된 문자면 무시
        #뒤에 붙일 문자가 남아있다면 스택에서 제거
        while stack and char < stack[-1] and counter[stack[-1]] > 0:#현재가 이전 문자보다 앞섰고, 이전문자들의 개수가 남아있으면
            stack.pop()
        stack.append(char)
    return ''.join(stack)