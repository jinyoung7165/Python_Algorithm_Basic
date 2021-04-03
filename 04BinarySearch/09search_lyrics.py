from bisect import bisect_left,bisect_right
def count_by_range(a, left_value, right_value): #[left_value,right_value] 인 데이터의 개수 반환
    right_index = bisect_right(a, right_value)
    left_index = bisect_left(a, left_value)
    return right_index - left_index
arr=[[]for _ in range(100)] #모든 단어들을 길이마다 나누어 저장하기 위한 리스트.100칸짜리 중첩리스트
reversed_arr=[[]for _ in range(100)] #모든 단어들을 길이마다 나누어서 뒤집어 저장하기 위한 리스트
def solution(words, queries): #각 키워드별로 매치된 단어가 몇 개인지 반환
    answer = []
    for word in words: #모든 단어를 접미사 와일드카드배열, 접두사 와일드카드 배열에 각각 삽입
        arr[len(word)].append(word) #단어를 삽입, arr[5]에는 ['frodo', 'front', 'frost', 'frame', 'kakao'] 저장.
        reversed_arr[len(word)].append(word[::-1]) #단어를 뒤집어서 삽입. reversed_arr[5]에는 ['odorf', 'tnorf', 'tsorf', 'emarf', 'oakak']저장
    for i in range(100): #이진 탐색을 수행하기 위해 각 단어 리스트 정렬 수행
        arr[i].sort()
        reversed_arr[i].sort()
    for q in queries: #쿼리를 하나씩 확인하며 처리
        if q[0]!='?': #접미사에 와일드카드가 붙은 경우. q: ---?? 꼴
            res=count_by_range(arr[len(q)],q.replace('?','a'),q.replace('?','z'))
        else: #접두사에 와일드카드가 붙은 경우 q:??--- 꼴 ->q[::-1]를 통해 뒤집음 ---?? 꼴
            res=count_by_range(reversed_arr[len(q)],q[::-1].replace('?','a'),q[::-1].replace('?','z'))
        answer.append(res)
    print(answer)
    return answer
solution(["frodo", "front", "frost", "frozen", "frame", "kakao"],["fro??", "????o", "fr???", "fro???", "pro?"])