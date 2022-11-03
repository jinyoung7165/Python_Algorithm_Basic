#Task Scheduler
#각 간격마다 CPU는 1개의 TASK만 실행 가능
#n번의 간격 내에는 동일 태스크를 실행할 수 없음
#더 이상 태스크실행 불가 시 idle상태
#모든 태스크를 실행하기 위한 최소 간격 구하라
#["A","A","A","B","B","B"], n=2일 때 -> 8(A>B>idle>A>B>idle>A>B)
#{A:4, B:2}
#n=1이면 ABABA-A
#마지막 A 실행되기 위해선 B 세트 3(A개수-1)개 필요
#n=2이면 AB-AB-A--A
#마지막 A 실행되기 위해선 B- 세트 3개 필요
#전체 간격: max_count + (max_count-1) * n

#{A:3, B:3, C:2} maxTask가 여러 개일 때
#n=1이면 ABCABCA -> B까지 실행. 3(A)+2*2(BC)+1(B)=8
#전체 간격: max_count + (max_count-1) * n + (maxTask개수-1)
#n=4이면 ABC-ABC-A -> B까지 실행. 3(A)+2*3(BC-)+1(B)=10 

#{A:3, B:3, C:3, D:2, E:1} maxTask가 여러 개일 때
#n=2이면 ABCDABCDABCE ->len(tasks):12
#위의 식 실행 시 3+2*2+2=9로 D,E를 무시해버림

import collections
def leastInterval(tasks, n):
    if n == 0:
        return len(tasks)
        
    counts = collections.Counter(tasks)
    max_count = counts.most_common()[0][1] 
    max_task_count = list(counts.values()).count(max_count)  #max count를 가지는 task 여러 개

    ans = max_count + (max_count-1) * n + (max_task_count-1)
    return max(ans, len(tasks))
    