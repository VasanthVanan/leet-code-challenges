# 125. Valid Palindrome
# https://leetcode.com/problems/valid-palindrome/description/

def function(inputs):
    s = inputs[0]
    # remove all non-alphanumeric characters and convert to lowercase
    s = ''.join(a for a in s if a.isalnum()).strip().lower()
    # compare the string to its reverse
    return True if s == s[::-1] else False


# Test Case 1
input_1 = ["A man, a plan, a canal: Panama"]
expected_output_1 = True

# Test Case 2
input_2 = ["race a car"]
expected_output_2 = False

# Test Case 3
input_3 = [" "]
expected_output_3 = True

try:
    assert function(input_1) == expected_output_1, f'Test Case 1 Failed'
    assert function(input_2) == expected_output_2, f'Test Case 2 Failed'
    assert function(input_3) == expected_output_3, f'Test Case 3 Failed'
    print('\033[92m All test cases passed! \033[0m')
except AssertionError as e:
    print('\033[91m Error: {}\033[0m'.format(e))