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
    maxSum = 0 # initialize maxsum to be 0
    windowSum = 0 # stores the sum of the window
    left = 0 # left pointer of the window

    for right in range(len(arr)): 
        windowSum += arr[right] # add elements to the window
        
        if right >= k-1: # once the window of size k has been established, now check for max sum
            maxSum = max(maxSum, windowSum)
            windowSum -= arr[left] # remove left element from the window sum
            left += 1 # increment left pointer

    return maxSum


print(max_sub_array_of_size_k(3, [2, 1, 5, 1, 3, 2]))
print(max_sub_array_of_size_k(2, [2, 3, 4, 1, 5]))       
    