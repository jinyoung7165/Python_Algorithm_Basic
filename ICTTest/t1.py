def balancedSum(arr):
    # Write your code here
    start, end = 0, len(arr) - 1
    while start <= end:
        mid = (start + end) // 2
        left = sum(arr[:mid])
        right = sum(arr[mid+1:])
        if left == right:
            return mid
        elif left > right:
            end = mid - 1
        else:
            start = mid + 1
    return None