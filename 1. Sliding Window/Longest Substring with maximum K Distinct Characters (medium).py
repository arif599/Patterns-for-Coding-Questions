"""
Problem Statement:
    Given a string, find the length of the longest substring in it with no more than K distinct characters.

Example 1:
    Input: String="araaci", K=2
    Output: 4
    Explanation: The longest substring with no more than '2' distinct characters is "araa".

Example 2:
    Input: String="araaci", K=1
    Output: 2
    Explanation: The longest substring with no more than '1' distinct characters is "aa".

Example 3:
    Input: String="cbbebi", K=3
    Output: 5
    Explanation: The longest substrings with no more than '3' distinct characters are "cbbeb" & "bbebi".
    
Example 4:
    Input: String="cbbebi", K=10
    Output: 6
    Explanation: The longest substring with no more than '10' distinct characters is "cbbebi".
"""

def longest_substring_with_k_distinct(str1, k):
    maxLen = 0
    windowLen = 0
    L = 0 
    hashmap = {}
  
    for R in range(len(str1)):
        if str1[R] not in hashmap:
            hashmap[str1[R]] = 1
            windowLen += 1
        else:
            hashmap[str1[R]] += 1
            windowLen += 1

        while len(hashmap) > k:
            maxLen = max(maxLen, windowLen-1)

            hashmap[str1[L]] -= 1
            if hashmap[str1[L]] == 0:
                del hashmap[str1[L]]

            windowLen -= 1
            L += 1
    
    if maxLen == 0:
        return windowLen

    return maxLen

print(longest_substring_with_k_distinct("araaci", 2))
print(longest_substring_with_k_distinct("araaci", 1))
print(longest_substring_with_k_distinct("cbbebi", 3))
print(longest_substring_with_k_distinct("cbbebi", 10))