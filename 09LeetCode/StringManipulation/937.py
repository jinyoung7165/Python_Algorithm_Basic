#로그 재정렬
#로그 가장 앞 부분은 식별자
#문자로 구성된 로그가 숫자 로그 보다 앞에 옴
#문자가 동일한 경우에는 식별자 순으로
#숫자 로그는 입력 순대로
#입력: ["dig2 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dog", "let3 art zero"]
#출력: ["let1 art can","let3 art zero","let2 own kit dig","dig1 8 1 5 1","dig2 3 6"]
def reorderlog(arr):
    num, alp = [], []
    for obj in arr:
        if obj.split()[1].isdigit():
            num.append(obj)
        else:
            alp.append(obj)

    alp.sort(key= lambda x: (x.split()[1:], x.split()[0])) #문자의 경우, 값 순 -> 식별자 순
    return alp + num
    
    

input = ["dig2 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dog", "let3 art zero"]
print(reorderlog(input))