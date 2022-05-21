#서로 다른 정수 입력받아 가능한 모든 순열 리턴하라
#[1,2,3] => [[1,2,3], [1,3,2], [2,1,3], ...]
from itertools import permutations

def permute(nums = [1,2,3]):
    return list(map(list, permutations(nums)))

print(permute())