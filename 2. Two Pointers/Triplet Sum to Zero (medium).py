'''
Problem Statement 
Given an array of unsorted numbers, find all unique triplets in it 
that add up to zero.

Example 1:
Input: [-3, 0, 1, 2, -1, 1, -2]
Output: [-3, 1, 2], [-2, 0, 2], [-2, 1, 1], [-1, 0, 1]
Explanation: There are four unique triplets whose sum is equal to zero.

Example 2:
Input: [-5, 2, -1, -2, 3]
Output: [[-5, 2, 3], [-2, -1, 3]]
Explanation: There are two unique triplets whose sum is equal to zero.
'''

def search_triplets(arr):
    triplets = []
    arr.sort()
    # TODO: Write your code here
    for i in range(len(arr)):
        search_pairs(arr, arr[i], i+1, triplets)

    return triplets


def search_pairs(arr, target_sum, left, triplets):
    right = len(arr) - 1
    i = left - 1
    
    while left < right:
        current_sum = arr[left] + arr[right]

        if current_sum == -1*target_sum:
            triplets.append([arr[i], arr[left], arr[right]])
            left += 1 
        elif current_sum > target_sum:
            current_sum -= arr[left]
            left += 1

            while left < right and arr[left+1] == arr[left]:
                left += 1
        else:
            current_sum -= arr[right]
            
            right -= 1
            while left < right and arr[right-1] == arr[right]:
                right -= 1

print(search_triplets([-3, 0, 1, 2, -1, 1, -2]))
print(search_triplets([-5, 2, -1, -2, 3]))