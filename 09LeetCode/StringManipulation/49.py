#그룹 애너그램
#문자열 배열을 받아 애너그램 단위로 그룹핑하라
#입력: ["eat", "tea", "tan", "ate", "nat", "bat"]
''' 출력:
    [
        ["ate","eat","tea"],
        ["nat","tan"],
        ["bat"]
    ]
'''
from collections import defaultdict

def groupanagram(input = ["eat", "tea", "tan", "ate", "nat", "bat"]):
    group = defaultdict(list) #value값으로 list 저장하기 위함
    for obj in input:
        #print(sorted(obj)) #['a', 'e', 't']
        group[''.join(sorted(obj))].append(obj)
    return list(group.values())
        
print(groupanagram())