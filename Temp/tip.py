#map 가로로 길게 입력 n번 받을 때
'''
n=3이고, 입력은 아래와 같이 들어올 때
0 1 0
1 0 1
0 0 1
'''
import collections

#최댓값 이거 쓰자!!!!
float('inf') #sys.maxsize 진짜 느림

graph = [list(map(int, input().split())) for _ in range(n)]

#세로로 원소 하나씩 입력될 때
'''
1
2
3
'''
graph = [int(input()) for _ in range(n)]

#list안 특정 조건의 수 셀 때
count = [i for i in list if i == True]
print(len(count))

#각 원소 가로로 띄어서 프린트
#1 2 3 4 5
print(*count)

nums = [1,1,1,2,2,3]
k=2
#nums의 원소 중 k개 이상 나타나는 원소들만 출력
result = collections.Counter(nums).most_common(k) #[(1, 3), (2, 2)]
# *result: (1,3) (2,2)
#list(zip(*result)): [(1,2), (3,2)] : zip+*의 힘.
list(zip(*result))[0] # unpacking시 안에 들어있는 시퀀스의 인덱스순서를 묶어 언패킹 (1,2) (3,2) => 결론적으로 collections.counter의 키만 출력 가능

a, *b = [1,2,3,4]
#a: 1, b: [2,3,4]
*c, d = [1,2,3,4]
#c:[1,2,3], d:4

date_info = {'year':'2022', 'month':'01', 'day': '7'}
new_info = {**date_info, 'day': '14'} #date_info의 나머지 멤버들 가지면서, day는 수정 가능

sum(nums[::2]) #짝수 번째 값만 더함 0,2,4,... 
sum(s in J for s in S) #S의 원소들에 대해, J에 속하면 true -> true 개수의 합

for i in list(graph): #defaultdict key를 통한 반복 시 반복할 때마다 변함 ->list로 해결
        pass

bin(2796202) #숫자-> 이진수 문자열
'0b1010101010101010101010'
str.zfill(5) #5자릿수 문자열 맞추기 위해 왼쪽에 '0'삽입
str.replace('1','#')

#다중집합 교집합-> collections.Counter() & collections.Counter() 두 집합에 존재해야 함
#그냥 집합 -> set() set() 끼리 intersection 연산자 존재