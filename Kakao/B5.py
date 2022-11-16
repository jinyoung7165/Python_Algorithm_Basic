#뉴스 클러스터링
#자카드 유사도 : 교집합 크기/합집합 크기
#FRENCH, FRANCE 주어졌을 때
# -> {FR,RE,EN,NC,CH}, {FR,RA,AN,NC,CE}로 나눠서 유사도 계산
#교집합 {FR, NC} : 크기2
#합집합 {FR,RA,AN,CE,RE,EN,NC,CH} : 크기8
#입력 str1, str2들어오는데, 공백, 특수문자, 숫자 부분은 버린다, 대소문자 구분x
#다중집합 교집합-> collections.Counter() & collections.Counter() 두 집합에 존재해야 함
#그냥 집합 -> set() set() 끼리 intersection 연산자 존재
import re, collections

def solution(str1, str2):
    #두 글자씩 끊어 다중 집합 계산
    str1s = [
        str1[i:i+2].lower()
        for i in range(len(str1)-1)
        if re.findall('[a-z]{2}', str1[i:i+2].lower())
    ]
    
    str2s = [
        str2[i:i+2].lower()
        for i in range(len(str2)-1)
        if re.findall('[a-z]{2}', str2[i:i+2].lower())
    ]
    
    #교집합 계산
    intersection = sum((collections.Counter(str1s) &
                        collections.Counter(str2s)).values())
    
    #합집합 계산
    union = sum((collections.Counter(str1s) |
                 collections.Counter(str2s)).values())
    
    #자카드 유사도 계산
    jaccard = 1 if union == 0 else intersection/union
    
    return int(jaccard * 65536)

def custom_solution(str1, str2):
    str1s = [str1[i:i+2].lower()
             for i in range(len(str1)-1)
             if str1[i:i+2].isalpha()]
    
    str2s = [str2[i:i+2].lower()
             for i in range(len(str2)-1)
             if str2[i:i+2].isalpha()]
    
    intersection = sum((collections.Counter(str1s) &
                        collections.Counter(str2s)).values())
    union = sum((collections.Counter(str1s) |
                 collections.Counter(str2s)).values())
    
    jaccard = 1 if union == 0 else intersection/union
    
    return int(jaccard * 65536)

print(custom_solution("FRANCE","french")) #16384
print(custom_solution("handshake","shake hands")) #65536
print(custom_solution("aa1+aa2","AAAA12")) #43690
print(custom_solution("e=m*c^2","e=m*c^2")) #65536