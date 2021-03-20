'''
알파벳 대문자와 숫자로만 구성된 문자열이 주어진다.
모든 알파벳을 정렬 후, 그 뒤에 모든 숫자를 더한 값을 이어서 출력
'''
data=input()
result=[]
value=0

for x in data:
    if x.isalpha():  #알파벳인 경우 따로 저장
        result.append(x)
    else:
        value+=int(x) #숫자는 더한다

result.sort() #알파벳 오름차순 정렬

if value!=0:
    result.append(str(value)) #합을 문자열 뒤에 붙이기

print(result)  #['a','b','c'] 리스트로 출력
print(''.join(result))  #abc로 이어져서 문자열로 출력(''는 구분자 역할)
