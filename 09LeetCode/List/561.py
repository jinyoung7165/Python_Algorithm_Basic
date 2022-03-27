#배열파티션1
#n개의 페어를 이용한 min(a,b)의 합으로 만들 수 있는 가장 큰 수
#입력: [1,4,3,2]
#출력: 4
#n은 2가 되며, 최대합은 4이다. min(1,2) + min(3,4) = 4
def arrpair(nums = [1,4,3,2]):
    nums.sort()
    return sum(nums[::2]) #짝수 번째 값만 더함 0,2,4,... 

print(arrpair())