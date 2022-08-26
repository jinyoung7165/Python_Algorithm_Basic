#후위 표기식
#연산자가 피연산자 뒤에 위치
#a+b*c-> abc*+
#괄호 안의 우선순위 높은 연산자부터 피연산자의 오른쪽으로
#+,-,*,/,(,)
S = list(input())
op = {'+':1, '-':1, '*':2, '/':2, '(':3, ')':3}
op_stack = []
result = ''
for i in S:
    if i.isalpha():
        result += i
    else:
        if i == '(':
            op_stack.append(i)
        elif i == ')':
            while op_stack and op_stack[-1] != '(':
                result += op_stack.pop()
            op_stack.pop() #(는 버림
        elif op[i] == 2:
            while op_stack and op[op_stack[-1]] == 2:
                result += op_stack.pop() #먼저 넣은 */부터 실행
            op_stack.append(i)
        elif op[i] == 1:
            while op_stack and op_stack[-1] != '(':
                result += op_stack.pop() #먼저 넣은 op부터 실행
            op_stack.append(i)
            
while op_stack:
    result += op_stack.pop()
    
print(result)