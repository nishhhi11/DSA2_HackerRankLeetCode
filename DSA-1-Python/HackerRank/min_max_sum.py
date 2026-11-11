arr = [1, 3, 5, 7, 9]

def MinMax(arr):
    total = sum(arr)
    minSum = total - max(arr)
    maxSum = total - min(arr)

    return minSum, maxSum

min_sum, max_sum = MinMax(arr)

print(min_sum, max_sum)