# 344. Reverse String
# https://leetcode.com/problems/reverse-string/description/

def function(inputs):
    # iterate through the string
    for i in range(len(inputs)//2):
        # swap the characters without using a temp variable
        inputs[i], inputs[-i-1] = inputs[-i-1], inputs[i]
    return inputs


# Test Case 1
input_1 = ["h","e","l","l","o"]
expected_output_1 = ["o","l","l","e","h"]

# Test Case 2
input_2 = ["H","a","n","n","a","h"]
expected_output_2 = ["h","a","n","n","a","H"]

# Test Case 3
# input_3 = []
# expected_output_3 = []
# assert function(input_3) == expected_output_3, f"Test Case 3 Failed"

try:
    assert function(input_1) == expected_output_1, f'Test Case 1 Failed'
    assert function(input_2) == expected_output_2, f'Test Case 2 Failed'
    #assert function(input_3) == expected_output_3, f'Test Case 3 Failed'
    print('\033[92m All test cases passed! \033[0m')
except AssertionError as e:
    print('\033[91m Error: {}\033[0m'.format(e))