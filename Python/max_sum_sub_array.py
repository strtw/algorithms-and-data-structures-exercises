def max_sum_subarray(arr):
    """
    :param - arr - input array
    return - number - largest sum in contiguous subarry within arr
    """
    currentSum = arr[0]
    maxSum = arr[0]
    for elem in arr[1:]:
        currentSum = max(currentSum + elem , elem)
        maxSum = max(currentSum, maxSum)
        
    return maxSum


print(max_sum_subarray([1, 2, 3, -4, 6]) == 8) # True
print(max_sum_subarray([1, 2, -5, -4, 1, 6]) == 7) # True
print(max_sum_subarray([1, 2, 3,-3,4]) == 7) # True
print(max_sum_subarray([1, 2, 3,-6,0]) == 6) # True
