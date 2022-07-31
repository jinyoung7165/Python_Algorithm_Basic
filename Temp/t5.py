'''
sentences = ['jim likes mary', 'kate likes tom', 'tom does not like jim']
queries = ['jim tom', 'likes']
=> queries 안의 단어 모두가 sentence에서 검색되면 sentence의 idx나열, 어디에도 검색되지 않으면 -1)
=> 출력 결과
-----
2 (0번 쿼리가 [2]에서 검색됨)
0 1 (1번 쿼리가 [0], [1]에서 검색됨)
-----
'''
from collections import defaultdict

def textQueries(sentences, queries):
    sentenceDict = defaultdict(list)
    
    for idx, sentence in enumerate(sentences):
        wordSentence = sentence.split()
        for word in wordSentence:
            sentenceDict[idx].append(word)
            
    result = [[] for _ in range(len(queries))]

    for idx, querySentence in enumerate(queries):
        wordQuery = querySentence.split()
        flag = False
        for dict in sentenceDict:
            left = len(wordQuery)
            for query in wordQuery:
                if query in sentenceDict[dict]:
                    left -= 1
                    if left == 0:
                        result[idx].append(dict)
                        flag = True
                else:
                    break
        if flag == False: #not found in any sentence
            result[idx].append(-1)
            
    return result


print(textQueries(['jim likes mary', 'kate likes tom', 'tom does not like jim'], ['jim tom', 'likes']))