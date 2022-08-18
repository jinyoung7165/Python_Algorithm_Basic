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
    wordSentence = []
    wordQuery = []
    sentenceDict = defaultdict(list)
    
    for idx, sentence in enumerate(sentences): #wordSentence: [[jim,mary,likes], [kate,likes,tom], [tom,does,not,like,jim]]
        wordSentence.append(sentence.split())
        for word in wordSentence[idx]:
            sentenceDict[word].append(idx)  #[jim:[0,2], likes:[0,1], tom:[1,2]...]
            
    result = [[] for _ in range(len(queries))]
    
    for idx, querySentence in enumerate(queries): #['jim','tom'], ['likes']
        wordQuery.append(querySentence.split()) #['jim','tom']
        firstKey = sentenceDict[wordQuery[idx][0]] #'jim' -> [0,2]
        if firstKey:
            for sentenceIdx in firstKey:
                if set(wordQuery[idx]).issubset(set(wordSentence[sentenceIdx])):
                    result[idx].append(sentenceIdx)
        if not result[idx]:
            result[idx].append(-1)
            
    return result

'''
def textQueries(sentences, queries):
    wordSentence = []
    wordQuery = []
    result = [[] for _ in range(len(queries))]
    
    for sentence in sentences: #wordSentence: [[jim,mary,likes], [kate,likes,tom], [tom,does,not,like,jim]]
        wordSentence.append(sentence.split())  
    
    for querySentence in queries: #wordQuery: ['jim','tom'], ['likes']
        wordQuery.append(querySentence.split()) #['jim','tom']
 
    for idx, query in enumerate(wordQuery):
        for sentenceIdx, sentenceWord in enumerate(wordSentence):
            if set(query).issubset(set(sentenceWord)):
                result[idx].append(sentenceIdx)
                
        if not result[idx]:
            result[idx].append(-1)
            
    return result
'''
print(textQueries(['jim likes mary', 'kate likes tom', 'tom does not like jim'], ['jim tom', 'likes', 'like'])) #[[2], [0, 1], [2]]
print(textQueries(['jim likes mary', 'kate likes tom', 'tom does not like jim'], ['jim tom likes', 'likes', 'like'])) #[[-1], [0, 1], [2]]