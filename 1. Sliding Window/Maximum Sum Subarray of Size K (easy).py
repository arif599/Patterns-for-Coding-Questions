"""
Problem statement: 
    Given an array of positive numbers and a positive number ‘k’, 
    find the maximum sum of any contiguous subarray of size ‘k’.

Example 1:
    Input: [2, 1, 5, 1, 3, 2], k=3 
    Output: 9
    Explanation: Subarray with maximum sum is [5, 1, 3].

Example 2:
    Input: [2, 3, 4, 1, 5], k=2 
    Output: 7
    Explanation: Subarray with maximum sum is [3, 4].
"""

def max_sub_array_of_size_k(k, arr):
    maxSum = 0
    windowSum = 0
    left = 0

    for right in range(len(arr)):
        windowSum += arr[right]
        
        if right >= k-1:
            maxSum = max(maxSum, windowSum)
            windowSum -= arr[left]
            left += 1

    return maxSum


print(max_sub_array_of_size_k(3, [2, 1, 5, 1, 3, 2]))
print(max_sub_array_of_size_k(2, [2, 3, 4, 1, 5]))       
    