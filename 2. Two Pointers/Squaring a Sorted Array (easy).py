'''
Problem Statement 
Given a sorted array, create a new array containing squares
of all the number of the input array in the sorted order.

Example 1:
Input: [-2, -1, 0, 2, 3]
Output: [0, 1, 4, 4, 9]

Example 2:
Input: [-3, -1, 0, 1, 2]
Output: [0 1 1 4 9]
'''

def make_squares(arr):
    result = []
    L = 0 
    R = len(arr)-1

    while L <= R:
        if arr[L]**2 > arr[R]**2:
            result.insert(0, arr[L]**2)
            L += 1
        else:
            result.insert(0, arr[R]**2)
            R -= 1

    return result 

print(make_squares([-2, -1, 0, 2, 3]))
print(make_squares([-3, -1, 0, 1, 2]))