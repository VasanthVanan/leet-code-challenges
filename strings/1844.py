# 1844. Replace All Digits with Characters
# https://leetcode.com/problems/replace-all-digits-with-characters 

def function(s):
    result = ''
    for i in range(0,len(s)):
        # if index is odd, shift the character by the number in the i-th index: shift(prev, i)
        result = result + chr(int(s[i]) + ord(s[i-1])) if i % 2 != 0 else result + s[i]
    return result

# Test Case 1
input_1 = "a1c1e1"
expected_output_1 = "abcdef"

# Test Case 2
input_2 = "a1b2c3d4e"
expected_output_2 = "abbdcfdhe"

# Test Case 3
input_3 = "v0g6s4d"
expected_output_3 = "vvgmswd"

try:
    assert function(input_1) == expected_output_1, f'Test Case 1 Failed'
    assert function(input_2) == expected_output_2, f'Test Case 2 Failed'
    assert function(input_3) == expected_output_3, f'Test Case 3 Failed'
    print('\033[92m All test cases passed! \033[0m')
except AssertionError as e:
    print('\033[91m Error: {}\033[0m'.format(e))