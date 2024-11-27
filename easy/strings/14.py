# 14. Longest Common Prefix
# https://leetcode.com/problems/longest-common-prefix/

def function(strs):
    longestCommonPrefix = ""
    
    # sort the strings according to the length in ASC
    strs = sorted(strs, key=len)

    # iterate through the strings
    for i in range(len(strs[0])):
        # check if all the strings have the same character at the same index
        if(all(strs[0][i] == strs[j][i] for j in range(len(strs)))):
            longestCommonPrefix = longestCommonPrefix + strs[0][i]
        else:
            break
    return longestCommonPrefix


# Test Case 1
input_1 = ["flower","flow","flight"]
expected_output_1 = "fl"

# Test Case 2
input_2 = ["dog","racecar","car"]
expected_output_2 = ""


try:
    assert function(input_1) == expected_output_1, f'Test Case 1 Failed'
    assert function(input_2) == expected_output_2, f'Test Case 2 Failed'
    print('\033[92m All test cases passed! \033[0m')
except AssertionError as e:
    print('\033[91m Error: {}\033[0m'.format(e))