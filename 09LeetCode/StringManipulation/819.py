#금지된 단어를 제외한 가장 흔하게 등장하는 단어를 출력해라
#대소문자 구분x, 마침표, 쉼표 무시
#입력: "Bob hit a ball, the hit BALL flew far after it was hit."
#금지: ["hit"]
#출력: "ball"
import re
def mostcommonword(input = "Bob hit a ball, the hit BALL flew far after it was hit."):
    banned = ["hit"]
    words = [word for word in re.sub('[^\w]', ' ', input) #^\w :단어문자가 아닌 것 공백으로
        .lower().split()
            if word not in banned]
    
    counts = dict()
    for word in words:
        counts[word] = words.count(word)
    for key in counts.keys():
        if counts[key] == max(counts.values()):
            print(key)
    
mostcommonword()