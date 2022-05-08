#Valid Parentheses
#괄호로 된 입력값이 올바른지
#입력: ()[]{}  출력: True
#[{()}]

arr = list(input())
stack = []
dict = {']':'[', '}':'{', ')':'('}

def parentheses():
    for i in arr:
        if i not in dict:
            stack.append(i) #여는 괄호를 stack에
        elif not stack or dict[i] != stack.pop():
            return False          
    return len(stack) == 0 #스택이 비어있어야 짝을 제대로 맞춘 것
print(parentheses())